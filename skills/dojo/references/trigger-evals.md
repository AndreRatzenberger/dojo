# Trigger Evaluations

The skill description is always visible to the router. Test whether it selects
the right work and stays out of adjacent work.

## Matrix

Start with 10–15 prompts. Expand when needed so every declared mode, explicit
exclusion, and credible neighboring skill owner appears at least once. A broad
multi-mode skill does not inherit the same routing budget as a narrow command
reference.

Use approximately:

- About 60% should-trigger positives, using real user language, slang, partial
  phrasing, and explicit invocations.
- About 40% near-miss negatives, especially prompts containing the same nouns
  but owned by another installed skill or no skill.

Declare the expected owner before running the judges. Allow multiple owners
only when the row is explicitly marked ambiguous in advance.

## Competitive Landscape

Use the active host's actual skill catalog when available. Preserve the exact
`name: description` snapshot, host, and date. Do not silently substitute every
skill found in caches or inactive directories.

Prefer exercising the real dispatcher. When that is unavailable, use two
fresh routing judges as an explicit proxy and give each the complete active
description list.

## Proxy Judge Prompt

```text
You are a skill-routing judge. Below is the active list of installed skills as
name and description pairs. For each prompt, return the single skill you would
invoke, or "none".

Output one line per prompt:
<number>: <skill-name-or-none>

SKILLS:
<complete active description list>

PROMPTS:
<numbered matrix>
```

Run the identical prompt in two fresh contexts.

## Scoring

- A row passes only when both proxy judges match the expected owner, or when
  the real dispatcher produces an accepted owner.
- Every positive must hit.
- Every negative must avoid the candidate skill.
- Report `X/N`, collisions, orphans, and judge disagreements separately.

## Tuning

- Missed positive: add the missing request shape to the description.
- Collision: sharpen the job boundary and exclusions.
- Disagreement: inspect ambiguity before changing prose.

Rerun the complete matrix after every description edit. Three failed tuning
rounds indicate a real scope collision, not a wording problem.
