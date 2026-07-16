# Runner capability envelopes

The six task files are the substantive prompts. Each was paired with one of
these sanitized role envelopes.

## No-skill baseline

```text
Complete task.md using only the task evidence and ordinary model capability.
Read only task.md in the current directory. Do not inspect sibling paths, user
skills, prior runs, criteria, or candidate files. Do not write files. Return
the complete user-facing artifact, followed by a concise path audit.
```

## Skilled run

```text
Use the local taste-extractor skill to complete task.md. Read only task.md and
files inside the candidate directory in the current capsule. Do not inspect
sibling paths, prior runs, or criteria. Do not write files. Return the complete
user-facing artifact, followed by a concise path audit.
```

The grader received only `task.md`, `criteria.md`, and one blinded output. The
candidate identity was concealed behind A/B labels whose order varied by case.
