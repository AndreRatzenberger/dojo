# Package checks

Candidate tree digest:
`01117cd40581534f188dc93461d53e96740ddd0d95815e23119853afc74d6643`

Portable candidate content digest:
`62704fed613ecb6751e106e20b1e98e133ad802882edf0028d73445483409cdd`

| Check | Result |
|---|---|
| Standard Agent Skill validator | pass — `Skill is valid!` |
| Skill directory equals frontmatter name | pass — `taste-extractor` |
| Description length | pass — 629 characters |
| Direct reference resolution | pass — `references/taste-profile.md` |
| Agent metadata | pass — `$taste-extractor` default prompt present |
| Isolated copy and byte comparison | pass — no difference |
| Skills CLI discovery | pass — exactly one skill found |
| Candidate tree unchanged after training | pass — frozen digest matched |
| Candidate tree unchanged after both holdouts | pass — frozen digest matched |
| Clean-context smoke invocation | pass — complete profile and handoff produced |
| Routing proxy | pass — two judges, 30/30 declared decisions matched |

The local Skills CLI source path is intentionally omitted from this receipt;
the checked-in example uses `<candidate-root>` in command examples.
