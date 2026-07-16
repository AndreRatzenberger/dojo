# Dojo scenarios — taste-extractor

Repository root: <repository-root>
Root resolution: git
Repository slug: dojo

Date: 2026-07-15
Host: fresh agent contexts
Model identifier: not exposed by host
Isolation: v1 fresh-context only; prompt boundary without a v0.2 canary or complete trace
Tier: technique

> **v0.2 evidence classification:** historical `fresh-context only`, not
> retroactively audited instruction-bounded evidence.

Criteria were written before any behavior run. Training scenarios may inform
bounded edits. Holdouts were kept outside the authoring loop, then run once
after the candidate was frozen.

## Claim

Given accessible evidence from any medium, `taste-extractor` should separate
source content from portable style, trace its abstractions to observations,
distinguish invariants from adaptable qualities, and produce an actionable
handoff that another agent can use without copying the source. When the source
cannot be inspected, it should refuse to invent a taste profile and request
the missing evidence.

## T1 — Interface to interface

Archetype: extract taste within the same medium.

Observable criteria:

1. Separates direct observations from inferred taste principles.
2. Covers composition, typography, color, density, motion, and interaction.
3. Distinguishes invariants from adaptable choices.
4. Names anti-patterns and source-copying boundaries.
5. Produces an actionable downstream handoff and yes/no validation checks.

Expected baseline weakness: an attractive mood-board summary without explicit
evidence mapping, adaptation rules, or a testable handoff.

## T2 — Prose to prose

Archetype: extract taste while separating voice from story content.

Observable criteria:

1. Separates narrative facts and distinctive phrases from reusable style.
2. Analyzes syntax, cadence, diction, narrative distance, humor, and omission.
3. Traces every major principle to a concrete source observation.
4. Translates the profile specifically for onboarding microcopy.
5. Supplies originality guardrails and yes/no validation checks.

Expected baseline weakness: loose adjectives or imitation that reuses the
passage's nouns, metaphors, or sentence shapes.

## T3 — Ceramics to a status page

Archetype: translate taste across media.

Observable criteria:

1. Reads form, material, imperfection, palette, spacing, and collection rhythm.
2. Separates medium-specific surface from portable principles.
3. Maps each retained principle to a concrete status-page decision.
4. Rejects literal pottery decoration and other shallow visual copying.
5. Produces an implementation handoff another agent can follow.

Expected baseline weakness: literal beige-and-clay styling without a defensible
translation from physical craft to interface behavior.

## T4 — Unavailable source

Archetype: degraded dependency handling.

Observable criteria:

1. States that the source cannot be inspected from the supplied context.
2. Makes no source-specific observations or inferred taste claims.
3. Requests an accessible artifact or structured observations.
4. Offers a medium-aware intake checklist rather than fabricating a profile.

Expected baseline weakness: guessing a profile from the title, URL, or user's
desired output.

## Heldouts

Two holdouts are stored in `taste-extractor-runs/holdouts/held-out-custody.md`.
They were designed in a fresh context and must not be opened until the
candidate skill is frozen after the training runs. Custody SHA-256:
`337f6c7fcfce50f17dedf8dc1b3bbb787ffa82b8f4deb63b21a1d9223db2cd3e`.

## Result ledger

| Run | Result | Notes |
|---|---|---|
| T1 baseline | 5/5 | Strong default interface extraction |
| T2 baseline | 4/5 | No principle-by-principle evidence trace |
| T3 baseline | 5/5 | Strong default cross-medium translation |
| T4 baseline | 4/4 | Correct missing-source refusal |
| T1 skilled | 5/5 | Regression preserved; explicit trace and contract |
| T2 skilled | 5/5 | Taste Trace corrected the observed failure |
| T3 skilled | 5/5 | Regression preserved; stable receipt shape |
| T4 skilled | 4/4 | Safe refusal preserved and formalized |
| Holdout 1 | 5/5 | One-shot graduation run passed after freeze |
| Holdout 2 | 5/5 | One-shot graduation run passed after freeze |
