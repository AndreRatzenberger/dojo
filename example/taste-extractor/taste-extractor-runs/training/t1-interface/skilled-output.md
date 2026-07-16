# Taste profile — operations product family

## Source and access

- Source: structured observations from daily overview, incident detail, empty state, and conference landing screen.
- Medium: desktop operations interface.
- Downstream target: alert-configuration panel.
- Access status: observations are inspectable; no screenshots, component specifications, or complete state inventory were supplied.
- Weighting: recurring operations surfaces receive primary weight (3/3 where applicable). The conference screen receives low family weight (0/3 recurrence) because release notes identify it as temporary and its language does not recur.

## Taste thesis

A disciplined, information-dense operational interface that uses rigid structure, terse language, and scarce semantic accents to make system state legible without visual theater (P1–P6).

## Observed interface axes

| Axis | Evidence |
|---|---|
| Composition/grid | Daily overview and incident detail share a strict twelve-column grid; empty state retains the same geometry. |
| Hierarchy/density | Daily overview uses dense tables; incident detail retains that density. Empty space separates systems rather than individual rows. |
| Typography/language | Daily overview uses monospaced numerals and terse noun labels; empty state uses one plain sentence. |
| Shape/components | Operations surfaces use near-square corners, hairline dividers, and an outlined empty-state action. |
| Color | Charcoal is the working field. Lime is reserved for live values and successful state changes; vermilion marks errors with a narrow edge. |
| Feedback/motion | Control changes receive a 120 ms snap, without bounce or blur. |
| Empty state | Existing geometry and typography remain; one sentence and one outlined action provide recovery. |
| Error state | The affected scope receives a narrow vermilion edge, never a filled red card. |
| Campaign outlier | Violet gradient, rounded cards, slogan, mascot, and elastic motion occur only on a temporary conference surface. |

## Taste trace

| ID | Source evidence and recurrence | Observation | Inferred principle | Confidence | Downstream consequence |
|---|---|---|---|---|---|
| P1 | Daily overview, incident detail, empty state: strict/shared geometry; 3/3 operations surfaces | Layout geometry persists across normal, incident, and empty contexts. | Structural continuity should survive state changes. | High | Keep the panel and all its states aligned to the product grid rather than introducing state-specific compositions. |
| P2 | Daily overview + incident detail: dense presentation; empty state: space separates systems, not rows; 3/3 | Information is compact within a system, while larger gaps mark system boundaries. | Density communicates operational relatedness; whitespace communicates architecture. | High | Group related alert settings compactly and reserve larger spacing for genuinely separate subsystems or stages. |
| P3 | Daily overview: lime only for live values and success; incident detail: narrow vermilion error edge; 2/2 relevant semantic states | Accent colors are scarce, state-bound, and localized. | Color is operational evidence, not decoration. | High | Use lime only for live/success meaning and vermilion only at the affected error scope; do not broaden either into ornamental surfaces. |
| P4 | Daily overview: terse noun labels and monospaced numerals; empty state: one plain sentence; 2/2 relevant language examples | Copy is compact and literal; numeric information is optimized for scanning. | Language should minimize interpretation cost. | High | Prefer short, concrete labels and plain guidance; use tabular or monospaced numerals where numeric comparison benefits. |
| P5 | Incident detail: 120 ms snap, no bounce or blur; 1/1 observed interaction specification | Feedback is immediate and restrained. | Motion confirms state change without becoming an event. | High for control changes; otherwise limited | Give control changes a crisp confirmation consistent with 120 ms; exclude elastic, blurred, or decorative motion. |
| P6 | Daily overview: near-square corners and hairline dividers; empty state retains geometry; 2/2 relevant surfaces | Shape and separators are precise rather than soft or card-like. | Components should read as parts of one instrument, not a collection of promotional objects. | High | Favor shared planes, restrained corners, and fine boundaries over rounded-card proliferation. |
| P7 | Conference screen only: gradient, rounded cards, slogan, mascot, elastic motion; 0/3 operations recurrence and explicitly temporary | Its visual grammar is isolated and campaign-specific. | Campaign expressiveness is an outlier, not product-family taste. | High | Exclude campaign treatments from the alert panel. |

## Transfer layers

- Source content—do not transfer: conference slogan, mascot, campaign imagery, or any literal labels and data from the observed screens.
- Surface manifestations—adapt deliberately: charcoal field, twelve-column alignment, near-square corners, hairlines, monospaced numerals, lime/vermilion accents, and 120 ms confirmation.
- Portable principles—preserve: structural continuity (P1), architecture-aware density (P2), semantic accent scarcity (P3), literal language (P4), restrained feedback (P5), and instrument-like component unity (P6).

## Taste contract

Signature principles:

1. Preserve one structural system across normal, empty, error, and changed states (P1).
2. Pack related operational information; separate distinct systems (P2).
3. Make every accent color carry a specific state meaning (P3).
4. Write for immediate scanning and unambiguous action (P4).
5. Let motion confirm, never entertain (P5).
6. Build a continuous operational instrument rather than a stack of promotional cards (P6).

Productive tensions:

- Dense, not cramped (P2).
- Severe, not hostile (P3, P6).
- Immediate, not animated (P5).
- Terse, not cryptic (P4).
- Visually quiet, but unmistakable when state changes (P3, P5).

Invariants:

- State changes must not reorganize the underlying geometry (P1).
- Lime remains exclusive to live values and successful state changes (P3).
- Errors use a localized vermilion edge at the affected scope, not a filled red container (P3).
- Related rows remain compact; major whitespace denotes system boundaries (P2).
- Control confirmation is crisp, with no bounce, blur, or elastic motion (P5).
- Campaign gradient, mascot, slogan scale, rounded-card language, and elastic motion do not enter the operations panel (P7).
- Accessibility, correctness, and operational clarity outrank extracted style and fidelity.

Degrees of freedom:

- Exact column allocation within the twelve-column system.
- Control types, field ordering, and grouping based on alert-configuration tasks.
- Exact charcoal, divider, and text values, subject to accessible contrast.
- Whether a boundary is expressed by a hairline, spacing, or both.
- Copy wording, provided it remains plain, concise, and unambiguous.
- Responsive behavior, loading treatment, and focus treatment, which the evidence does not establish.

## Translation to the alert panel

| Principle | Source manifestation | Target-medium decision | Literal copy to avoid |
|---|---|---|---|
| P1 | Shared grid and geometry across states | Anchor configuration, validation, empty, and confirmation states to one panel structure. | Reproducing an observed screen’s exact composition. |
| P2 | Dense rows; space between systems | Compact related settings and use larger intervals only between conceptual systems. | Copying table density where form comprehension requires more room. |
| P3 | Rare lime; narrow vermilion error edge | Reserve accents for their established meanings and place errors at the failing scope. | Decorative lime, success-colored primary actions, or filled red cards. |
| P4 | Noun labels, plain sentence, monospaced numerals | Use concrete labels, literal help text, and scan-friendly numeric presentation. | Reusing source phrases or forcing noun-only wording when clarity suffers. |
| P5 | 120 ms snap | Use brief, crisp feedback for control changes where motion is appropriate. | Elastic campaign motion or animating every update. |
| P6 | Near-square geometry and hairlines | Prefer integrated sections and precise boundaries over floating rounded cards. | Mechanically copying every divider regardless of hierarchy. |
| P7 | Temporary campaign language | Treat campaign styling as explicitly out of scope. | Gradient, mascot, slogan typography, or campaign card shapes. |

## Production sequence

1. Establish the panel’s task hierarchy and map it onto the existing grid (P1).
2. Group settings by operational system, keeping related controls compact (P2).
3. Define normal, changed, success, error, and empty behavior without changing structure (P1).
4. Assign color only after state semantics are defined (P3).
5. Write concise labels and literal guidance; keep errors, identity, consent, fees, security, permissions, and risk statements fully explicit (P4).
6. Add restrained control feedback where it aids confirmation (P5).
7. Remove promotional card, campaign, and decorative-accent drift (P6, P7).
8. Validate accessibility, correctness, and operational clarity before stylistic fidelity.

## Downstream prompt

> Design an alert-configuration panel for a dense desktop operations product. Preserve structural continuity across normal, changed, success, error, and empty states (P1). Keep related controls compact and use larger whitespace only to separate distinct systems (P2). Treat color as operational evidence: lime is exclusive to live values and successful state changes; vermilion appears only as a narrow marker at the affected error scope, never as a filled error card (P3). Use terse, concrete labels, plain guidance, and scan-friendly numerals without sacrificing comprehension (P4). Control changes may receive a crisp 120 ms confirmation, with no bounce, blur, or elastic motion (P5). Favor integrated planes, near-square geometry, and fine boundaries over rounded-card stacks (P6). Exclude the temporary campaign language—violet gradient, mascot, oversized slogan, rounded promotional cards, and elastic motion (P7). Do not reuse source content or exact compositions. Accessibility, correctness, and operational clarity outrank style and fidelity; keep all high-stakes language literal.

## Rejection and validation checks

- [ ] Does every state retain the same underlying grid and hierarchy?
- [ ] Does larger whitespace separate systems rather than individual rows?
- [ ] Is every use of lime either a live value or successful state change?
- [ ] Is each error marked locally with a narrow vermilion edge, with no filled red card?
- [ ] Are labels concise but still unambiguous?
- [ ] Are numeric values optimized for scanning where useful?
- [ ] Is control feedback crisp and free of bounce, blur, and elastic motion?
- [ ] Does the panel avoid unnecessary rounded-card fragmentation?
- [ ] Are all campaign-only motifs absent?
- [ ] Are source phrases, imagery, and exact compositions absent?
- [ ] Do accessible contrast, focus visibility, correctness, and operational clarity take precedence over stylistic fidelity?
- [ ] Are errors, identity, consent, fees, security, permissions, and risk statements literal?

## Evidence gaps and confidence

The profile is high-confidence for grid, density, semantic color, error treatment, control-change motion, geometry, and campaign exclusion. It is provisional for focus, hover, disabled, loading, permissions, destructive confirmation, responsive behavior, detailed typography beyond numerals, and full accessibility behavior because those states were not observed. The smallest useful supplement would be annotated captures of those states plus the product’s component and accessibility specifications.

The downstream handoff begins at “Taste contract”; the standalone production brief is under “Downstream prompt.”

Boundary audit: Read only `task.md`, `taste-extractor/SKILL.md`, and `taste-extractor/references/taste-profile.md` within the current directory. No files were written or modified.