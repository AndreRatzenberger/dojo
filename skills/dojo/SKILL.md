---
name: dojo
description: 'Use when an Agent Skill needs behavioral evaluation, hardening, trigger tuning, isolation auditing, or evidence before release, or when the user explicitly asks to create a skill through Dojo. Runs coverage-scaled baseline and skilled scenarios, pressure-tests discipline skills, holds out graduation cases, checks routing collisions, and records proof under ~/.dojo. Responds to "dojo", "test this skill", "prove this skill works", "skill evals", "harden this SKILL.md", and "why is this skill triggering". Does not own ordinary first-draft skill creation unless Dojo is explicitly requested.'
---

# Dojo — Skills Earn Their Place

## Purpose

Treat every skill as a claim about future agent behavior. Make the claim earn
trust through observable evidence before release. Do not ship a skill merely
because its instructions sound convincing.

Dojo is the verification layer. Reuse an installed skill creator or the host's
normal scaffolding when useful; do not compete with it. Own evaluation,
pressure, held-out graduation, routing checks, and the evidence record. When
the user explicitly asks to build a skill through Dojo, run the full lifecycle.

For a narrow edit, use the edit-to-kata mapping below. State which kata are
run, which are skipped, and why.

## Measurability Rule

Use two kinds of pass criteria:

- **Observable process checks** — yes/no facts about what the agent did.
- **Exact-match trigger checks** — which skill the router selected.

Keep holistic output quality as explicit human or reviewer judgment. Do not
turn taste into a fake scalar. When a real task-level grader exists, use it and
record its result alongside the Dojo evidence.

Before any run, declare whether load-bearing success includes qualitative
judgment that process checks cannot decide. If so, name the human or reviewer
authority, prewrite the acceptance rubric, and blind the judge to baseline
versus candidate identity when practical. A required rejection makes the gate
`FAIL`; an unavailable required authority makes the campaign `UNPROVEN`.
Passing observable checks cannot overrule that gate. After a qualitative
`FAIL`, make one bounded fix, freeze a new candidate revision, and rerun the
same qualitative gate before opening another graduation attempt.

## Choose The Tier

| Tier | Skill shape | Required rigor |
|---|---|---|
| **Discipline** | Rules agents rationalize around | RED–GREEN–REFACTOR plus adversarial pressure variants |
| **Technique** | Multi-step orchestration | Baseline-fail plus skilled walkthrough |
| **Reference** | Facts, flags, or recipes | Correctness review plus trigger evaluation |

Every full campaign gets trigger evaluation. Only discipline skills require
time, sunk-cost, and authority-pressure variants.

When a skill mixes tiers, the highest-risk load-bearing behavior wins. Any
rule whose value depends on resisting a plausible shortcut, authority claim,
unsafe request, permission expansion, or evidence rationalization makes the
campaign **discipline** unless that behavior is split into a separate skill.
Use **technique** only when the hard part is orchestration competence rather
than temptation resistance. Use **reference** only for lookup and correctness.

For a reference-tier skill, run source-backed correctness review, trigger
evaluation, and packaging. Mark behavioral RED/GREEN comparison, pressure
variants, and held-out graduation as not applicable. If the candidate claims
an operational workflow beyond reference lookup, classify it as technique
instead of quietly expanding the reference tier. Read
`references/reference-correctness.md` for the executable review contract.

## Narrow Edit Mapping

Every Dojo edit campaign records identity, changed claims, selected kata,
package validation, and a terminal verdict. Then apply this mapping:

| Changed surface | Required kata |
|---|---|
| `name`, description, trigger phrases, or exclusions | Full trigger matrix and package validation |
| Behavioral instructions or references | Isolation preflight; affected training cases plus adjacent regressions; new held-outs when the release behavior claim changes; package validation |
| Reference facts or authoritative sources | Correctness review for every affected claim; package validation; trigger matrix only if routing text changed |
| Isolation, runner, grader, or evidence semantics | Harness preflight; affected behavioral regressions; package validation |
| Host metadata or package structure only | Package validation and clean-context smoke; trigger matrix when routing metadata changed |

A documentation-only repository edit outside the installable skill is not a
Dojo campaign. A skipped trigger or graduation kata is valid only when this
table makes it unaffected and the record states that rationale.

## Establish Isolation Before Testing

Fresh context alone is insufficient. A new runner may still spelunk through
sibling seeds, criteria, prior runs, installed skill metadata, or the candidate
itself. Choose and record the strongest available grade:

1. **Audited instruction-bounded** — a fresh context receives an exact
   capability envelope, unique run folder, canary preflight, and inspected
   path or tool audit. Clean runs may support RED, pressure, and graduation.
2. **Fresh-context only** — a new context without a verified read boundary.
   Use for exploratory feedback, not clean RED or graduation claims.
3. **Degraded local review** — static inspection in the authoring context.

Use `PASS`, `FAIL`, or `INVALID` for every behavioral run. Any access to
criteria, expected answers, sibling fixtures, prior outputs, forbidden skill
material, or other undeclared context makes the run `INVALID`, regardless of
its output score. Replace invalid evidence before graduation. Read
`references/isolation.md` before launching any behavioral runner.

## The Seven Kata

### 1. Intake

Classify the tier and whether this is a new skill or an edit. Build a coverage
ledger across claimed modes, archetypes, state transitions, dependency states,
output contracts, and safety boundaries. Select the smallest scenario set that
covers the load-bearing cells and interactions. Complexity expands scenario
breadth; risk and stochasticity expand independent trials. Hold out enough
different-in-kind scenarios to cover unseen high-risk or cross-axis behavior.

Persist the battery immediately:

```text
~/.dojo/<repo-slug>/<skill>/
  <skill>-scenarios.md
  <skill>-runs/
  <skill>-record.md
```

Require a candidate skill directory before creating the evidence identity. For
an idea-only request, choose or create the intended candidate directory first.
Resolve the repository root with
`git -C <candidate-skill-directory> rev-parse --show-toplevel`. If the candidate
is not in Git, use the explicitly declared project root containing it; if none
exists, use the candidate directory itself. Never derive identity from ambient
working directory. Record the candidate path and fallback.
Canonicalize the root by making it absolute, resolving symlinks plus `.` and
`..`, rendering separators as `/`, removing a trailing separator except for a
filesystem root, and lowercasing only a Windows drive letter. Derive
`repo-slug` from the canonical root basename by lowercasing it, replacing
non-alphanumeric runs with hyphens, and trimming edge hyphens.

Before writing, read the identity fields in any occupied slug. If they name the
same canonical root, reuse it. If they are missing or name another root, append
the first eight lowercase hex characters of SHA-256 over the UTF-8 canonical
root. If that candidate is also occupied by another or unknown root, extend the
same digest prefix four characters at a time through all 64 characters. A
mismatch at the full digest is an error: stop and never merge evidence trees.
Immediately after the title in both the scenario ledger and record, write
`Repository root:`, `Root resolution: git|declared-project|candidate-fallback`,
`Repository slug:`, and `Candidate skill path:`. The repository fields are the
collision identity; do not infer ownership from the directory name alone.

Append every test prompt verbatim as sent and every result line as received.
Record the coverage ledger, predeclared trial counts, isolation plan, training
scenarios, and only the reserved coverage cells for held-outs. Do not
materialize concrete holdout tasks in the authoring context. Read
`references/pressure-testing.md` before designing the battery and
`references/isolation.md` for the required role separation.

### 2. Baseline — RED

Bind the counterfactual to the declared claim before running it:

- New-skill or absolute skill-value claim: compare against no skill.
- Edit-improvement claim: compare against the frozen previous released version.
- Both claims: run and label both comparisons separately.

Never use a no-skill comparison to claim that an edit improved the released
version. Preserve it only as separately labeled absolute-value evidence when
that claim was predeclared; it cannot establish `corrected` or `preserved`
edit behavior. Score only the prewritten criteria and capture the exact failure
modes. Separate three claims: `corrected` means baseline fail then skilled pass;
`preserved` means both pass; `unproven` means no valid counterfactual exists. If
every valid baseline already passes, do not invent a failure or claim marginal
improvement. Reconsider whether the skill adds reliability, compression,
routing, or anything worth shipping.

Skip a new baseline only when concrete prior evidence already demonstrates the
failure. Name and preserve that evidence.

### 3. Write — GREEN

Author the smallest instructions that address the observed failures. Check
every criterion against an explicit instruction. Keep `SKILL.md` focused and
move conditional detail into directly linked `references/` files.

### 4. Pressure-Test — REFACTOR

Run the same training scenarios with the skill available. For discipline
skills, add one pressure variant at a time. On failure, make one bounded edit,
rerun only that scenario, and record whether the edit survived. Preserve failed
attempts in the rejected-fix table.

Do not add a criterion after seeing an output and score it retroactively. Turn
the discovery into a new precommitted scenario or regression case.

After three failed bounded edits for the same criterion, stop and reassess the
skill shape or criterion.

### 5. Graduation

Freeze the candidate, record its content digest as the candidate revision, and
open a new graduation-attempt identifier. Only then have a separate holdout custodian materialize
the predeclared coverage cells into concrete tasks and criteria without seeing
the candidate, training cases, or prior outputs. Run each held-out scenario for
its predeclared number of independent trials with no edits between runs. A
single required-trial failure burns the holdout: fix the skill, reserve and
materialize a new holdout, and attempt graduation again. Never reuse a burned
or exposed holdout as proof of generalization. Label graduation with its
isolation grade.

### 6. Trigger Evaluation

Start with 10–15 realistic prompts: roughly 60% positives and 40% near-miss
negatives. Expand until every declared mode and credible neighboring owner is
covered. Compare against the actual installed skill landscape when the host
exposes it. Prefer the real dispatcher; otherwise run two independent routing
judges and label them as a proxy.

Every positive must select the skill. Any negative stolen from another skill is
a collision. Read `references/trigger-evals.md` before running this kata.

### 7. Package And Record

Validate the installed skill folder against the Agent Skills format and the
target host. Smoke-invoke it from a clean context. Leak-check every curated
artifact before copying it into a repository.

End every candidate revision with exactly one verdict: `GRADUATED`,
`NOT GRADUATED`, or `UNPROVEN`, scoped to its latest graduation attempt. Use
`GRADUATED` only when every applicable gate for that revision and attempt
passes with valid evidence and the record demonstrates a bounded value claim.
Use `NOT GRADUATED` for a valid failing current gate. Use `UNPROVEN` when a
required current gate is missing, contaminated, or cannot run validly. Retain
older failures and burned attempts as history, but do not count replaced
evidence against a later revision. Known limitations may narrow the claim;
they never waive a current gate.

Keep raw runtime evidence under `~/.dojo/`. Copy a curated record or fixtures
into a repository only when the user wants checked-in proof. Read
`references/packaging.md` for the ship checklist and record template.

## Run Rules

- Use a fresh context per test run and label its actual isolation grade.
- Give every runner an exact read/write capability envelope.
- Keep criteria, expected answers, sibling fixtures, prior runs, and holdouts
  outside the runner's allowed roots.
- Keep the candidate absent from baseline allowed roots, startup context, and
  skill catalogs; any leak makes the baseline `INVALID`.
- Make every prompt self-contained; test runners do not inherit this chat.
- Write criteria before observing the result.
- Ask runners for raw steps and outputs, not a polished user summary.
- Record exact prompts, tool/file traces when available, inspected paths,
  model, host, active skill catalog, network policy, and isolation grade.
- Treat the inspected path or tool audit as the evidence that the declared
  boundary held.

## Do Not Use Dojo For

- One-line non-skill configuration or documentation edits.
- Ordinary plans, specifications, articles, or code review.
- Skills with a mature scalar grader and representative eval corpus; use that
  grader and treat Dojo only as a routing or release wrapper if needed.

## References

- [`references/isolation.md`](references/isolation.md) — read before every
  behavioral run.
- [`references/pressure-testing.md`](references/pressure-testing.md) — read for
  kata 1, 2, and 4.
- [`references/reference-correctness.md`](references/reference-correctness.md)
  — read for every reference-tier campaign.
- [`references/trigger-evals.md`](references/trigger-evals.md) — read for kata
  6.
- [`references/packaging.md`](references/packaging.md) — read for kata 7.
