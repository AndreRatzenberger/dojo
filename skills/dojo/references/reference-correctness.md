# Reference Correctness

Use this procedure for reference-tier campaigns. The question is whether the
skill's factual contract is correct and traceable for the declared version,
not whether a runner can perform a technique workflow.

## Build A Claim Inventory

List every externally checkable claim that can change an agent's action:

- commands, flags, defaults, schemas, limits, and compatibility
- authoritative definitions and required terminology
- version-dependent behavior and deprecations
- source citations, URLs, and quoted or paraphrased rules
- negative claims such as “unsupported,” “never,” or “only”

Assign each claim a stable identifier that remains unchanged across checks,
conflicts, reruns, and revisions. Do not verify a sample and imply the rest.

## Resolve Authority

Prefer primary authority in this order when applicable:

1. the declared version's executable behavior or source code
2. official versioned documentation, specification, or release notes
3. an explicitly named project-owned source of truth
4. a secondary source only when primary authority is unavailable, with that
   limitation recorded

Record source identifier, version or commit, and access date. Current or
version-sensitive claims require live verification. Never silently combine
conflicting sources; record the conflict and mark the claim unresolved until
an authority rule selects one.

## Verify And Record

Use one row per claim:

| Claim ID | Exact claim | Authority and version | Check performed | Status | Notes |
|---|---|---|---|---|---|
| R-01 | ... | ... | ... | pass/fail/unresolved | ... |

Treat this six-column schema as required evidence, not illustrative formatting.
Do not omit, merge, or paraphrase away `Claim ID`, `Exact claim`, `Authority and
version`, `Check performed`, `Status`, or `Notes` in the campaign procedure or
record. Every row needs all six fields, including explicit notes when there is
nothing exceptional to add.

Where safe and deterministic, exercise example commands or recipes against the
declared version. Separate documentation agreement from runtime agreement when
both matter. A stale link, unavailable authority, or ambiguous version is
`unresolved`, not a guessed pass.

## Reference Verdict

Reference correctness passes only when every action-affecting claim is `pass`.
Any `fail` produces `NOT GRADUATED`. Any required `unresolved` claim produces
`UNPROVEN` unless the skill removes or explicitly narrows that claim. Preserve
the inventory, source snapshot, checks, and conflicts in the Dojo record.
