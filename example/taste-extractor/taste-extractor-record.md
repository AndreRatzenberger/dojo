# Dojo record — taste-extractor

*Tier: technique · 2026-07-15 · isolated agent contexts / model identifier not exposed*

Repository root: <repository-root>
Root resolution: git
Repository slug: dojo

## Claim

Given accessible evidence from any medium, `taste-extractor` separates source
content from portable taste, traces abstractions to observations, distinguishes
invariants from adaptable qualities, and produces an implementation handoff
another agent can use without copying the source. Without source access, it
requests appropriate evidence instead of inventing a profile.

## Baseline findings

| Scenario | Failure mode |
|---|---|
| Interface to interface | No observed failure: 5/5 before training. |
| Prose to onboarding microcopy | 4/5: principles were not traced one by one to concrete source evidence. |
| Ceramics to status page | No observed failure: 5/5 before training. |
| Inaccessible source | No observed failure: safe refusal passed 4/4 before training. |

## Loopholes closed

| # | Loophole | Bounded edit |
|---|---|---|
| 1 | A polished taste summary could pass without showing how each major principle follows from source evidence. | Require a Taste Trace for every major principle: source evidence, observation, inferred principle, confidence, and downstream consequence. Unsupported principles are removed or marked unresolved. |

## Rejected fixes

| # | Attempt | Why it was rejected |
|---|---|---|
| N/A | No candidate edit was rejected. | The first bounded instruction corrected the only observed baseline failure and preserved all previously passing behavior. |

## Training result

| Scenario | Baseline | Skilled | Result |
|---|---:|---:|---|
| Interface to interface | 5/5 | 5/5 | preserved |
| Prose to onboarding microcopy | 4/5 | 5/5 | corrected |
| Ceramics to status page | 5/5 | 5/5 | preserved |
| Inaccessible source | 4/4 | 4/4 | preserved |

## Pressure testing

Not applicable. This is a technique-tier skill. Separate time-pressure,
sunk-cost, and authority-pressure variants are required for discipline skills,
not for this tier.

## Graduation

The candidate was frozen at tree digest
`01117cd40581534f188dc93461d53e96740ddd0d95815e23119853afc74d6643`
before either holdout was opened. Both were run once in fresh contexts with no
candidate edit between them. The digest matched after both runs.

| Holdout | Result | Notes |
|---|---|---|
| Contemporary dance duet to architecture-decision meeting | 5/5 — pass | Timestamped relational and temporal evidence became an exactly timed, non-themed 45-minute facilitation protocol. |
| Printed field-guide family to public-transport IVR | 5/5 — pass | Recurring family rules outranked a one-off variant and became an implementable audio information system. |

No holdout was burned.

## Trigger matrix

No callable production dispatcher was exposed. Expected owners were declared
first, then two isolated routing judges served as an explicit proxy. Both
judges matched all 15 rows: 30/30 decisions correct.

| # | Prompt | Expected | Actual | Pass |
|---|---|---|---|---|
| 1 | Extract reusable taste from three landing pages. | taste-extractor | taste-extractor (2/2) | yes |
| 2 | Reverse-engineer an essay's voice without copying phrases. | taste-extractor | taste-extractor (2/2) | yes |
| 3 | Translate a ceramic collection's taste into status-page rules. | taste-extractor | taste-extractor (2/2) | yes |
| 4 | Turn music-video observations into a launch-film motion grammar. | taste-extractor | taste-extractor (2/2) | yes |
| 5 | Distill a synth track into a game-audio production handoff. | taste-extractor | taste-extractor (2/2) | yes |
| 6 | Translate a service ritual into a new app flow. | taste-extractor | taste-extractor (2/2) | yes |
| 7 | Use the skill on an inaccessible link and request evidence if needed. | taste-extractor | taste-extractor (2/2) | yes |
| 8 | Build an evidence-traced style profile from product photos. | taste-extractor | taste-extractor (2/2) | yes |
| 9 | Extract invariants and variables across packaging variants. | taste-extractor | taste-extractor (2/2) | yes |
| 10 | Create an Agent Skill for reconciling CSV schemas. | skill-creator | skill-creator (2/2) | yes |
| 11 | Use Dojo to test taste-extractor before publication. | dojo | dojo (2/2) | yes |
| 12 | Generate a transparent bitmap illustration. | imagegen | imagegen (2/2) | yes |
| 13 | Rewrite a paragraph to sound less AI-generated. | humanizer | humanizer (2/2) | yes |
| 14 | Repair an overloaded product naming model. | naming-as-design | naming-as-design (2/2) | yes |
| 15 | James-review an implementation plan for cold execution. | james | james (2/2) | yes |

## Package

| Check | Result |
|---|---|
| Standard Agent Skill validator | pass |
| Name, description, reference, and agent metadata | pass |
| Isolated byte-for-byte copy | pass |
| Skills CLI discovery | pass — exactly one skill |
| Clean-context package smoke | pass |
| Frozen tree integrity | pass after training and both graduation runs |

## Known limitations

- The evaluation represents media through supplied evidence packets. It does
  not yet prove direct inspection across image, audio, video, or physical
  artifact tooling.
- Three baselines were already strong. The demonstrated behavioral improvement
  is specifically the prose trace from 4/5 to 5/5; the other runs demonstrate
  preservation and generalization, not a claim that every useful behavior came
  only from the skill.
- Routing used two isolated proxy judges, not a production dispatcher.
- The candidate was evaluated as the environment's taste-extraction
  capability, not installed alongside another same-purpose skill.
- A finite scenario set cannot exhaust the phrase “any medium.” Unknown source
  access and downstream constraints still require honest degradation.
- The host did not expose a model identifier. Isolation was fresh-context
  isolation within the available host, not diversity across model families.
- The original graduation tree digest includes local absolute filenames and is
  therefore path-bound. The freeze receipt also publishes a path-independent
  file manifest and portable content digest for the copied candidate.
- The repository example is a sanitized copy of local evidence. Path and
  runner identifiers are replaced before publication; substantive prompts,
  outputs, criteria, and scores are retained.
