# Pressure Testing

## Scenario Design

Write realistic tasks, not quizzes. Give a zero-context runner enough local
information to act without exposing the intended answer.

- Use one scenario per archetype the skill claims to handle.
- Use three to five training scenarios and one or two holdouts.
- Make holdouts differ in kind, not merely wording.
- Include a degraded dependency case when the skill relies on tools, auth,
  network access, or a particular host capability.

## Observable Criteria

Write criteria before the run. Prefer yes/no facts such as:

- Reconnaissance happened before scoped deep reading: yes/no.
- A missing dependency was detected and reported: yes/no.
- The output artifact was written to the declared location: yes/no.
- Claims were separated into observed, claimed, and inferred: yes/no.

Do not use criteria such as “the output was good” or “the agent handled the
problem appropriately.” Those are judgments, not observables.

Map every criterion to an expected baseline failure and an explicit skill
instruction. If the baseline never fails a criterion, ask whether the skill is
actually teaching it.

## Baseline Prompt

```text
You are working on the following task. Use whatever approach you think is
right.

Available context:
<self-contained scenario, environment, tools, and permissions>

Task:
<realistic user request>

Your final response is raw working data for analysis, not a user-facing
summary. Report the steps you took, the relevant commands or artifacts, and
the result.
```

Use a fresh subagent or clean session. Preserve the exact prompt and output.

## Skilled Prompt

Use the same prompt and add the installed skill path or full skill content in
the way the target host normally exposes a skill. Include only the reference
files the scenario path would naturally load.

Do not reveal the criteria, expected failure, intended fix, or prior run.

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

## Isolation Fallback

If fresh subagents are unavailable, use separate clean sessions. If neither is
possible, perform only a degraded static review and do not claim RED, pressure,
or graduation evidence.
