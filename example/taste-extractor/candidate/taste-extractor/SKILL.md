---
name: taste-extractor
description: 'Extracts portable taste from any accessible medium into an evidence-traced profile and downstream production brief. Use when the user asks to extract, distill, reverse-engineer, or capture the style, taste, feel, visual language, voice, or character of an interface, image, text, video, music, object, brand, or experience so another agent can create new work with the same character without copying source content. Also use for cross-medium style translation. Refuse to fabricate a profile when the source cannot be inspected. Not for directly generating the final artifact unless the user asks for both extraction and creation.'
---

# Taste Extractor

## Purpose

Turn source evidence into a portable taste contract another agent can act on.
Preserve the character, not the source's literal content. Produce a receipt,
not a pile of adjectives: every major taste principle must trace back to an
observation and forward to a production rule.

## Establish The Job

Record before analysis:

- source artifact or artifacts
- source medium
- downstream medium and entity, when known
- accessible evidence and unavailable evidence
- user constraints, exclusions, and desired fidelity

If the downstream target is unknown, produce a medium-neutral profile and say
which translation decisions remain open.

## Verify Source Access

Inspect the source before describing its taste. If no meaningful source
evidence is available, or the source cannot be inspected at all:

1. state exactly what could and could not be inspected;
2. make no source-specific observation or inferred taste claim;
3. request an accessible artifact or structured observations;
4. provide a medium-aware intake checklist instead of a taste profile.

When evidence is partial, analyze only the supported axes and label the result
`provisional`. Name every missing modality or state, make no claim about those
unknown axes, request the smallest additional evidence needed, and keep the
downstream handoff inside what the inspected evidence supports.

Never infer taste from a filename, URL slug, title, reputation, or requested
target alone.

## Extract The Taste

Read [`references/taste-profile.md`](references/taste-profile.md) for the
medium axes and output template.

### 1. Observe Before Abstracting

Inventory concrete evidence using the relevant medium axes. Preserve useful
coordinates: quoted fragments, component names, frame or page locations,
timestamps, sequence positions, material details, or interaction states.
Trace negative and unknown claims too: an unsupported axis must cite the
coordinate, inspected range, or explicit evidence boundary that establishes
its absence. Do not leave `unknown` or `not established` rows unlocated.
When the task requests an axis-accounting table, every row must carry its own
explicit coordinate or boundary citation regardless of whether its status is
supported, partial, or unknown; do not rely on a nearby row or section heading
to supply the coordinate implicitly.
Explicitly account for every supported axis you rely on instead of silently
skipping it. For prose, give syntax, cadence, diction, imagery, point of view,
narrative distance, humor, omission, paragraph movement, and emotional
temperature their own explicit rows. Each supported row must cite a passage ID
and a short source fragment. Mark an axis `not established` only after naming
the passages inspected and why they do not support a claim.
If the task requests axes for each passage, build the full passage-by-axis
matrix and put a non-empty source quote in every supported cell. A nearby quote
or prose summary does not satisfy another cell. Audit the matrix cell by cell
before delivery.

### 2. Build The Taste Trace

For every major principle, write one row:

| Source evidence | Observation | Inferred principle | Confidence | Downstream consequence |
|---|---|---|---|---|

Give each inferred principle a stable ID. Every named inference used anywhere
else in the handoff, including the thesis, signature principles, tensions,
invariants, translations, and production rules, must point back to one of
those IDs. Do not introduce an untraced principle in explanatory prose. For a
multi-work corpus, each row must name its supporting works and an explicit
recurrence weight; a seductive outlier cannot support a principle by itself.
Keep direct observation and inference in separate columns. If a principle has
no evidence row, remove it or label it an unresolved hypothesis.

### 3. Separate The Transfer Layers

- **Source content:** names, story facts, phrases, logos, characters, motifs,
  exact compositions, melodies, or other identifiers. Do not transfer these.
- **Surface manifestations:** colors, materials, sentence shapes, instruments,
  layouts, gestures, or effects. Adapt only when the target medium supports the
  same job; do not copy them by reflex.
- **Portable principles:** relationships such as density, restraint, contrast,
  rhythm, hierarchy, emotional distance, feedback, imperfection, or surprise.
  These are the primary transfer layer.

### 4. Distill The Taste Contract

Produce:

- a one-sentence taste thesis
- three to seven signature principles
- productive tensions such as `dense, not cramped`
- invariants that must survive
- degrees of freedom the downstream agent may adapt
- anti-patterns that would turn the taste into costume
- originality guardrails that forbid source-content reuse

Do not manufacture exact values the source does not establish. Preserve them
as relational constraints or unknowns.

### 5. Translate Into The Target Medium

Map each retained principle through a translation table:

| Principle | Source manifestation | Target-medium decision | Literal copy to avoid |
|---|---|---|---|

When source and target use different media, translate the job performed by the
source choice, not its appearance. Accessibility, correctness, and the target
medium's function outrank stylistic fidelity.

For product, interface, or service handoffs, repeat that precedence explicitly
in the delivered contract: accessibility, correctness, and operational clarity
outrank extracted style and fidelity. Do not leave the priority merely implied
by individual rules.

For high-stakes product language, keep errors, identity, consent, fees,
security, permissions, and risk statements literal. Apply extracted voice only
to surrounding low-stakes guidance where it cannot blur meaning.

Preserve every explicit source prohibition, exclusivity rule, and safety
invariant as a named target invariant plus an executable yes/no check. Do not
collapse adjacent authorities during translation: when one role clears a
prerequisite and another owns the resulting decision or state transition,
model the clearance and handoff separately rather than granting the first role
the second role's authority. State uniqueness constraints, such as no duplicate
assignment, literally when the source contract depends on them.

### 6. Hand Off Production

Give the next agent:

- target-specific rules and a short production sequence
- a ready-to-use downstream prompt
- explicit degrees of freedom
- rejection tests for shallow imitation
- yes/no validation checks
- unresolved evidence gaps and confidence notes

When the requested downstream contract defines mandatory coordinates for
actions or transitions, put every normative action in one action register and
populate every required coordinate on every row. Explanatory prose may clarify
those rows but must not introduce additional unregistered actions.

Preserve exact contract vocabulary. If the task supplies field names, allowed
labels, literal phrases, enumerated states, or other closed values, repeat them
exactly and check each one before delivery. A recurrence count records cited
source occurrences, including a one-off outlier; express exclusion or design
weight in a separate field rather than changing the count to zero.

Do not create the final entity unless the user explicitly asks for extraction
and production in the same request. Keep the profile separable so another
agent can consume it without this conversation.

## Quality Gate

Before delivery, verify:

- every major principle has a taste-trace row;
- observed, inferred, and unknown claims are visibly distinct;
- negative and unknown claims cite the evidence boundary that supports them;
- source content is excluded from the portable layer;
- invariants and adaptable choices are both explicit;
- cross-medium mappings explain function rather than decoration;
- the handoff contains rules, freedoms, anti-patterns, and yes/no checks;
- product, interface, and service handoffs explicitly state that accessibility,
  correctness, and operational clarity outrank style and fidelity;
- high-stakes product language explicitly keeps errors, identity, consent,
  fees, security, permissions, and risk statements literal where applicable;
- partial evidence produces an explicitly provisional profile with no claims
  about missing modalities or states;
- an unavailable source produced an intake request, not invented taste.
- task-supplied labels, fields, phrases, states, and counts are reproduced with
  exact schema fidelity;
- every required prose passage-by-axis cell contains its own coordinate and
  source fragment;

## Final Report

Return the completed profile, then briefly name:

- source and access status
- downstream target
- strongest evidence-backed taste thesis
- unresolved evidence gaps
- where the downstream handoff begins
