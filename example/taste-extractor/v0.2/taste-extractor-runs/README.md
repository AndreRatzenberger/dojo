# Taste Extractor v0.2 run artifacts

This folder is the sanitized public tape for the v0.2 redo. The local raw run
tree remains the source receipt; machine paths and runner identifiers are
replaced here without rewriting substantive tasks, outputs, or scores.

## Artifact map

| Folder | Contents | Why it matters |
|---|---|---|
| `isolation/` | Role preflights and invalid-run ledger | Shows what each role could see and which broken runs counted for nothing. |
| `training/` | Six tasks, criteria, no-skill outputs, final skilled outputs, and scorecard | Makes the counterfactual improvement inspectable. |
| `corrections/` | Burned-attempt scores and affected-case regressions | Shows the misses that caused bounded edits instead of hiding them. |
| `holdouts/` | Post-freeze custody plus H16-H18 tasks, outputs, and blind scores | Supplies the actual graduation evidence. |
| `routing/` | Catalog, matrix, two proxy judges, and aggregate score | Checks when the skill should and should not trigger. |
| `package/` | Validators, discovery, cold smoke task, output, and score | Proves the installable folder works outside the authoring loop. |

Final candidate revision:
`sha256:b5ade59ca5952440b433fa122e40c0c69f0d5c62d9e98145021a74a2e1cf987f`.

Final outcome: **GRADUATED** under audited instruction-bounded evidence.
