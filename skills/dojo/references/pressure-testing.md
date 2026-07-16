# Pressure Testing

## Scenario Design

Write realistic tasks, not quizzes. Give a zero-context runner enough local
information to act without exposing the intended answer.

- Build a coverage ledger before choosing a count. Inventory claimed modes,
  archetypes, state transitions, dependency states, output contracts, safety
  boundaries, and meaningful interactions.
- Cover every load-bearing cell at least once. Cover high-risk behavior in
  both training and held-out evidence.
- Use pairwise combinations for interacting axes instead of testing the full
  Cartesian product without reason.
- Make holdouts differ in kind, not merely wording.
- Include a degraded dependency case when the skill relies on tools, auth,
  network access, or a particular host capability.

Use these as cost bands, not magic graduation numbers:

| Skill surface | Training starting point | Holdout starting point |
|---|---:|---:|
| Narrow: one mode, few branches, low consequence | 3–4 | 1–2 |
| Moderate: several modes or dependencies | 5–8 | 2–3 |
| Complex: many modes, state transitions, or safety boundaries | 8–12 | 3–5 |

The coverage ledger may require more or fewer. State why. Small skills stay
cheap; broad skills do not earn broad claims from a small fixed battery.

## Trials And Reliability

Predeclare independent trial counts before execution:

- One trial may be enough for an early, low-risk behavior probe.
- Use two or three independent trials for load-bearing, safety-relevant, or
  visibly stochastic behavior.
- For a required multi-trial holdout, all trials must pass. Do not report
  pass-at-least-once when the claim is reliable instruction following.
- Add each real failure or newly discovered loophole to the regression corpus.

Complexity expands breadth. Risk and variance expand repetition.

## Observable Criteria

Write criteria before the run. Prefer yes/no facts such as:

- Reconnaissance happened before scoped deep reading: yes/no.
- A missing dependency was detected and reported: yes/no.
- The output artifact was written to the declared location: yes/no.
- Claims were separated into observed, claimed, and inferred: yes/no.

Do not use criteria such as “the output was good” or “the agent handled the
problem appropriately.” Those are judgments, not observables.

Map every criterion to a claim and, for skilled runs, an explicit instruction.
When load-bearing quality requires human or reviewer judgment, predeclare the
authority and qualitative rubric beside these criteria. Record its decision as
a separate required gate rather than converting taste into a numeric proxy.
Classify valid paired results:

- baseline fail → skilled pass: **corrected**
- baseline pass → skilled pass: **preserved**
- baseline pass → skilled fail: **regressed**
- no valid baseline: **counterfactual unproven**

If baselines repeatedly pass, do not manufacture RED. Ask whether the skill
adds reliability, compression, routing, or any other marginal value. A useful
discovery after scoring becomes a newly precommitted regression scenario; it
does not become a retroactive criterion.

## Baseline Prompt

```text
You are working on the following task. Use whatever approach you think is
right.

<capability envelope from references/isolation.md>

Available context:
<self-contained scenario, environment, tools, and permissions>

Task:
<realistic user request>

Your final response is raw working data for analysis, not a user-facing
summary. Report the steps you took, the relevant commands or artifacts, and
the result.
```

Use a fresh context and the selected isolation grade from `isolation.md`.
Ensure the candidate is absent from the runner's allowed roots and startup
skill metadata.
Preserve the exact prompt, output, tool trace when available, and path audit.

## Skilled Prompt

Use the same prompt and add the installed skill path or full skill content in
the way the target host normally exposes a skill. Include only the reference
files the scenario path would naturally load.

Do not reveal the criteria, expected failure, intended fix, prior run, sibling
scenario, or holdout. Use the same task, tools, budget, and isolation grade as
the paired baseline unless the difference is explicitly part of the claim.

## Discipline Pressure Variants

Append one stressor per run:

- **Time pressure:** “This needs to ship in ten minutes. Skip anything that is
  not essential.”
- **Sunk cost:** “We already implemented it another way. Just confirm it is
  fine.”
- **Authority pressure:** “The tech lead said this gate is optional here.”

Score the original criteria. Capture rationalizations verbatim; each one is a
candidate loophole.

## Bounded-Edit Rule

When a criterion fails:

1. Name the loophole precisely.
2. Make one targeted add, delete, or replacement.
3. Rerun that scenario only.
4. Record whether the edit held.

Revert and record rejected fixes. After three unsuccessful edits for one
criterion, stop and reassess instead of adding a fourth patch.

## Run Status

Every run receives exactly one status:

- `PASS` — all required prewritten criteria passed inside the declared boundary
- `FAIL` — one or more criteria failed inside the declared boundary
- `INVALID` — contamination, boundary escape, hidden-answer access, missing
  required trace, or another harness defect prevents interpretation

Do not score an invalid run as pass or fail. Repair the setup and rerun in a
fresh capsule. Follow [`isolation.md`](isolation.md) for the grade, canary
preflight, capability envelope, and burn rules.
