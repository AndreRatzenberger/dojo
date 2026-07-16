# Portable Audit Harness

## Scope

This harness is an Audit Lane supplement, not an entrance fee. Use it only
when the package has hidden evaluator material, executable dependencies,
network/process/memory receipts, generated artifact proofs, a cross-host
machine-readable claim, or an explicit portable-harness request.

Ordinary audited text runs keep the v0.2 boundary: fresh context, exact
capability envelope, unique capsule, canary, and inspected native path/tool
audit. Do not create manifests merely to make the evidence folder look busy.

The portable layer defines:

1. `dojo.run/v1` — capability envelope, isolation grade, and observable event
   fields;
2. `dojo.package/v1` — visibility, dependency, task/grader, and artifact
   contracts;
3. `dojo.event/v1` — host-observed atomic events;
4. `dojo.receipt/v1` and `dojo.artifacts/v1` — derived evidence.

The bundled validator never launches an agent. A host adapter owns launch and
native trace capture; the validator checks the portable files it receives.

## Run Manifest

Copy `assets/harness-template/` into the unique run capsule and replace every
placeholder. Paths use normalized POSIX syntax relative to `capsule_root`.
Absolute paths, backslashes, symlinks, special files, and `..` are invalid.

Required fields:

- `run_id`, `role`, `capsule_root`, and `working_directory` identify the run;
- `isolation_grade` uses Dojo's existing
  `audited_instruction_bounded` or `fresh_context_only` vocabulary;
- `capabilities.read.allow`, `harness_inputs`, and `deny` define the complete
  visible and hidden roots;
- `capabilities.write.allow` defines every writable root;
- `capabilities.network` is `disabled`, `restricted`, or `enabled`; restricted
  mode requires explicit allowed hosts;
- `capabilities.memory` is `disabled`, `ephemeral`, or `declared`;
- `telemetry.event_capabilities` declares the exact dotted fields the adapter
  can emit for each accepted event kind;
- `telemetry.required_event_kinds` names event kinds that must occur at least
  once; use `run.start` and `run.finish` for an evidence-bearing trace;
- `telemetry.receipt_event_kinds` selects events whose receipts are derived.

The task, urgency, an in-file instruction, or a claimed authority cannot
expand the manifest. Close the run and create a new identity when its
capabilities change.

## Package Preflight

`dojo.package/v1` closes the evaluation package before it reaches a runner.
Preflight checks that:

- runner-visible and evaluator-only roots exist and do not overlap;
- every path in the package is a regular file or directory, never a symlink or
  special file;
- evaluator-only roots are covered by the run deny list;
- required files and declared dependencies exist and are visible to their
  consumer;
- clean work roots contain only declared placeholders;
- selected text files do not reference hidden, missing, escaping, or malformed
  local paths;
- structured task and evaluator fields mirrored through JSON pointers match;
- every required evidence field exists in the adapter's declared telemetry;
- artifact roots exist and the external manifest sits outside them.

Declare local dependencies used by scripts, imports, validators, finalizers,
templates, schemas, and fixtures. Static reference scanning is a conservative
backstop, not a dependency resolver.

Use `contract_mirrors` for facts that task and grader must share exactly:
network mode, write roots, required output names, status vocabulary, or other
machine-readable fields. Do not ask a model to compare two prose contracts.

Run preflight before exposing a concrete holdout. A failed preflight means
`INVALID_PACKAGE`, not candidate failure. Repair it inside the custodian
boundary; if hidden material already reached the author, apply the normal burn
rule.

## Canonical Events

Each JSONL row contains:

```json
{
  "schema_version": "dojo.event/v1",
  "run_id": "candidate-h2-01",
  "event_id": "network-open-0003",
  "sequence": 3,
  "kind": "network.open",
  "actor": "runner",
  "time": {
    "precision": "exact",
    "value": "2026-07-16T14:00:00Z",
    "source": "host"
  },
  "data": {
    "host": "example.test",
    "request": "https://example.test/source",
    "result_url": "https://example.test/source",
    "outcome": "returned"
  }
}
```

Sequences are contiguous from one and event IDs are unique. Every event kind
must be declared in `event_capabilities`; adapters may add namespaced kinds
only by declaring their fields first. Batched native actions become atomic
children before receipt derivation.

Portable core kinds are `run.start`, `run.finish`, `filesystem.read`,
`filesystem.inspect`, `filesystem.write`, `filesystem.create`,
`filesystem.delete`, `process.exec`, `network.search`, `network.open`,
`network.request`, `memory.read`, and `memory.write`.

Restricted network events require `data.host`. Any supplied request or result
URL must be an absolute HTTP(S) URL whose host matches the allowlist. Search
queries may remain plain text in `data.request`; their destination still comes
from `data.host`.

Time precision is `exact`, `interval`, or `unavailable`. Intervals require
timezone-aware start/end values with end at or after start. Never assign a
later validation clock sample to an earlier event. Retain the native trace
beside canonical events so adapter normalization can be reviewed.

## Receipts And Artifacts

Receipts are generated from canonical events, not from the runner's narrative.
Every configured receipt event gets exactly one row with the same event ID,
sequence, kind, request, result URL, outcome, and time.

Generate `dojo.artifacts/v1` after the runner stops. Hash every regular file in
the declared artifact root with SHA-256 and keep the manifest outside that
root. Artifact v1 has no exclusion list: use narrower roots instead. The
validator rejects absent roots, symlinks, special files, root-identity drift,
and changed final bytes.

## Host Adapter Boundary

A host adapter must:

1. apply or accurately communicate the run manifest;
2. launch a fresh context with evaluator and sibling material unavailable;
3. capture native path/tool/process/network activity without asking the agent
   to recreate it;
4. normalize only observed atomic events and retain the native trace;
5. stop the runner before moving outputs into shared evidence storage;
6. derive receipts and artifact hashes after the run.

The adapter may be a sandbox, CI job, API client, IDE integration, shell
orchestrator, or carefully recorded manual host procedure. A valid manifest
does not prove that the boundary held. The inspected native trace remains the
authority for the Audit Lane isolation grade.

## Commands

All bundled commands use the Python standard library:

```text
python3 scripts/dojo_harness.py validate-run run-manifest.json
python3 scripts/dojo_harness.py preflight-package package-manifest.json
python3 scripts/dojo_harness.py derive-receipts \
  --run run-manifest.json --events evidence/events.jsonl \
  --output evidence/receipts.jsonl
python3 scripts/dojo_harness.py validate-evidence \
  --run run-manifest.json --events evidence/events.jsonl \
  --receipts evidence/receipts.jsonl
python3 scripts/dojo_harness.py hash-artifacts \
  --root work --output evidence/artifacts.json
python3 scripts/dojo_harness.py validate-artifacts \
  --root work --manifest evidence/artifacts.json
```

## Failure Semantics

- Invalid run manifest: do not launch.
- Invalid package preflight: `INVALID_PACKAGE`; no candidate score.
- Missing required telemetry or unknown event kind: run `INVALID`.
- Boundary-crossing event, receipt mismatch, or artifact mismatch: run
  `INVALID`.
- Adapter cannot provide evidence required by the task: campaign `UNPROVEN`.
- Candidate output fails prewritten criteria inside a valid boundary: `FAIL`.

Record validator output verbatim. A clean validator result supports the
machine contract; it never replaces the native audit or upgrades the lane.
