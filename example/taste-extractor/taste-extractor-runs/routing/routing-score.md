# Routing proxy score

Result: **pass — 30/30 decisions matched**

The environment did not expose a callable production dispatcher, so two fresh
isolated routing judges were used as an explicit proxy. Expected owners were
declared before either judge ran.

| Judge | Correct | Incorrect | Result |
|---|---:|---:|---|
| 1 | 15 | 0 | pass |
| 2 | 15 | 0 | pass |

Both judges selected `taste-extractor` for all nine positive prompts and kept
all six near-miss prompts with their declared neighboring skills.
