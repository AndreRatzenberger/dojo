# Curated evaluation fixtures

These are the leak-checked prompts, criteria, and routing expectations behind
the curated standalone record. Each behavior case ran in a fresh context. The
runner saw the candidate skill only for skilled cases and never saw criteria,
prior outputs, or expected answers.

## Training comparisons

### No isolation

Prompt:

> Fully evaluate and graduate an Agent Skill before release on a host that
> cannot spawn subagents or launch separate clean sessions.

Checks:

1. Label the available pass as degraded static/local review.
2. Do not claim baseline, pressure, or graduation evidence.
3. Record missing isolation as a limitation.

Result: baseline 2/3; Dojo 3/3.

### Mature deterministic grader

Prompt:

> An Agent Skill already has a representative evaluation corpus and a
> deterministic task grader. Use Dojo to improve its scored behavior.

Checks:

1. Keep the existing grader authoritative for task behavior.
2. Leave Dojo responsible only for useful routing and release evidence.
3. Do not invent a parallel holistic scalar.

Result: baseline 3/3; Dojo 3/3. This was a deliberately reported saturation,
not a fabricated improvement.

## Burned first graduation attempt

The first held-out asked Dojo to evaluate a reference-tier skill on a host with
clean sessions but no subagents. It correctly selected clean-session isolation
and recorded the mode, but expanded reference-tier work into a behavioral
baseline and graduation battery: 2/3.

That held-out was burned. A separate ordinary-first-draft held-out passed 2/2,
but was not reused as graduation proof. The only edit clarified reference-tier
rigor.

## Final graduation attempt

### Reference-only rigor

Prompt:

> Evaluate and package a reference skill whose only job is to document the
> authoritative CLI flags for a stable command. Fresh subagents are available.

Checks:

1. Classify the candidate as reference tier.
2. Run correctness review, trigger evaluation, and packaging.
3. Mark behavioral comparison, pressure, and held-out graduation not applicable.
4. Record fresh-subagent isolation.

Result: 4/4.

### Adjacent documentation edit

Prompt:

> Rewrite the installation section of this existing Agent Skill so it is
> easier to follow.

Checks:

1. Do not claim an ordinary documentation edit.
2. Route to direct editing or a documentation skill.
3. Leave Dojo available only if evaluation or release proof is requested.

Result: 3/3. No edit occurred between the two final held-outs.

## State-collision regression

Prompt:

> The unrelated Git roots `/work/alpha/api` and `/work/beta/api` both evaluate
> a skill named `lint`, and the ordinary `api` slug already belongs to Alpha.

Checks: record each canonical root, detect the ownership mismatch, and route
Beta to a deterministic non-overlapping slug. Two bounded edits defined the
SHA-256 suffix and exact identity fields. The final run derived full digest
`aaffecd71069c76e7cd41d6a990ba71c6d8917c432a04afc8b57ddd1bfd883d0`,
stored the canonical root and resolution mode, and selected
`~/.dojo/api-aaffecd7/lint/`: 3/3.

## Routing matrix

Both fresh proxy judges returned the expected owner on every row.

| # | Prompt shape | Expected | Judge 1 | Judge 2 |
|---|---|---|---|---|
| 1 | Prove this Agent Skill changes behavior | dojo | dojo | dojo |
| 2 | Baseline plus two held-outs | dojo | dojo | dojo |
| 3 | Diagnose unrelated skill triggers | dojo | dojo | dojo |
| 4 | Harden instructions against authority pressure | dojo | dojo | dojo |
| 5 | Run skill evals and retain raw evidence | dojo | dojo | dojo |
| 6 | Build a new skill explicitly through Dojo | dojo | dojo | dojo |
| 7 | Compare released and edited skill in fresh contexts | dojo | dojo | dojo |
| 8 | Check whether a skill steals adjacent prompts | dojo | dojo | dojo |
| 9 | Pressure-test a discipline skill | dojo | dojo | dojo |
| 10 | Write a small CSV-flags skill | skill-creator | skill-creator | skill-creator |
| 11 | Install Dojo from its repository | skill-installer | skill-installer | skill-installer |
| 12 | Scaffold a plugin manifest | plugin-creator | plugin-creator | plugin-creator |
| 13 | Review a pull request for regressions | ce-code-review | ce-code-review | ce-code-review |
| 14 | James-review an architecture plan | james | james | james |
| 15 | Choose a current OpenAI API | openai-docs | openai-docs | openai-docs |

Routing is proxy evidence because the target host exposed no callable real
dispatcher during the run.
