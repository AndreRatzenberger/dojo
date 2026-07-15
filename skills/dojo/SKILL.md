---
name: dojo
description: 'Use when an Agent Skill needs behavioral evaluation, hardening, trigger tuning, or evidence before release, or when the user explicitly asks to create a skill through Dojo. Runs observable baseline and skilled scenarios, pressure-tests discipline skills, holds out graduation cases, checks routing collisions, and records proof under ~/.dojo. Responds to "dojo", "test this skill", "prove this skill works", "skill evals", "harden this SKILL.md", and "why is this skill triggering". Does not own ordinary first-draft skill creation unless Dojo is explicitly requested.'
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

For a narrow edit, run only the kata touched by the change. State which kata
are skipped and why.

## Measurability Rule

Use two kinds of pass criteria:

- **Observable process checks** — yes/no facts about what the agent did.
- **Exact-match trigger checks** — which skill the router selected.

Keep holistic output quality as explicit human or reviewer judgment. Do not
turn taste into a fake scalar. When a real task-level grader exists, use it and
record its result alongside the Dojo evidence.

## Choose The Tier

| Tier | Skill shape | Required rigor |
|---|---|---|
| **Discipline** | Rules agents rationalize around | RED–GREEN–REFACTOR plus adversarial pressure variants |
| **Technique** | Multi-step orchestration | Baseline-fail plus skilled walkthrough |
| **Reference** | Facts, flags, or recipes | Correctness review plus trigger evaluation |

Every tier gets trigger evaluation. Only discipline skills require time,
sunk-cost, and authority-pressure variants.

For a reference-tier skill, run source-backed correctness review, trigger
evaluation, and packaging. Mark behavioral RED/GREEN comparison, pressure
variants, and held-out graduation as not applicable. If the candidate claims
an operational workflow beyond reference lookup, classify it as technique
instead of quietly expanding the reference tier.

## Establish Isolation Before Testing

Choose and record the strongest available execution mode:

1. **Fresh subagents** — preferred. Use a new context for every run.
2. **Separate clean sessions** — acceptable when subagents are unavailable.
3. **Degraded local review** — static inspection only.

Never label a degraded local review as a baseline comparison, pressure-test,
or graduation. Record the missing isolation as a known limitation.

## The Seven Kata

### 1. Intake

Classify the tier and whether this is a new skill or an edit. Design one
realistic scenario per claimed archetype with yes/no criteria written before
any run. Hold back one or two scenarios that are never used during iteration.

Persist the battery immediately:

```text
~/.dojo/<repo-slug>/<skill>/
  <skill>-scenarios.md
  <skill>-runs/
  <skill>-record.md
```

Resolve the repository root with `git rev-parse --show-toplevel` when available;
otherwise use the current working directory and record that fallback.
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
At the top of both the scenario ledger and record, write `Repository root:`,
`Root resolution: git|cwd-fallback`, and `Repository slug:`. These fields are
the collision identity; do not infer ownership from the directory name alone.

Append every test prompt verbatim as sent and every result line as received.
Read `references/pressure-testing.md` before designing the battery.

### 2. Baseline — RED

Run training scenarios without the skill, or against the previous released
version for an edit. Score only the prewritten criteria and capture the exact
failure modes. A skill that corrects no observed failure is decoration.

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

After three failed bounded edits for the same criterion, stop and reassess the
skill shape or criterion.

### 5. Graduation

Run each held-out scenario once with no edits between holdouts. A failure burns
the holdout: fix the skill, design a new holdout, and attempt graduation again.
Never reuse a burned holdout as proof of generalization.

### 6. Trigger Evaluation

Build a matrix of 10–15 realistic prompts: roughly 60% positives and 40%
near-miss negatives. Compare against the actual installed skill landscape when
the host exposes it. Prefer the real dispatcher; otherwise run two independent
routing judges and label them as a proxy.

Every positive must select the skill. Any negative stolen from another skill is
a collision. Read `references/trigger-evals.md` before running this kata.

### 7. Package And Record

Validate the installed skill folder against the Agent Skills format and the
target host. Smoke-invoke it from a clean context. Leak-check every curated
artifact before copying it into a repository.

Keep raw runtime evidence under `~/.dojo/`. Copy a curated record or fixtures
into a repository only when the user wants checked-in proof. Read
`references/packaging.md` for the ship checklist and record template.

## Run Rules

- Use a fresh isolated context per test run.
- Make every prompt self-contained; test runners do not inherit this chat.
- Write criteria before observing the result.
- Ask runners for raw steps and outputs, not a polished user summary.
- Prevent cross-run leakage from files, prior messages, and expected answers.
- Record the model, host, and isolation mode when available.

## Do Not Use Dojo For

- One-line non-skill configuration or documentation edits.
- Ordinary plans, specifications, articles, or code review.
- Skills with a mature scalar grader and representative eval corpus; use that
  grader and treat Dojo only as a routing or release wrapper if needed.

## References

- [`references/pressure-testing.md`](references/pressure-testing.md) — read for
  kata 1, 2, and 4.
- [`references/trigger-evals.md`](references/trigger-evals.md) — read for kata
  6.
- [`references/packaging.md`](references/packaging.md) — read for kata 7.
