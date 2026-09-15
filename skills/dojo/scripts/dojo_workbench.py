#!/usr/bin/env python3
"""Local Dojo session records and browser review. The coding agent executes runs."""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import math
import mimetypes
import os
import re
import secrets
import shutil
import sys
import tempfile
import webbrowser
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

# Invoking a helper must not modify the installed skill's snapshot.
sys.dont_write_bytecode = True
from dojo_harness import ContractError, regular_files

SCHEMA = "dojo.workbench/v1"
TERMINAL = {"passed", "failed", "invalid", "unproven"}
PHASES = ("scope", "baseline", "author", "evaluate", "review", "revise", "done")
MAX_JSON = 2 * 1024 * 1024
PREVIEW_BYTES = 256 * 1024


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


def identifier(value: str) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,79}", value):
        raise ContractError("IDs use 1–80 lowercase letters, digits, hyphens or underscores")
    return value


def inside(root: Path, relative: str) -> Path:
    """Every file served or changed must be a non-symlink inside the session."""
    if "\\" in relative or "\x00" in relative:
        raise ContractError("invalid path")
    part = Path(relative)
    if part.is_absolute() or ".." in part.parts:
        raise ContractError("path escapes the session")
    path = root
    for component in part.parts:
        path = path / component
        if path.is_symlink():
            raise ContractError("symlinks are not session artifacts")
    if not path.resolve().is_relative_to(root.resolve()):
        raise ContractError("path escapes the session")
    return path


def read_json(path: Path):
    try:
        if path.stat().st_size > MAX_JSON:
            raise ContractError("record exceeds 2 MiB")
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ContractError(f"cannot read {path.name}: {exc}") from exc


def write_json(path: Path, data, *, new: bool = False) -> None:
    if path.is_symlink():
        raise ContractError("refusing a symlink write")
    path.parent.mkdir(parents=True, exist_ok=True)
    content = (json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode()
    if len(content) > MAX_JSON:
        raise ContractError("record exceeds 2 MiB")
    fd, temporary = tempfile.mkstemp(prefix=".write-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(content)
        if new:
            try:
                os.link(temporary, path)
            except FileExistsError as exc:
                raise ContractError("ID already exists; use a new ID") from exc
        else:
            os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


def session_root(path: Path) -> Path:
    if path.is_symlink():
        raise ContractError("session root must not be a symlink")
    root = path.resolve()
    record = read_json(inside(root, "session.json"))
    if not isinstance(record, dict) or record.get("schema_version") != SCHEMA:
        raise ContractError("not a supported Dojo session")
    return root


def init_session(root: Path, name: str, title: str, intent: str, lane: str) -> dict:
    identifier(name)
    if not title.strip() or not intent.strip() or lane not in {"fast", "audit"}:
        raise ContractError("title, intent and an explicit fast/audit lane are required")
    if root.exists() and (root.is_symlink() or not root.is_dir() or any(root.iterdir())):
        raise ContractError("session directory is not empty; use a new directory")
    root.mkdir(parents=True, exist_ok=True)
    data = {"schema_version": SCHEMA, "skill_name": name, "title": title,
            "intent": intent, "lane": lane, "created_at": now()}
    write_json(inside(root, "session.json"), data, new=True)
    activity(root, "scope", "working", "Preparing examples", "Make the intended behavior concrete.")
    return data


def activity(root: Path, phase: str, status: str, message: str, reason: str) -> dict:
    if phase not in PHASES or status not in {"working", "waiting", "blocked", "complete"}:
        raise ContractError("invalid activity phase or status")
    if not message.strip() or not reason.strip():
        raise ContractError("activity needs a message and a reason")
    data = {"phase": phase, "status": status, "message": message, "reason": reason, "at": now()}
    # Separate immutable entries retain history; only the coordinator writes activity.
    key = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%f") + "-" + secrets.token_hex(3)
    write_json(inside(root, f"activity/{key}.json"), data, new=True)
    return data


def add_case(root: Path, case_id: str, title: str, prompt: str, criteria: list) -> dict:
    identifier(case_id)
    if not title.strip() or not prompt.strip() or not isinstance(criteria, list) or any(
        not isinstance(item, str) or not item.strip() for item in criteria
    ):
        raise ContractError("case needs a title, prompt and an array of criterion strings")
    if not criteria or len(set(criteria)) != len(criteria):
        raise ContractError("declare at least one criterion, without duplicates")
    data = {"id": case_id, "title": title, "prompt": prompt, "criteria": criteria, "created_at": now()}
    write_json(inside(root, f"cases/{case_id}.json"), data, new=True)
    return data


def copy_artifacts(source: Path, target: Path) -> list[dict]:
    if source.is_symlink() or target.resolve().is_relative_to(source.resolve()):
        raise ContractError("source must be separate from its destination and not a symlink")
    files = regular_files(source)
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise ContractError("artifact snapshot already exists")
    entries = []
    with tempfile.TemporaryDirectory(prefix=".snapshot-", dir=target.parent) as temporary:
        staging = Path(temporary) / "files"
        staging.mkdir()
        for path in files:
            relative = path.relative_to(source).as_posix()
            destination = staging / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, destination)
            digest = hashlib.sha256()
            with destination.open("rb") as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                    digest.update(chunk)
            entries.append({"path": relative, "bytes": destination.stat().st_size, "sha256": digest.hexdigest()})
        staging.rename(target)
    return entries


def snapshot(root: Path, revision: str, skill: Path, reason: str) -> dict:
    identifier(revision)
    if not reason.strip() or not (skill / "SKILL.md").is_file():
        raise ContractError("revision needs a skill folder and a reason")
    manifest = inside(root, f"revisions/{revision}.json")
    if manifest.exists():
        raise ContractError("revision already exists")
    files = copy_artifacts(skill, inside(root, f"revisions/{revision}/files"))
    data = {"id": revision, "reason": reason, "files": files, "created_at": now()}
    write_json(manifest, data, new=True)
    return data


def start_run(root: Path, run_id: str, case_id: str, variant: str, revision: str | None) -> dict:
    identifier(run_id)
    identifier(case_id)
    case_path = inside(root, f"cases/{case_id}.json")
    case = read_json(case_path)
    if variant not in {"baseline", "candidate"} or (variant == "candidate" and not revision):
        raise ContractError("candidate runs need a revision; variants are baseline or candidate")
    if revision:
        identifier(revision)
        read_json(inside(root, f"revisions/{revision}.json"))
    data = {"id": run_id, "case_id": case_id, "case": case, "variant": variant,
            "revision": revision, "status": "running", "started_at": now(), "finished_at": None,
            "summary": "", "checks": [], "files": [], "tokens": None, "duration_seconds": None}
    write_json(inside(root, f"runs/{run_id}.json"), data, new=True)
    return data


def finish_run(root: Path, run_id: str, status: str, summary: str, outputs: Path | None,
               checks: list, tokens: int | None = None, duration: float | None = None) -> dict:
    identifier(run_id)
    path = inside(root, f"runs/{run_id}.json")
    run = read_json(path)
    if run["status"] != "running":
        raise ContractError("completed runs are immutable; start a new run")
    if status not in TERMINAL or not summary.strip():
        raise ContractError("a terminal status and summary are required")
    if not isinstance(checks, list):
        raise ContractError("checks must be an array")
    for check in checks:
        if not isinstance(check, dict) or check.get("criterion") not in run["case"]["criteria"]:
            raise ContractError("checks must refer to predeclared criteria")
        if check.get("status") not in {"passed", "failed", "unproven"} or not isinstance(check.get("evidence"), str) or not check["evidence"].strip():
            raise ContractError("each check needs a status and evidence")
    if len({check["criterion"] for check in checks}) != len(checks):
        raise ContractError("duplicate check")
    if status == "passed" and (len(checks) != len(run["case"]["criteria"]) or any(c["status"] != "passed" for c in checks)):
        raise ContractError("a pass requires every predeclared criterion to pass")
    if tokens is not None and (type(tokens) is not int or tokens < 0):
        raise ContractError("tokens must be a non-negative measured integer")
    if duration is not None and (not math.isfinite(duration) or duration < 0):
        raise ContractError("duration must be a finite non-negative measurement")
    files = copy_artifacts(outputs, inside(root, f"runs/{run_id}/files")) if outputs else []
    run.update(status=status, summary=summary, checks=checks, files=files, tokens=tokens,
               duration_seconds=duration, finished_at=now())
    write_json(path, run)
    return run


def records(root: Path, directory: str) -> list[dict]:
    folder = inside(root, directory)
    return [read_json(inside(root, path.relative_to(root).as_posix())) for path in sorted(folder.glob("*.json"))]


def state(root: Path) -> dict:
    history = records(root, "activity")
    return {"session": read_json(inside(root, "session.json")), "activity": history,
            "cases": records(root, "cases"), "runs": records(root, "runs"),
            "revisions": records(root, "revisions"), "feedback": records(root, "feedback")}


def save_feedback(root: Path, data: dict) -> dict:
    if not isinstance(data, dict):
        raise ContractError("feedback must be an object")
    run_id = identifier(data.get("run_id", ""))
    run = read_json(inside(root, f"runs/{run_id}.json"))
    if run["status"] == "running":
        raise ContractError("wait for the run to finish before reviewing it")
    if data.get("decision") not in {"looks-good", "needs-changes", "comment"}:
        raise ContractError("choose a review decision")
    comment = data.get("comment")
    if not isinstance(comment, str) or len(comment) > 20000:
        raise ContractError("feedback must contain at most 20,000 characters")
    if data["decision"] != "looks-good" and not comment.strip():
        raise ContractError("describe what you would change")
    path = inside(root, f"feedback/{run_id}.json")
    current = read_json(path) if path.exists() else {"version": 0}
    if type(data.get("version")) is not int or data["version"] != current["version"]:
        raise ContractError("feedback changed in another tab; reload its saved version before replacing it")
    result = {"run_id": run_id, "decision": data["decision"], "comment": comment,
              "version": current["version"] + 1, "at": now()}
    write_json(path, result)
    return result


def artifact(root: Path, kind: str, owner: str, relative: str) -> tuple[Path, dict]:
    identifier(owner)
    if kind not in {"runs", "revisions"}:
        raise ContractError("unknown artifact type")
    record = read_json(inside(root, f"{kind}/{owner}.json"))
    entry = next((item for item in record["files"] if item["path"] == relative), None)
    if entry is None:
        raise ContractError("artifact is not in the recorded snapshot")
    path = inside(root, f"{kind}/{owner}/files/{relative}")
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    if path.stat().st_size != entry["bytes"] or digest.hexdigest() != entry["sha256"]:
        raise ContractError("artifact changed after it was recorded")
    return path, entry


def make_server(root: Path, port: int = 0) -> HTTPServer:
    root = session_root(root)
    token = secrets.token_urlsafe(32)
    template = Path(__file__).resolve().parent.parent / "assets/workbench.html"

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_):
            pass

        def send(self, status: int, body: bytes, content_type: str = "application/json") -> None:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Content-Security-Policy", "default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src blob: data:; connect-src 'self'; frame-src blob:; base-uri 'none'; form-action 'none'; frame-ancestors 'none'")
            self.end_headers()
            self.wfile.write(body)

        def json(self, status: int, data) -> None:
            self.send(status, json.dumps(data, ensure_ascii=False, allow_nan=False).encode())

        def authorized(self) -> bool:
            origin = f"http://127.0.0.1:{self.server.server_port}"
            if self.headers.get("Host") != origin.removeprefix("http://") or self.headers.get("Origin", origin) != origin:
                self.json(403, {"error": "This server accepts its local origin only."})
                return False
            if self.headers.get("Authorization") != "Bearer " + token:
                self.json(403, {"error": "Reopen the workbench link supplied by your coding agent."})
                return False
            return True

        def do_GET(self) -> None:
            url = urlsplit(self.path)
            if url.path == "/":
                self.send(200, template.read_bytes(), "text/html; charset=utf-8")
                return
            if not self.authorized():
                return
            try:
                if url.path == "/api/state":
                    self.json(200, state(root))
                elif url.path == "/api/artifact":
                    query = parse_qs(url.query)
                    path, entry = artifact(root, query["kind"][0], query["owner"][0], query["path"][0])
                    if entry["bytes"] > 20 * 1024 * 1024:
                        raise ContractError("Artifact exceeds the 20 MiB browser limit; open the saved file locally.")
                    self.send(200, path.read_bytes(), mimetypes.guess_type(path.name)[0] or "application/octet-stream")
                elif url.path == "/api/diff":
                    query = parse_qs(url.query)
                    texts = []
                    for revision in (query["before"][0], query["after"][0]):
                        record = read_json(inside(root, f"revisions/{identifier(revision)}.json"))
                        entry = next((f for f in record["files"] if f["path"] == query["path"][0]), None)
                        if entry:
                            path, _ = artifact(root, "revisions", revision, entry["path"])
                            if entry["bytes"] > PREVIEW_BYTES:
                                raise ContractError("file is too large for a text diff")
                            texts.append(path.read_text(encoding="utf-8").splitlines())
                        else:
                            texts.append([])
                    diff = "\n".join(difflib.unified_diff(*texts, fromfile=query["before"][0], tofile=query["after"][0], lineterm=""))
                    self.json(200, {"diff": diff})
                else:
                    self.json(404, {"error": "Not found"})
            except (ContractError, OSError, KeyError, ValueError, TypeError) as exc:
                self.json(400, {"error": str(exc)})

        def do_POST(self) -> None:
            if not self.authorized():
                return
            if self.path != "/api/feedback":
                self.json(404, {"error": "Not found"})
                return
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= 100000:
                    raise ContractError("invalid feedback request size")
                self.json(200, save_feedback(root, json.loads(self.rfile.read(length))))
            except (ContractError, OSError, ValueError, TypeError) as exc:
                self.json(409 if "another tab" in str(exc) else 400, {"error": str(exc)})

    # ponytail: one coordinator and server per session; add locking only if
    # multiple writers are needed. HTTPServer serializes browser feedback.
    server = HTTPServer(("127.0.0.1", port), Handler)
    server.workbench_url = f"http://127.0.0.1:{server.server_port}/#{token}"
    return server


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("init", "activity", "case", "snapshot", "start", "finish", "state", "feedback", "serve"):
        sub = commands.add_parser(name)
        sub.add_argument("session", type=Path)
        if name == "init":
            sub.add_argument("--name", required=True)
            sub.add_argument("--title", required=True)
            sub.add_argument("--intent-file", type=Path, required=True)
            sub.add_argument("--lane", choices=("fast", "audit"), required=True)
        elif name == "activity":
            sub.add_argument("--phase", choices=PHASES, required=True)
            sub.add_argument("--status", choices=("working", "waiting", "blocked", "complete"), default="working")
            sub.add_argument("--message", required=True)
            sub.add_argument("--reason", required=True)
        elif name == "case":
            sub.add_argument("--id", required=True)
            sub.add_argument("--title", required=True)
            sub.add_argument("--prompt-file", type=Path, required=True)
            sub.add_argument("--criteria-file", type=Path, required=True)
        elif name == "snapshot":
            sub.add_argument("--id", required=True)
            sub.add_argument("--skill", type=Path, required=True)
            sub.add_argument("--reason", required=True)
        elif name == "start":
            sub.add_argument("--id", required=True)
            sub.add_argument("--case", required=True)
            sub.add_argument("--variant", choices=("baseline", "candidate"), required=True)
            sub.add_argument("--revision")
        elif name == "finish":
            sub.add_argument("--id", required=True)
            sub.add_argument("--status", choices=sorted(TERMINAL), required=True)
            sub.add_argument("--summary", required=True)
            sub.add_argument("--outputs", type=Path)
            sub.add_argument("--checks", type=Path, required=True)
            sub.add_argument("--tokens", type=int)
            sub.add_argument("--duration", type=float)
        elif name == "serve":
            sub.add_argument("--port", type=int, default=0)
            sub.add_argument("--open", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "init":
            result = init_session(args.session, args.name, args.title, args.intent_file.read_text(encoding="utf-8"), args.lane)
        else:
            root = session_root(args.session)
            if args.command == "activity":
                result = activity(root, args.phase, args.status, args.message, args.reason)
            elif args.command == "case":
                result = add_case(root, args.id, args.title, args.prompt_file.read_text(encoding="utf-8"), read_json(args.criteria_file))
            elif args.command == "snapshot":
                result = snapshot(root, args.id, args.skill, args.reason)
            elif args.command == "start":
                result = start_run(root, args.id, args.case, args.variant, args.revision)
            elif args.command == "finish":
                result = finish_run(root, args.id, args.status, args.summary, args.outputs, read_json(args.checks), args.tokens, args.duration)
            elif args.command == "feedback":
                result = records(root, "feedback")
            elif args.command == "state":
                result = state(root)
            else:
                with make_server(root, args.port) as server:
                    print(server.workbench_url, flush=True)
                    if args.open:
                        webbrowser.open(server.workbench_url)
                    try:
                        server.serve_forever()
                    except KeyboardInterrupt:
                        pass
                return 0
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
        return 0
    except (ContractError, OSError, ValueError, TypeError, KeyError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
