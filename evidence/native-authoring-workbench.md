# Native Authoring And Workbench Validation

Date: 2026-09-15. Scope: the installed authoring/review workflow and its local
tooling. These are focused development checks, not Audit Lane graduation or
a benchmark of skill-generated output quality.

## Executable Checks

```bash
python3 -m unittest discover -s tests -v
python3 tests/check_workbench_browser.py
python3 skills/dojo/scripts/dojo_harness.py validate-skill skills/dojo
python3 -S skills/dojo/scripts/dojo_harness.py validate-skill skills/dojo
```

- All 18 standard-library tests pass, including the 11 existing harness
  regressions. New checks cover the session lifecycle, frozen case criteria,
  immutable completed runs, distinct failure states, feedback conflicts,
  unknown measurements, metadata preservation, path/symlink boundaries,
  artifact tampering, and HTTP authentication/origin checks.
- The browser check passes with `agent-browser`: saved feedback reaches the
  CLI; unfinished drafts survive polling and reload; stale writes cannot
  replace newer feedback; offline recovery retains the draft; text diffs,
  keyboard focus, and 1440/390-pixel layouts work. The HTML fixture renders
  while its script and local network probe are blocked.
- The native package validates with and without site packages. A separate
  installed host skill validator also accepts the package. Tests simulate
  extended YAML without a parser and verify `UNPROVEN` without rewriting it.
- Desktop and mobile screenshots were inspected. The README image uses
  illustrative UI fixtures; its results are not model benchmark evidence.

## Installed-Package Exercises

Each initial runner received a separate copied package, a self-contained
task, exact allowed paths, and no access to other creators, global memory,
network, prior results, or evaluator criteria. Evidence grade: **fresh-context
only**, with reported paths and commands; no audited sandbox claim.

The predeclared edit exercise asked for native revision of a release-notes
skill, preservation of metadata/resources, an executed package validator,
original/revised snapshots, and an honest review-waiting state. No behavior
runs or human approval were supplied.

| Exercise | Observed result |
|---|---|
| Released package at `9c61f005` | Reported `MISSING_CONTEXT` for the absent bundled authoring/workbench capabilities. Left the skill unchanged and invented no evidence. |
| New package, same edit exercise | Executed the native helpers, preserved `license`, nested `metadata`, and the linked reference, validated the edit, and recorded original/v1 snapshots with a waiting review. Zero fabricated runs or feedback; behavioral improvement remained `UNPROVEN`. |
| Fresh creation with `--lane fast --quiet` and `python3 -S` | Created one `SKILL.md`, executed the bundled validator successfully without a YAML dependency, and returned exactly `NATIVE_PACKAGE_PASS`. No workbench or progress chatter. |
| Feedback-to-revision integration | The authoring runner consumed an explicitly synthetic, `unproven` review fixture through the bundled feedback command. It added the requested missing-input rule, validated and snapshotted v2, retained original/v1 and metadata/resources, and left human review pending. A separate file/hash readback confirmed the resulting state. |

This comparison establishes availability and use of the new workflow. It does
not establish that the resulting release-notes skill outperforms an agent
without that skill. Existing Audit Lane custody and graduation requirements
remain applicable to such a claim.

## Routing Proxy

Two independent judges received the same 142-entry active description
catalog, with its Dojo entry replaced by the candidate, and 15 predeclared
prompts. Both selected Dojo for all nine positive requests and avoided it for
all six neighboring requests. No Dojo collisions or judge disagreements.

Exact expected-owner agreement was **14/15 for each judge**: both assigned a
Python logic-bug review to the debugging skill where the predeclared owner was
`none`. That expectation was not changed after observing the result. This is
a description-routing proxy, not a live-dispatcher measurement.

## Limits

Browser execution was checked on Linux/Chromium. Native macOS/Windows and
other browsers were not exercised. Session storage assumes one coordinator
and one local server; it is not a remote or multi-user service. Token usage,
behavioral reliability, and genuine human acceptance were not measured by
these exercises. Full Audit Lane graduation remains unproven.
