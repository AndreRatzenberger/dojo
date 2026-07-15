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

Inspect the source before describing its taste. If the source, required tool,
or relevant modality is unavailable:

1. state exactly what could and could not be inspected;
2. make no source-specific observation or inferred taste claim;
3. request an accessible artifact or structured observations;
4. provide a medium-aware intake checklist instead of a taste profile.

Never infer taste from a filename, URL slug, title, reputation, or requested
target alone.

## Extract The Taste

Read [`references/taste-profile.md`](references/taste-profile.md) for the
medium axes and output template.

### 1. Observe Before Abstracting

Inventory concrete evidence using the relevant medium axes. Preserve useful
coordinates: quoted fragments, component names, frame or page locations,
timestamps, sequence positions, material details, or interaction states.

### 2. Build The Taste Trace

For every major principle, write one row:

| Source evidence | Observation | Inferred principle | Confidence | Downstream consequence |
|---|---|---|---|---|

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

### 6. Hand Off Production

Give the next agent:

- target-specific rules and a short production sequence
- a ready-to-use downstream prompt
- explicit degrees of freedom
- rejection tests for shallow imitation
- yes/no validation checks
- unresolved evidence gaps and confidence notes

Do not create the final entity unless the user explicitly asks for extraction
and production in the same request. Keep the profile separable so another
agent can consume it without this conversation.

## Quality Gate

Before delivery, verify:

- every major principle has a taste-trace row;
- observed, inferred, and unknown claims are visibly distinct;
- source content is excluded from the portable layer;
- invariants and adaptable choices are both explicit;
- cross-medium mappings explain function rather than decoration;
- the handoff contains rules, freedoms, anti-patterns, and yes/no checks;
- an inaccessible source produced an intake request, not invented taste.

## Final Report

Return the completed profile, then briefly name:

- source and access status
- downstream target
- strongest evidence-backed taste thesis
- unresolved evidence gaps
- where the downstream handoff begins
