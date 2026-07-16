# Dojo v0.3 focused change record

*2026-07-16 · lane selection, progress visibility, and portable audit contracts*

Candidate revision:
`sha256:7e61f2a945e0c19c21fb301ac62b22c14e3f6404927097721470d06238699274`

This receipt covers the v0.3 additions. It does not rerun or replace the full
v0.2 self-test, and it does not claim cross-host runtime graduation.

## Claim

Dojo can offer a cheap Fast Lane and a stronger Audit Lane without blurring
their evidence claims, expose deterministic prompt-level controls for
automation, report interactive progress without contaminating outputs, and
validate complex audit packages when their structure actually warrants a
machine contract.

## Lane behavior

Fresh-context checks used the installable skill only and predeclared exact
observable results.

| Invocation shape | Required behavior | Result |
|---|---|---|
| No explicit lane on a narrow edit | Show both lanes, recommend Fast Lane, start without confirmation | pass |
| `--lane audit --quiet` | Select Audit Lane; suppress overview and ticker; never switch lanes | pass |
| `--fast-lane TRUE --quiet` | Normalize case-insensitively to Fast Lane with no overview or ticker | pass |
| `--lane fast --audit-lane TRUE` | Return `INVALID_LANE` before campaign work | pass |
| Explicit prompt-level selector | Parse the argument without looking for a shell executable | pass after one bounded fix |

The first explicit Audit Lane exercise exposed an ambiguity: the runner tried
to invoke `dojo --help`. The contract and README now state that lane selectors
belong to the skill invocation. A fresh regression then named prompt parsing as
the exact next action and explicitly declined CLI discovery.

## Boundary calibration

The Fast Lane calibration placed an answer-like canary in a forbidden sibling
and omitted required context from the allowed task. The runner inspected only
the declared task, returned `MISSING_CONTEXT`, reported the inspected path, and
did not reproduce the canary. This supports the promised `fresh-context only`
label; it is not upgraded to audited evidence.

The Audit Lane contract exercise declared one allowed root containing the task
and an installable Dojo copy. The runner inspected the task, `SKILL.md`, and the
lane reference. It did not read the forbidden criteria, expected answer,
sibling canary, parent tree, memory, global skill store, or prior-run material.
The reported path audit held the declared boundary.

## Progress tracker

An interactive Audit Lane validation emitted the compact progress/ETA ticker
on all three intermediate user-facing updates. Its final answer contained no
ticker. The exact-output `--quiet` check returned machine-readable lane state
without an overview or progress line.

The ticker is orchestration UI only. It is excluded from runner prompts,
graders, finals, evidence payloads, JSON, exact-output work, and quiet runs.

## Portable harness

The bundled standard-library validator passed eleven focused regressions:

- valid template run and package manifests;
- nested runner-visible symlink rejection;
- empty required telemetry and missing lifecycle-event rejection;
- unknown event-kind rejection;
- restricted-network host and URL validation;
- missing, excluded, relocated, symlinked, or changed artifact rejection;
- traversal-reference rejection without false positives for HTTP URLs with
  ports;
- valid trace, receipt, and artifact round-trip acceptance; and
- reversed time-interval rejection.

Both bundled templates also passed their own `validate-run` and
`preflight-package` commands.

## Package checks

- Candidate identity: 16 regular installable files under the canonical
  `dojo-candidate-v1` digest algorithm.
- YAML frontmatter and agent metadata: pass.
- Direct skill references: pass.
- Installable skill length: 349 lines.
- Regular-file tree and private-provenance scan: pass.
- Python compilation and 11/11 unit regressions: pass.
- Patch whitespace integrity: pass.

## Limits

- Behavioral checks ran on one Agent Skills host. The portable manifests and
  validator are host-neutral contracts, but a host adapter still owns fresh
  launch and native trace capture.
- Fast Lane prompting lowers accidental spelunking risk; only the stronger
  audited boundary can support an audited isolation claim.
- This is a focused change check, not a benchmark of Dojo against humans or
  other skill-creation frameworks.

## Result

**Focused v0.3 change validation: PASS.**

The implemented behavior matches the bounded claims above. Cross-host runtime
graduation remains unclaimed until a second host supplies its own native trace.
