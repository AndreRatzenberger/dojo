#!/usr/bin/env python3
"""Portable validators for Dojo harness contracts.

This module never launches an agent. Host adapters create capsules and canonical
event streams; these commands validate the shared contracts and evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path, PurePosixPath
from typing import Any, Iterable
from urllib.parse import urlparse


RUN_SCHEMA = "dojo.run/v1"
PACKAGE_SCHEMA = "dojo.package/v1"
EVENT_SCHEMA = "dojo.event/v1"
RECEIPT_SCHEMA = "dojo.receipt/v1"
ARTIFACT_SCHEMA = "dojo.artifacts/v1"
NETWORK_MODES = {"disabled", "restricted", "enabled"}
MEMORY_MODES = {"disabled", "ephemeral", "declared"}
ISOLATION_GRADES = {"audited_instruction_bounded", "fresh_context_only"}
TIME_PRECISIONS = {"exact", "interval", "unavailable"}


class ContractError(Exception):
    pass


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ContractError(f"cannot read JSON {path}: {exc}") from exc


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise ContractError(f"cannot read JSONL {path}: {exc}") from exc
    for number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ContractError(f"invalid JSONL {path}:{number}: {exc}") from exc
        if not isinstance(row, dict):
            raise ContractError(f"JSONL row must be an object: {path}:{number}")
        rows.append(row)
    return rows


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, path)


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    os.replace(temporary, path)


def require_object(value: Any, field: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append(f"{field} must be an object")
        return {}
    return value


def require_string(value: Any, field: str, errors: list[str]) -> str:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{field} must be a non-empty string")
        return ""
    return value


def require_string_list(value: Any, field: str, errors: list[str]) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        errors.append(f"{field} must be an array of strings")
        return []
    if len(value) != len(set(value)):
        errors.append(f"{field} contains duplicates")
    return list(value)


def normalize_relative(value: str, field: str, errors: list[str], allow_dot: bool = True) -> str:
    if not value:
        errors.append(f"{field} must not be empty")
        return ""
    if "\\" in value or "\x00" in value:
        errors.append(f"{field} must use POSIX separators and contain no NUL")
        return ""
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts:
        errors.append(f"{field} must be relative and contain no '..': {value!r}")
        return ""
    normalized = str(path)
    if normalized == "." and not allow_dot:
        errors.append(f"{field} may not be '.'")
    if value != normalized:
        errors.append(f"{field} is not normalized: {value!r}; expected {normalized!r}")
    return normalized


def path_within(path: str, root: str) -> bool:
    if root == ".":
        return True
    return path == root or path.startswith(root + "/")


def paths_overlap(left: str, right: str) -> bool:
    return path_within(left, right) or path_within(right, left)


def under_any(path: str, roots: Iterable[str]) -> bool:
    return any(path_within(path, root) for root in roots)


def resolve_inside(root: Path, relative: str) -> Path:
    base = root.resolve()
    target = (base / Path(*PurePosixPath(relative).parts)).resolve(strict=False)
    try:
        target.relative_to(base)
    except ValueError as exc:
        raise ContractError(f"path escapes package root: {relative}") from exc
    return target


def reject_symlink_chain(root: Path, relative: str, errors: list[str]) -> None:
    cursor = root.resolve()
    for part in PurePosixPath(relative).parts:
        cursor = cursor / part
        if cursor.is_symlink():
            errors.append(f"symlink is not allowed in harness package: {relative}")
            return


def parse_iso(value: Any, field: str, errors: list[str]) -> datetime | None:
    if not isinstance(value, str):
        errors.append(f"{field} must be an ISO 8601 string")
        return None
    candidate = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(candidate)
    except ValueError:
        errors.append(f"{field} is not a parseable ISO 8601 timestamp: {value!r}")
        return None
    if parsed.tzinfo is None:
        errors.append(f"{field} must include a timezone offset: {value!r}")
        return None
    return parsed


def reject_unsafe_tree(root: Path, errors: list[str]) -> None:
    if not root.is_dir():
        errors.append(f"package root is not a directory: {root}")
        return
    for path in sorted(root.rglob("*"), key=lambda item: item.as_posix().encode("utf-8")):
        rel = path.relative_to(root).as_posix()
        if path.is_symlink():
            errors.append(f"symlink is not allowed in harness package: {rel}")
        elif not path.is_dir() and not path.is_file():
            errors.append(f"special file is not allowed in harness package: {rel}")


def get_pointer(document: Any, pointer: str) -> Any:
    if pointer == "":
        return document
    if not pointer.startswith("/"):
        raise ContractError(f"JSON pointer must start with '/': {pointer}")
    value = document
    for raw in pointer[1:].split("/"):
        token = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(value, dict) and token in value:
            value = value[token]
        elif isinstance(value, list) and token.isdigit() and int(token) < len(value):
            value = value[int(token)]
        else:
            raise ContractError(f"JSON pointer does not resolve: {pointer}")
    return value


def get_dotted(document: Any, dotted: str) -> Any:
    value = document
    for token in dotted.split("."):
        if not isinstance(value, dict) or token not in value:
            raise KeyError(dotted)
        value = value[token]
    return value


def validate_run_document(document: Any) -> tuple[dict[str, Any], list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    run = require_object(document, "run manifest", errors)
    if run.get("schema_version") != RUN_SCHEMA:
        errors.append(f"schema_version must be {RUN_SCHEMA!r}")
    require_string(run.get("run_id"), "run_id", errors)
    require_string(run.get("role"), "role", errors)
    if run.get("isolation_grade") not in ISOLATION_GRADES:
        errors.append(f"isolation_grade must be one of {sorted(ISOLATION_GRADES)}")
    capsule_root = normalize_relative(
        require_string(run.get("capsule_root"), "capsule_root", errors),
        "capsule_root",
        errors,
    )
    working = normalize_relative(
        require_string(run.get("working_directory"), "working_directory", errors),
        "working_directory",
        errors,
    )
    if capsule_root and working and not path_within(working, capsule_root):
        errors.append("working_directory must be inside capsule_root")

    capabilities = require_object(run.get("capabilities"), "capabilities", errors)
    read = require_object(capabilities.get("read"), "capabilities.read", errors)
    write = require_object(capabilities.get("write"), "capabilities.write", errors)
    read_allow = require_string_list(read.get("allow"), "capabilities.read.allow", errors)
    harness_inputs = require_string_list(
        read.get("harness_inputs", []), "capabilities.read.harness_inputs", errors
    )
    deny = require_string_list(read.get("deny", []), "capabilities.read.deny", errors)
    write_allow = require_string_list(write.get("allow"), "capabilities.write.allow", errors)
    for field, values in (
        ("capabilities.read.allow", read_allow),
        ("capabilities.read.harness_inputs", harness_inputs),
        ("capabilities.read.deny", deny),
        ("capabilities.write.allow", write_allow),
    ):
        for index, value in enumerate(values):
            normalize_relative(value, f"{field}[{index}]", errors)
    for allowed in read_allow + harness_inputs:
        for forbidden in deny:
            if paths_overlap(allowed, forbidden):
                errors.append(f"read authorization overlaps deny root: {allowed!r} vs {forbidden!r}")
    for allowed in write_allow:
        for forbidden in deny:
            if paths_overlap(allowed, forbidden):
                errors.append(f"write authorization overlaps deny root: {allowed!r} vs {forbidden!r}")

    network = require_object(capabilities.get("network"), "capabilities.network", errors)
    network_mode = network.get("mode")
    if network_mode not in NETWORK_MODES:
        errors.append(f"capabilities.network.mode must be one of {sorted(NETWORK_MODES)}")
    hosts = require_string_list(network.get("allowed_hosts", []), "network.allowed_hosts", errors)
    for index, host in enumerate(hosts):
        if not normalize_network_host(host):
            errors.append(f"network.allowed_hosts[{index}] is not a plain hostname: {host!r}")
    if network_mode == "disabled" and hosts:
        errors.append("disabled network may not declare allowed_hosts")
    if network_mode == "restricted" and not hosts:
        errors.append("restricted network requires allowed_hosts")
    if capabilities.get("memory") not in MEMORY_MODES:
        errors.append(f"capabilities.memory must be one of {sorted(MEMORY_MODES)}")

    telemetry = require_object(run.get("telemetry"), "telemetry", errors)
    normalize_relative(
        require_string(telemetry.get("events_path"), "telemetry.events_path", errors),
        "telemetry.events_path",
        errors,
    )
    if not isinstance(telemetry.get("required"), bool):
        errors.append("telemetry.required must be boolean")
    event_capabilities = require_object(
        telemetry.get("event_capabilities"), "telemetry.event_capabilities", errors
    )
    for kind, fields in event_capabilities.items():
        require_string(kind, f"event capability kind {kind!r}", errors)
        require_string_list(fields, f"telemetry.event_capabilities.{kind}", errors)
    receipt_kinds = require_string_list(
        telemetry.get("receipt_event_kinds", []), "telemetry.receipt_event_kinds", errors
    )
    required_kinds = require_string_list(
        telemetry.get("required_event_kinds", []), "telemetry.required_event_kinds", errors
    )
    for kind in receipt_kinds + required_kinds:
        if kind not in event_capabilities:
            errors.append(f"required event kind lacks declared telemetry capability: {kind}")
    if run.get("isolation_grade") == "audited_instruction_bounded":
        if telemetry.get("required") is not True:
            errors.append("audited_instruction_bounded requires telemetry.required=true")
        missing_lifecycle = sorted({"run.start", "run.finish"} - set(required_kinds))
        if missing_lifecycle:
            errors.append(f"audited_instruction_bounded requires lifecycle events: {missing_lifecycle}")
    return run, errors, warnings


def validate_run_file(path: Path) -> tuple[dict[str, Any], list[str], list[str]]:
    return validate_run_document(load_json(path))


def local_reference_tokens(text: str) -> set[str]:
    tokens: set[str] = set()
    text = re.sub(r"[A-Za-z][A-Za-z0-9+.-]*://\S+", "", text)
    pattern = re.compile(r"(?<!://)(?<![A-Za-z0-9_.-])((?:\.?\.?/)?[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)+)")
    for match in pattern.finditer(text):
        token = match.group(1).rstrip(".,;:)]}'\"`")
        if "://" not in token:
            tokens.add(token)
    return tokens


def validate_package(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    package = require_object(load_json(path), "package manifest", errors)
    if package.get("schema_version") != PACKAGE_SCHEMA:
        errors.append(f"schema_version must be {PACKAGE_SCHEMA!r}")
    require_string(package.get("package_id"), "package_id", errors)
    package_root_rel = normalize_relative(
        require_string(package.get("package_root"), "package_root", errors),
        "package_root",
        errors,
    )
    package_root = resolve_inside(path.parent, package_root_rel or ".")
    reject_unsafe_tree(package_root, errors)
    run_manifest_rel = normalize_relative(
        require_string(package.get("run_manifest"), "run_manifest", errors),
        "run_manifest",
        errors,
        allow_dot=False,
    )
    run_manifest_path = resolve_inside(package_root, run_manifest_rel) if run_manifest_rel else package_root
    run: dict[str, Any] = {}
    if not run_manifest_path.is_file():
        errors.append(f"run_manifest does not exist: {run_manifest_rel}")
    else:
        run, run_errors, run_warnings = validate_run_file(run_manifest_path)
        errors.extend(f"run manifest: {item}" for item in run_errors)
        warnings.extend(f"run manifest: {item}" for item in run_warnings)

    runner_visible = require_string_list(package.get("runner_visible"), "runner_visible", errors)
    evaluator_only = require_string_list(package.get("evaluator_only"), "evaluator_only", errors)
    required_files = require_string_list(package.get("required_files"), "required_files", errors)
    for field, values in (
        ("runner_visible", runner_visible),
        ("evaluator_only", evaluator_only),
        ("required_files", required_files),
    ):
        for index, value in enumerate(values):
            normalized = normalize_relative(value, f"{field}[{index}]", errors, allow_dot=False)
            if not normalized:
                continue
            reject_symlink_chain(package_root, normalized, errors)
            target = resolve_inside(package_root, normalized)
            if not target.exists():
                errors.append(f"{field}[{index}] does not exist: {value}")
            elif field == "required_files" and not target.is_file():
                errors.append(f"required_files[{index}] is not a regular file: {value}")
    for visible in runner_visible:
        for hidden in evaluator_only:
            if paths_overlap(visible, hidden):
                errors.append(f"runner-visible and evaluator-only paths overlap: {visible!r} vs {hidden!r}")

    if run:
        read = run.get("capabilities", {}).get("read", {})
        write = run.get("capabilities", {}).get("write", {})
        deny = read.get("deny", [])
        for hidden in evaluator_only:
            if not under_any(hidden, deny):
                errors.append(f"evaluator-only path is not covered by run deny roots: {hidden}")
        for writable in write.get("allow", []):
            if any(paths_overlap(writable, hidden) for hidden in evaluator_only):
                errors.append(f"write root overlaps evaluator-only material: {writable}")

    clean_directories = package.get("clean_directories", [])
    if not isinstance(clean_directories, list):
        errors.append("clean_directories must be an array")
        clean_directories = []
    for index, entry in enumerate(clean_directories):
        item = require_object(entry, f"clean_directories[{index}]", errors)
        rel = normalize_relative(
            require_string(item.get("path"), f"clean_directories[{index}].path", errors),
            f"clean_directories[{index}].path",
            errors,
            allow_dot=False,
        )
        allowed = set(require_string_list(item.get("allow", []), f"clean_directories[{index}].allow", errors))
        target = resolve_inside(package_root, rel) if rel else package_root
        if not target.is_dir():
            errors.append(f"clean directory does not exist: {rel}")
        else:
            unexpected = sorted(child.name for child in target.iterdir() if child.name not in allowed)
            if unexpected:
                errors.append(f"clean directory is not clean: {rel}: {unexpected}")

    dependencies = package.get("dependencies", [])
    if not isinstance(dependencies, list):
        errors.append("dependencies must be an array")
        dependencies = []
    for index, entry in enumerate(dependencies):
        item = require_object(entry, f"dependencies[{index}]", errors)
        consumer = normalize_relative(
            require_string(item.get("consumer"), f"dependencies[{index}].consumer", errors),
            f"dependencies[{index}].consumer",
            errors,
            allow_dot=False,
        )
        requires = require_string_list(item.get("requires"), f"dependencies[{index}].requires", errors)
        audience = item.get("audience")
        if audience not in {"runner", "evaluator"}:
            errors.append(f"dependencies[{index}].audience must be runner or evaluator")
        for rel in [consumer] + requires:
            normalized = normalize_relative(rel, f"dependencies[{index}] path", errors, allow_dot=False)
            if normalized and not resolve_inside(package_root, normalized).exists():
                errors.append(f"declared dependency does not exist: {normalized}")
        expected_roots = runner_visible if audience == "runner" else evaluator_only
        for rel in [consumer] + requires:
            if rel and not under_any(rel, expected_roots):
                errors.append(f"{audience} dependency is outside its visibility roots: {rel}")

    scan_files = require_string_list(package.get("static_reference_scan", []), "static_reference_scan", errors)
    write_roots = run.get("capabilities", {}).get("write", {}).get("allow", []) if run else []
    for index, rel in enumerate(scan_files):
        normalized = normalize_relative(rel, f"static_reference_scan[{index}]", errors, allow_dot=False)
        target = resolve_inside(package_root, normalized) if normalized else package_root
        if not target.is_file():
            errors.append(f"static reference scan target is not a file: {rel}")
            continue
        try:
            data = target.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"cannot scan text references in {rel}: {exc}")
            continue
        for token in sorted(local_reference_tokens(data)):
            token_errors: list[str] = []
            token_norm = normalize_relative(token, f"local reference in {rel}", token_errors, allow_dot=False)
            if token_errors:
                errors.extend(token_errors)
                continue
            if not token_norm:
                continue
            if token.startswith(("./", "../")):
                token_errors = []
                token_norm = normalize_relative(
                    str(PurePosixPath(rel).parent / PurePosixPath(token)),
                    f"local reference in {rel}",
                    token_errors,
                    allow_dot=False,
                )
                if token_errors:
                    errors.extend(token_errors)
                    continue
            candidate = resolve_inside(package_root, token_norm)
            if under_any(token_norm, evaluator_only):
                errors.append(f"runner-visible file {rel} references evaluator-only path: {token_norm}")
            elif not candidate.exists() and not under_any(token_norm, write_roots):
                errors.append(f"runner-visible file {rel} references missing local path: {token_norm}")

    mirrors = package.get("contract_mirrors", [])
    if not isinstance(mirrors, list):
        errors.append("contract_mirrors must be an array")
        mirrors = []
    loaded: dict[str, Any] = {}
    for index, entry in enumerate(mirrors):
        item = require_object(entry, f"contract_mirrors[{index}]", errors)
        sides: list[Any] = []
        for side_name in ("left", "right"):
            side = require_object(item.get(side_name), f"contract_mirrors[{index}].{side_name}", errors)
            rel = normalize_relative(
                require_string(side.get("file"), f"contract_mirrors[{index}].{side_name}.file", errors),
                f"contract_mirrors[{index}].{side_name}.file",
                errors,
                allow_dot=False,
            )
            pointer = side.get("pointer")
            if not isinstance(pointer, str):
                errors.append(f"contract_mirrors[{index}].{side_name}.pointer must be a string")
                continue
            try:
                if rel not in loaded:
                    loaded[rel] = load_json(resolve_inside(package_root, rel))
                sides.append(get_pointer(loaded[rel], pointer))
            except ContractError as exc:
                errors.append(str(exc))
        if len(sides) == 2 and sides[0] != sides[1]:
            errors.append(f"contract mirror mismatch at index {index}: {sides[0]!r} != {sides[1]!r}")

    requirements = package.get("evidence_requirements", [])
    if not isinstance(requirements, list):
        errors.append("evidence_requirements must be an array")
        requirements = []
    capabilities = run.get("telemetry", {}).get("event_capabilities", {}) if run else {}
    for index, entry in enumerate(requirements):
        item = require_object(entry, f"evidence_requirements[{index}]", errors)
        kind = require_string(item.get("event_kind"), f"evidence_requirements[{index}].event_kind", errors)
        fields = require_string_list(item.get("fields"), f"evidence_requirements[{index}].fields", errors)
        if kind and kind not in capabilities:
            errors.append(f"required evidence event kind is not observable: {kind}")
        available = set(capabilities.get(kind, []))
        for field in fields:
            if field not in available:
                errors.append(f"unobservable required evidence field for {kind}: {field}")

    artifact_policy = require_object(package.get("artifact_policy"), "artifact_policy", errors)
    roots = require_string_list(artifact_policy.get("roots"), "artifact_policy.roots", errors)
    manifest_path = normalize_relative(
        require_string(artifact_policy.get("manifest_path"), "artifact_policy.manifest_path", errors),
        "artifact_policy.manifest_path",
        errors,
        allow_dot=False,
    )
    if artifact_policy.get("algorithm") != "sha256":
        errors.append("artifact_policy.algorithm must be sha256")
    for root in roots:
        normalized_root = normalize_relative(root, "artifact_policy root", errors, allow_dot=False)
        if normalized_root and not resolve_inside(package_root, normalized_root).is_dir():
            errors.append(f"artifact root is not a directory: {normalized_root}")
        if manifest_path and path_within(manifest_path, root):
            errors.append("artifact manifest must be outside every hashed artifact root")
    return errors, warnings


def validate_time(value: Any, field: str, errors: list[str]) -> None:
    time = require_object(value, field, errors)
    precision = time.get("precision")
    if precision not in TIME_PRECISIONS:
        errors.append(f"{field}.precision must be one of {sorted(TIME_PRECISIONS)}")
        return
    require_string(time.get("source"), f"{field}.source", errors)
    if precision == "exact":
        parse_iso(time.get("value"), f"{field}.value", errors)
    elif precision == "interval":
        start = parse_iso(time.get("start"), f"{field}.start", errors)
        end = parse_iso(time.get("end"), f"{field}.end", errors)
        if start is not None and end is not None and end < start:
            errors.append(f"{field}.end must be at or after {field}.start")
    elif precision == "unavailable" and time.get("value") is not None:
        errors.append(f"{field}.value must be null when precision is unavailable")


def normalize_network_host(value: Any) -> str:
    if not isinstance(value, str) or not value.strip():
        return ""
    candidate = value.strip().lower().rstrip(".")
    if "://" in candidate or "/" in candidate or "@" in candidate:
        return ""
    return candidate


def allowed_network_host(value: Any, allowed_hosts: list[str]) -> bool:
    host = normalize_network_host(value)
    allowed = [normalize_network_host(item) for item in allowed_hosts]
    return bool(host) and any(host == item or host.endswith("." + item) for item in allowed if item)


def allowed_network_url(value: Any, allowed_hosts: list[str]) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        return False
    return allowed_network_host(parsed.hostname, allowed_hosts)


def validate_evidence(
    run_path: Path, events_path: Path, receipts_path: Path | None
) -> tuple[list[str], list[str]]:
    run, errors, warnings = validate_run_file(run_path)
    events = load_jsonl(events_path)
    run_id = run.get("run_id")
    capabilities = run.get("capabilities", {})
    read = capabilities.get("read", {})
    write = capabilities.get("write", {})
    read_roots = read.get("allow", []) + read.get("harness_inputs", [])
    deny_roots = read.get("deny", [])
    write_roots = write.get("allow", [])
    network = capabilities.get("network", {})
    telemetry = run.get("telemetry", {})
    event_capabilities = telemetry.get("event_capabilities", {})
    if telemetry.get("required") and not events:
        errors.append("telemetry is required but the event stream is empty")
    capsule_root = resolve_inside(run_path.parent, run.get("capsule_root", "."))
    seen_ids: set[str] = set()
    sequences: list[int] = []
    by_id: dict[str, dict[str, Any]] = {}
    for index, event in enumerate(events):
        prefix = f"event[{index}]"
        if event.get("schema_version") != EVENT_SCHEMA:
            errors.append(f"{prefix}.schema_version must be {EVENT_SCHEMA!r}")
        if event.get("run_id") != run_id:
            errors.append(f"{prefix}.run_id does not match run manifest")
        event_id = require_string(event.get("event_id"), f"{prefix}.event_id", errors)
        if event_id in seen_ids:
            errors.append(f"duplicate event_id: {event_id}")
        seen_ids.add(event_id)
        by_id[event_id] = event
        sequence = event.get("sequence")
        if not isinstance(sequence, int) or sequence < 1:
            errors.append(f"{prefix}.sequence must be a positive integer")
        else:
            sequences.append(sequence)
        kind = require_string(event.get("kind"), f"{prefix}.kind", errors)
        if kind and kind not in event_capabilities:
            errors.append(f"{prefix}.kind is not declared in telemetry.event_capabilities: {kind}")
        require_string(event.get("actor"), f"{prefix}.actor", errors)
        validate_time(event.get("time"), f"{prefix}.time", errors)
        data = require_object(event.get("data"), f"{prefix}.data", errors)
        for field in event_capabilities.get(kind, []):
            try:
                get_dotted(event, field)
            except KeyError:
                errors.append(f"{prefix} lacks adapter-promised field {field!r} for {kind}")
        if kind == "filesystem.read" or kind.startswith("filesystem.inspect"):
            rel = normalize_relative(str(data.get("path", "")), f"{prefix}.data.path", errors)
            if rel:
                reject_symlink_chain(capsule_root, rel, errors)
            if rel and (under_any(rel, deny_roots) or not under_any(rel, read_roots)):
                errors.append(f"read event outside capability envelope: {rel}")
        elif kind in {"filesystem.write", "filesystem.create", "filesystem.delete"}:
            rel = normalize_relative(str(data.get("path", "")), f"{prefix}.data.path", errors)
            if rel:
                reject_symlink_chain(capsule_root, rel, errors)
            if rel and (under_any(rel, deny_roots) or not under_any(rel, write_roots)):
                errors.append(f"write event outside capability envelope: {rel}")
        elif kind == "process.exec":
            cwd = normalize_relative(str(data.get("cwd", "")), f"{prefix}.data.cwd", errors)
            if cwd and not path_within(cwd, run.get("capsule_root", ".")):
                errors.append(f"process cwd outside capsule root: {cwd}")
        elif kind.startswith("network."):
            mode = network.get("mode")
            if mode == "disabled":
                errors.append(f"network event occurred while network is disabled: {event_id}")
            host = data.get("host")
            if not normalize_network_host(host):
                errors.append(f"network event lacks a valid data.host: {host!r}")
            if mode == "restricted" and not allowed_network_host(host, network.get("allowed_hosts", [])):
                errors.append(f"network event uses host outside allowlist: {host!r}")
            for key in ("request", "result_url"):
                value = data.get(key)
                if isinstance(value, str) and "://" in value:
                    allowed = network.get("allowed_hosts", []) if mode == "restricted" else [urlparse(value).hostname or ""]
                    if not allowed_network_url(value, allowed):
                        errors.append(f"network event has an invalid or disallowed {key}: {value!r}")
                elif key == "result_url" and value is not None:
                    errors.append(f"network event result_url must be an absolute HTTP(S) URL: {value!r}")
        elif kind.startswith("memory.") and capabilities.get("memory") == "disabled":
            errors.append(f"memory event occurred while memory is disabled: {event_id}")
    if sequences and sequences != list(range(1, len(sequences) + 1)):
        errors.append("event sequences must be contiguous and ordered from 1")

    seen_kinds = {event.get("kind") for event in events}
    missing_required_kinds = sorted(set(telemetry.get("required_event_kinds", [])) - seen_kinds)
    if missing_required_kinds:
        errors.append(f"missing required event kinds: {missing_required_kinds}")

    required_kinds = set(run.get("telemetry", {}).get("receipt_event_kinds", []))
    if required_kinds and receipts_path is None:
        errors.append("receipts are required by the run manifest but no receipt file was supplied")
    if receipts_path is not None:
        receipts = load_jsonl(receipts_path)
        receipt_event_ids: set[str] = set()
        receipt_ids: set[str] = set()
        for index, receipt in enumerate(receipts):
            prefix = f"receipt[{index}]"
            if receipt.get("schema_version") != RECEIPT_SCHEMA:
                errors.append(f"{prefix}.schema_version must be {RECEIPT_SCHEMA!r}")
            if receipt.get("run_id") != run_id:
                errors.append(f"{prefix}.run_id does not match run manifest")
            receipt_id = require_string(receipt.get("receipt_id"), f"{prefix}.receipt_id", errors)
            if receipt_id in receipt_ids:
                errors.append(f"duplicate receipt_id: {receipt_id}")
            receipt_ids.add(receipt_id)
            event_id = require_string(receipt.get("event_id"), f"{prefix}.event_id", errors)
            if event_id in receipt_event_ids:
                errors.append(f"multiple receipts reference one event: {event_id}")
            receipt_event_ids.add(event_id)
            if event_id not in by_id:
                errors.append(f"receipt references unknown event: {event_id}")
                continue
            event = by_id[event_id]
            if receipt.get("kind") != event.get("kind"):
                errors.append(f"receipt kind differs from event {event_id}")
            if receipt.get("sequence") != event.get("sequence"):
                errors.append(f"receipt sequence differs from event {event_id}")
            for key in ("request", "result_url", "outcome"):
                if receipt.get(key) != event.get("data", {}).get(key):
                    errors.append(f"receipt {key} differs from event {event_id}")
            if receipt.get("time") != event.get("time"):
                errors.append(f"receipt time differs from event {event_id}")
        required_ids = {
            event.get("event_id")
            for event in events
            if event.get("kind") in required_kinds
            and isinstance(event.get("event_id"), str)
            and event.get("event_id")
        }
        missing = sorted(required_ids - receipt_event_ids)
        extra = sorted(receipt_event_ids - required_ids)
        if missing:
            errors.append(f"missing receipts for required events: {missing}")
        if extra:
            errors.append(f"receipts exist for non-required events: {extra}")
    return errors, warnings


def derive_receipts(run_path: Path, events_path: Path, output: Path) -> None:
    run, errors, _ = validate_run_file(run_path)
    if errors:
        raise ContractError("invalid run manifest: " + "; ".join(errors))
    kinds = set(run.get("telemetry", {}).get("receipt_event_kinds", []))
    rows: list[dict[str, Any]] = []
    for event in load_jsonl(events_path):
        if event.get("kind") not in kinds:
            continue
        data = event.get("data", {})
        rows.append(
            {
                "schema_version": RECEIPT_SCHEMA,
                "run_id": event.get("run_id"),
                "receipt_id": f"receipt:{event.get('event_id')}",
                "event_id": event.get("event_id"),
                "sequence": event.get("sequence"),
                "kind": event.get("kind"),
                "request": data.get("request"),
                "result_url": data.get("result_url"),
                "outcome": data.get("outcome"),
                "time": event.get("time"),
            }
        )
    write_jsonl(output, rows)


def regular_files(root: Path) -> list[Path]:
    if not root.is_dir():
        raise ContractError(f"artifact root is not a directory: {root}")
    files: list[Path] = []
    for path in sorted(root.rglob("*"), key=lambda item: item.relative_to(root).as_posix().encode("utf-8")):
        rel = path.relative_to(root).as_posix()
        if path.is_symlink():
            raise ContractError(f"symlink is not allowed in artifact root: {rel}")
        if path.is_dir():
            continue
        if not path.is_file():
            raise ContractError(f"special file is not allowed in artifact root: {rel}")
        files.append(path)
    return files


def artifact_manifest(root: Path, output: Path) -> dict[str, Any]:
    root_abs = root.resolve()
    if not root_abs.is_dir():
        raise ContractError(f"artifact root is not a directory: {root}")
    output_abs = output.resolve(strict=False)
    try:
        output_abs.relative_to(root_abs)
    except ValueError:
        pass
    else:
        raise ContractError("artifact manifest output must be outside the hashed artifact root")
    entries = []
    for path in regular_files(root_abs):
        content = path.read_bytes()
        entries.append(
            {
                "path": path.relative_to(root_abs).as_posix(),
                "bytes": len(content),
                "sha256": hashlib.sha256(content).hexdigest(),
            }
        )
    return {
        "schema_version": ARTIFACT_SCHEMA,
        "algorithm": "sha256",
        "root": root_abs.as_posix(),
        "files": entries,
    }


def validate_artifacts(root: Path, manifest_path: Path) -> list[str]:
    errors: list[str] = []
    manifest = require_object(load_json(manifest_path), "artifact manifest", errors)
    if manifest.get("schema_version") != ARTIFACT_SCHEMA:
        errors.append(f"artifact manifest schema_version must be {ARTIFACT_SCHEMA!r}")
    if manifest.get("algorithm") != "sha256":
        errors.append("artifact manifest algorithm must be sha256")
    if "excluded" in manifest:
        errors.append("artifact manifest exclusions are not supported; use a narrower root")
    try:
        expected = artifact_manifest(root, manifest_path)
    except ContractError as exc:
        errors.append(str(exc))
        return errors
    if manifest.get("root") != expected.get("root"):
        errors.append("artifact manifest root does not match the validated root")
    if manifest.get("files") != expected.get("files"):
        errors.append("artifact manifest does not match final regular files")
    return errors


def emit_result(errors: list[str], warnings: list[str] | None = None) -> int:
    warnings = warnings or []
    status = "PASS" if not errors else "FAIL"
    print(json.dumps({"status": status, "errors": errors, "warnings": warnings}, indent=2))
    return 0 if not errors else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("validate-run", help="Validate a dojo.run/v1 manifest.")
    run.add_argument("manifest", type=Path)
    package = sub.add_parser("preflight-package", help="Preflight a dojo.package/v1 package.")
    package.add_argument("manifest", type=Path)
    evidence = sub.add_parser("validate-evidence", help="Validate canonical events and receipts.")
    evidence.add_argument("--run", required=True, type=Path)
    evidence.add_argument("--events", required=True, type=Path)
    evidence.add_argument("--receipts", type=Path)
    derive = sub.add_parser("derive-receipts", help="Generate receipts from canonical events.")
    derive.add_argument("--run", required=True, type=Path)
    derive.add_argument("--events", required=True, type=Path)
    derive.add_argument("--output", required=True, type=Path)
    snapshot = sub.add_parser("hash-artifacts", help="Write an external final-byte artifact manifest.")
    snapshot.add_argument("--root", required=True, type=Path)
    snapshot.add_argument("--output", required=True, type=Path)
    verify = sub.add_parser("validate-artifacts", help="Validate an artifact manifest.")
    verify.add_argument("--root", required=True, type=Path)
    verify.add_argument("--manifest", required=True, type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "validate-run":
            _, errors, warnings = validate_run_file(args.manifest)
            return emit_result(errors, warnings)
        if args.command == "preflight-package":
            errors, warnings = validate_package(args.manifest)
            return emit_result(errors, warnings)
        if args.command == "validate-evidence":
            errors, warnings = validate_evidence(args.run, args.events, args.receipts)
            return emit_result(errors, warnings)
        if args.command == "derive-receipts":
            derive_receipts(args.run, args.events, args.output)
            return emit_result([])
        if args.command == "hash-artifacts":
            manifest = artifact_manifest(args.root, args.output)
            write_json(args.output, manifest)
            return emit_result([])
        if args.command == "validate-artifacts":
            return emit_result(validate_artifacts(args.root, args.manifest))
    except ContractError as exc:
        return emit_result([str(exc)])
    return emit_result([f"unknown command: {args.command}"])


if __name__ == "__main__":
    sys.exit(main())
