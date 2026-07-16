from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
HARNESS_PATH = REPO / "skills/dojo/scripts/dojo_harness.py"
TEMPLATE = REPO / "skills/dojo/assets/harness-template"

SPEC = importlib.util.spec_from_file_location("dojo_harness", HARNESS_PATH)
assert SPEC and SPEC.loader
HARNESS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(HARNESS)


def exact_time(value: str = "2026-07-16T12:00:00Z") -> dict[str, str]:
    return {"precision": "exact", "source": "test-host", "value": value}


def event(run_id: str, sequence: int, kind: str, data: dict | None = None) -> dict:
    return {
        "schema_version": "dojo.event/v1",
        "run_id": run_id,
        "event_id": f"event-{sequence}",
        "sequence": sequence,
        "kind": kind,
        "actor": "test-host",
        "time": exact_time(),
        "data": data or {},
    }


class HarnessRegressionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="dojo-harness-test-")
        self.capsule = Path(self.temporary.name) / "capsule"
        shutil.copytree(TEMPLATE, self.capsule)
        self.run_path = self.capsule / "run-manifest.json"
        self.package_path = self.capsule / "package-manifest.json"

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def load(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def save(self, path: Path, value: dict) -> None:
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")

    def save_events(self, rows: list[dict]) -> Path:
        path = self.capsule / "events.jsonl"
        path.write_text(
            "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows),
            encoding="utf-8",
        )
        return path

    def test_template_preflight_passes(self) -> None:
        errors, warnings = HARNESS.validate_package(self.package_path)
        self.assertEqual([], errors)
        self.assertEqual([], warnings)

    def test_runner_visible_nested_symlink_is_rejected(self) -> None:
        secret = self.capsule / "fixtures/secret.json"
        try:
            secret.symlink_to("../evaluation/contract.json")
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"symlink unavailable: {exc}")

        task = self.capsule / "task.md"
        task.write_text(
            task.read_text(encoding="utf-8").replace(
                "fixtures/context.json", "fixtures/secret.json"
            ),
            encoding="utf-8",
        )
        package = self.load(self.package_path)
        package["dependencies"][0]["requires"] = ["fixtures/secret.json"]
        self.save(self.package_path, package)

        errors, _ = HARNESS.validate_package(self.package_path)
        self.assertTrue(any("symlink is not allowed" in error for error in errors), errors)

    def test_empty_required_telemetry_is_rejected(self) -> None:
        events_path = self.save_events([])
        errors, _ = HARNESS.validate_evidence(self.run_path, events_path, None)
        self.assertIn("telemetry is required but the event stream is empty", errors)
        self.assertTrue(any("missing required event kinds" in error for error in errors), errors)

    def test_unknown_event_kind_is_rejected(self) -> None:
        run_id = self.load(self.run_path)["run_id"]
        events_path = self.save_events(
            [
                event(run_id, 1, "run.start"),
                event(run_id, 2, "custom.undeclared"),
                event(run_id, 3, "run.finish"),
            ]
        )
        errors, _ = HARNESS.validate_evidence(self.run_path, events_path, None)
        self.assertTrue(any("not declared" in error for error in errors), errors)

    def test_restricted_network_requires_declared_allowed_host_and_absolute_url(self) -> None:
        run = self.load(self.run_path)
        run["capabilities"]["network"] = {
            "mode": "restricted",
            "allowed_hosts": ["good.test"],
        }
        run["telemetry"]["event_capabilities"]["network.open"] = [
            "data.host",
            "data.result_url",
            "time",
        ]
        self.save(self.run_path, run)
        run_id = run["run_id"]
        events_path = self.save_events(
            [
                event(run_id, 1, "run.start"),
                event(
                    run_id,
                    2,
                    "network.open",
                    {
                        "host": "evil.test",
                        "request": "evil.test/source",
                        "result_url": "evil.test/source",
                        "outcome": "returned",
                    },
                ),
                event(run_id, 3, "run.finish"),
            ]
        )
        errors, _ = HARNESS.validate_evidence(self.run_path, events_path, None)
        self.assertTrue(any("outside allowlist" in error for error in errors), errors)
        self.assertTrue(any("absolute HTTP(S) URL" in error for error in errors), errors)

    def test_missing_artifact_root_is_rejected(self) -> None:
        root = self.capsule / "missing"
        manifest = self.capsule / "artifacts.json"
        self.save(
            manifest,
            {
                "schema_version": "dojo.artifacts/v1",
                "algorithm": "sha256",
                "root": root.resolve().as_posix(),
                "files": [],
            },
        )
        errors = HARNESS.validate_artifacts(root, manifest)
        self.assertTrue(any("not a directory" in error for error in errors), errors)

    def test_artifact_exclusion_and_root_tampering_are_rejected(self) -> None:
        root = self.capsule / "work"
        (root / "result.md").write_text("original\n", encoding="utf-8")
        manifest_path = self.capsule / "artifacts.json"
        manifest = HARNESS.artifact_manifest(root, manifest_path)
        manifest["excluded"] = ["result.md"]
        manifest["root"] = "/wrong/root"
        manifest["files"] = []
        self.save(manifest_path, manifest)

        errors = HARNESS.validate_artifacts(root, manifest_path)
        self.assertTrue(any("exclusions are not supported" in error for error in errors), errors)
        self.assertTrue(any("root does not match" in error for error in errors), errors)
        self.assertTrue(any("does not match final regular files" in error for error in errors), errors)

    def test_traversal_reference_is_rejected(self) -> None:
        task = self.capsule / "task.md"
        task.write_text(
            "Read `fixtures/../evaluation/contract.json` and write `work/result.md`.\n",
            encoding="utf-8",
        )
        errors, _ = HARNESS.validate_package(self.package_path)
        self.assertTrue(any("contain no '..'" in error for error in errors), errors)

    def test_http_url_with_port_is_not_treated_as_local_dependency(self) -> None:
        task = self.capsule / "task.md"
        task.write_text(
            task.read_text(encoding="utf-8")
            + "\nThe application endpoint is http://localhost:3000/api/items.\n",
            encoding="utf-8",
        )
        errors, _ = HARNESS.validate_package(self.package_path)
        self.assertEqual([], errors)

    def test_valid_trace_with_required_start_and_finish_passes(self) -> None:
        run_id = self.load(self.run_path)["run_id"]
        events_path = self.save_events(
            [
                event(run_id, 1, "run.start"),
                event(run_id, 2, "filesystem.read", {"path": "fixtures/context.json"}),
                event(run_id, 3, "filesystem.write", {"path": "work/result.md"}),
                event(run_id, 4, "run.finish"),
            ]
        )
        errors, warnings = HARNESS.validate_evidence(self.run_path, events_path, None)
        self.assertEqual([], errors)
        self.assertEqual([], warnings)

    def test_reversed_interval_is_rejected(self) -> None:
        errors: list[str] = []
        HARNESS.validate_time(
            {
                "precision": "interval",
                "source": "test-host",
                "start": "2026-07-16T12:01:00Z",
                "end": "2026-07-16T12:00:00Z",
            },
            "time",
            errors,
        )
        self.assertTrue(any("at or after" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
