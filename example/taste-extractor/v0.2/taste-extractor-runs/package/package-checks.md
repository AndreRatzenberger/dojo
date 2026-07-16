# Package checks

Candidate revision:
`sha256:b5ade59ca5952440b433fa122e40c0c69f0d5c62d9e98145021a74a2e1cf987f`

| Check | Result |
|---|---|
| Standard Agent Skill validator | pass — `Skill is valid!` |
| YAML frontmatter parse | pass — name and description present |
| Candidate tree | pass — three regular files; no symlinks or special files |
| Direct reference | pass — `references/taste-profile.md` resolves |
| Agent metadata | pass — `agents/openai.yaml` parses and names the skill |
| Skills CLI discovery | pass — exactly one skill, `taste-extractor` |
| Routing proxy | pass — 30/30 declared decisions |
| Clean-context smoke | pass — cold invocation produced the evidence trace and implementation handoff |
| Frozen integrity | pass — digest matched before holdouts, after holdouts, and after smoke |

Public command examples use `<candidate-root>`; local discovery paths are not
part of this receipt.
