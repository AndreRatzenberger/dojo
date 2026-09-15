from __future__ import annotations

import json
import sys
import tempfile
import threading
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills/dojo/scripts"))
import dojo_workbench as wb
from dojo_harness import ContractError, validate_skill


class WorkbenchTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.root = self.base / "session"
        wb.init_session(self.root, "release-notes", "Release notes", "Write useful release notes.", "fast")
        wb.add_case(self.root, "first", "A small release", "Summarize these changes.", ["Includes the fix"])
        self.skill = self.base / "release-notes"
        self.skill.mkdir()
        (self.skill / "SKILL.md").write_text('---\nname: release-notes\ndescription: "Write release notes when asked."\n---\nKeep the fix.\n')
        wb.snapshot(self.root, "v1", self.skill, "First candidate")
        wb.start_run(self.root, "candidate-1", "first", "candidate", "v1")
        self.checks = [{"criterion": "Includes the fix", "status": "passed", "evidence": "The output names the fixed behavior."}]

    def finish(self):
        return wb.finish_run(self.root, "candidate-1", "passed", "The fix is present.", self.skill, self.checks)

    def test_lifecycle_keeps_inputs_and_artifacts_and_missing_metrics(self):
        case = self.root / "cases/first.json"
        changed = wb.read_json(case)
        changed["criteria"] = ["A later criterion"]
        wb.write_json(case, changed)
        result = self.finish()
        self.assertEqual(result["case"]["criteria"], ["Includes the fix"])
        self.assertIsNone(result["tokens"])
        self.assertIsNone(result["duration_seconds"])
        (self.skill / "SKILL.md").write_text("Changed after the run")
        path, _ = wb.artifact(self.root, "runs", "candidate-1", "SKILL.md")
        self.assertIn("Keep the fix.", path.read_text())
        self.assertEqual(wb.state(self.root)["runs"][0]["status"], "passed")
        with self.assertRaisesRegex(ContractError, "immutable"):
            self.finish()
        with self.assertRaisesRegex(ContractError, "already exists"):
            wb.snapshot(self.root, "v1", self.skill, "Overwrite the original")

    def test_no_pass_without_predeclared_checks_or_with_fake_metrics(self):
        for checks in ([], self.checks * 2, [{**self.checks[0], "criterion": "Invented afterwards"}]):
            with self.assertRaises(ContractError):
                wb.finish_run(self.root, "candidate-1", "passed", "Result", None, checks)
        for tokens, duration in ((-1, None), (True, None), (None, float("nan")), (None, -1)):
            with self.assertRaises(ContractError):
                wb.finish_run(self.root, "candidate-1", "passed", "Result", None, self.checks, tokens, duration)
        with self.assertRaises(ContractError):
            wb.add_case(self.root, "empty", "No criteria", "A task", [])
        with self.assertRaises(ContractError):
            wb.start_run(self.root, "missing-revision", "first", "candidate", None)

    def test_failed_invalid_and_unproven_stay_distinct(self):
        for status in ("failed", "invalid", "unproven"):
            wb.start_run(self.root, status, "first", "baseline", None)
            result = wb.finish_run(self.root, status, status, "The recorded reason", None, [])
            self.assertEqual(result["status"], status)

    def test_feedback_survives_reload_and_stale_writes_fail(self):
        review = {"run_id": "candidate-1", "decision": "needs-changes", "comment": "Show the user impact.", "version": 0}
        with self.assertRaisesRegex(ContractError, "finish"):
            wb.save_feedback(self.root, review)
        self.finish()
        saved = wb.save_feedback(self.root, review)
        self.assertEqual(wb.state(wb.session_root(self.root))["feedback"], [saved])
        with self.assertRaisesRegex(ContractError, "another tab"):
            wb.save_feedback(self.root, review)
        with self.assertRaises(ContractError):
            wb.save_feedback(self.root, {**review, "version": 1, "comment": ""})
        updated = wb.save_feedback(self.root, {**review, "version": 1, "decision": "looks-good", "comment": ""})
        self.assertEqual(updated["version"], 2)

    def test_scope_and_snapshot_tampering_are_rejected(self):
        for path in ("../secret", "/etc/passwd", "runs/../../secret", "..\\secret"):
            with self.assertRaises(ContractError):
                wb.inside(self.root, path)
        with self.assertRaises(ContractError):
            wb.artifact(self.root, "revisions", "v1", "../../session.json")
        stored, _ = wb.artifact(self.root, "revisions", "v1", "SKILL.md")
        stored.write_text("tampered")
        with self.assertRaisesRegex(ContractError, "changed after"):
            wb.artifact(self.root, "revisions", "v1", "SKILL.md")
        try:
            (self.root / "feedback").symlink_to(self.base, target_is_directory=True)
        except (OSError, NotImplementedError):
            return  # Native Windows may not grant symlink creation.
        self.finish()
        with self.assertRaisesRegex(ContractError, "symlink"):
            wb.save_feedback(self.root, {"run_id": "candidate-1", "decision": "looks-good", "comment": "", "version": 0})

    def test_native_validation_preserves_metadata_and_reports_unsupported_yaml(self):
        with patch.dict(sys.modules, {"yaml": None}):
            self.assertEqual(validate_skill(self.skill)["status"], "PASS")
            path = self.skill / "SKILL.md"
            extended = path.read_text().replace('---\nKeep', 'license: MIT\nmetadata:\n  version: "1.0"\n---\nKeep')
            path.write_text(extended)
            self.assertEqual(validate_skill(self.skill)["status"], "UNPROVEN")
            self.assertEqual(path.read_text(), extended)
        try:
            import yaml
        except ImportError:
            return
        self.assertEqual(validate_skill(self.skill)["status"], "PASS")
        path.write_text(extended + "\n[Missing](references/missing.md)\n")
        self.assertEqual(validate_skill(self.skill)["status"], "FAIL")
        path.write_text("---\nname: [broken\n---\nBody")
        self.assertEqual(validate_skill(self.skill)["status"], "FAIL")

    def test_http_auth_feedback_diff_and_artifact_contract(self):
        self.finish()
        (self.skill / "SKILL.md").write_text("A revised skill")
        wb.snapshot(self.root, "v2", self.skill, "Use feedback")
        server = wb.make_server(self.root)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(thread.join)
        self.addCleanup(server.shutdown)
        url, token = server.workbench_url.split("#")

        def request(path, data=None, headers=None):
            req = Request(url + path, data=json.dumps(data).encode() if data else None,
                          headers=headers if headers is not None else {"Authorization": "Bearer " + token})
            return urlopen(req, timeout=3)

        with request("") as response:
            self.assertIn(b"Skill workbench", response.read())
        for headers in ({}, {"Authorization": "Bearer " + token, "Origin": "https://unrelated.example"},
                        {"Authorization": "Bearer " + token, "Host": "other.example"}):
            with self.assertRaises(HTTPError) as rejected:
                request("api/state", headers=headers)
            self.assertEqual(rejected.exception.code, 403)
        with request("api/diff?before=v1&after=v2&path=SKILL.md") as response:
            self.assertIn("+A revised skill", json.load(response)["diff"])
        with request("api/artifact?kind=runs&owner=candidate-1&path=SKILL.md") as response:
            self.assertIn(b"Keep the fix", response.read())
        review = {"run_id": "candidate-1", "decision": "looks-good", "comment": "", "version": 0}
        with request("api/feedback", review) as response:
            self.assertEqual(json.load(response)["version"], 1)
        with self.assertRaises(HTTPError) as stale:
            request("api/feedback", review)
        self.assertEqual(stale.exception.code, 409)
        with self.assertRaises(HTTPError) as malformed:
            request("api/feedback", {"run_id": None})
        self.assertEqual(malformed.exception.code, 400)


if __name__ == "__main__":
    unittest.main()
