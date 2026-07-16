# Taste profile — hand-thrown breakfast ceramics

## Source and access

- Source: Structured observations of four bowls, one tall cup, spatial presentation, repairs, finish, and use.
- Source medium: Physical craft collection, represented through written observations.
- Downstream target: Public service-status page.
- Access status: Sufficient for a provisional translation of form, finish, variation, repair, hierarchy, spacing, and collection rhythm.
- Unavailable: Direct visual inspection, scale, weight, tactility, underside and joinery views, wear over time, and additional use states.

## Taste thesis

A calm, useful system should feel human without becoming decorative: establish a restrained family, permit bounded irregularity, reveal recovery plainly, leave generous space, and keep service information dominant (P1–P6).

## Taste trace

| Source evidence | Observation | Inferred principle | Confidence | Downstream consequence |
|---|---|---|---|---|
| Four bowls: “slightly off-round,” with visible thumb marks | Repeated forms retain small production differences | **P1 — Bounded variation:** consistency comes from family resemblance, not mechanical sameness | High | Reuse a coherent component system while allowing limited variation in content length, grouping, and emphasis |
| One cobalt line stops before completing a circle; spacing and weight vary | A recurring mark is restrained, incomplete, and non-identical | **P2 — Restraint over completion:** signals may be concise and need not visually enclose everything | High | Avoid excessive containers, rules, badges, and repeated framing; use emphasis only where it has a job |
| Three quiet forms followed by one tall cup, connected by shared finish and handwork | One proportional exception remains recognizably part of the set | **P3 — Coherent exception:** an unusual item may stand out without abandoning the system | High | Let a major incident receive stronger scale or placement while retaining the same structural and typographic language |
| Objects sit far apart on rough linen; nothing is glossy | Separation is generous and the finish suppresses glare and spectacle | **P4 — Quiet spaciousness:** clarity comes from breathing room and low visual sheen | High | Maintain generous grouping space, restrained surfaces, and low decorative contrast |
| Two repaired pieces expose their joins without ornamenting them | Repair is legible but not celebrated as decoration | **P5 — Matter-of-fact recovery:** show disruption and restoration honestly, without dramatization | High | Present incidents, updates, and resolution history clearly; distinguish repaired service from uninterrupted service without celebratory effects |
| Food remains visually dominant; decoration never competes with use | The object supports its purpose rather than demanding attention | **P6 — Utility-led hierarchy:** operational content must remain the focal layer | High | Status, affected services, impact, timestamps, and guidance outrank branding and stylistic expression |

## Transfer layers

### Source content — do not transfer

Do not reuse pottery colors, vessel shapes, incomplete circles, thumb marks, glaze effects, linen imagery, repaired-crack graphics, brush strokes, or craft language.

### Surface manifestations — adapt deliberately

Off-round forms, matte glaze, sparse marks, irregular spacing, and visible repairs are source-specific manifestations. Translate only their functions: bounded variation, restraint, spaciousness, and honest recovery.

### Portable principles — preserve

- P1: Bounded variation
- P2: Restraint over completion
- P3: Coherent exception
- P4: Quiet spaciousness
- P5: Matter-of-fact recovery
- P6: Utility-led hierarchy

## Signature principles

1. **P1 — Build a family, not a field of clones.** Components should share structure while accommodating real differences in service names, incident depth, and update history.
2. **P2 — Use fewer visual assertions.** Every border, badge, rule, or highlight must clarify state or hierarchy.
3. **P3 — Make exceptional severity prominent but structurally familiar.** Urgency may change emphasis, never the page’s underlying grammar.
4. **P4 — Give information room to separate naturally.** Prefer spacing and grouping over ornamental dividers.
5. **P5 — Treat recovery as part of the record.** Preserve incident chronology and resolved states in direct language.
6. **P6 — Keep operational truth dominant.** The page exists to answer what is affected, how severely, since when, and what users should do.

## Productive tensions

- Human, not whimsical (P1)
- Varied, not inconsistent (P1)
- Restrained, not vague (P2)
- Exceptional, not alien to the system (P3)
- Spacious, not sparse of necessary information (P4, P6)
- Transparent, not theatrical (P5)
- Calm, not falsely reassuring (P5, P6)

## Invariants

- Current service condition, impact, scope, timestamps, and user guidance remain explicit and easy to find (P6).
- Incident severity is never communicated through subtle styling alone; use literal text and accessible semantics (P3, P6).
- Active, monitoring, resolved, and historical states remain distinguishable in wording and structure (P5).
- Recovery history is not erased or converted into decoration (P5).
- No visual treatment competes with operational content (P2, P6).
- Accessibility, correctness, responsive behavior, and service-status conventions outrank stylistic fidelity (P4, P6).

## Degrees of freedom

The implementing agent may choose the grid, typeface, neutral palette, spacing scale, breakpoints, component architecture, data source, and interaction details. It may also decide whether service groups use rows, cards, or another accessible structure.

Those choices must preserve restrained emphasis (P2), coherent exceptions (P3), generous separation (P4), plain recovery records (P5), and operational hierarchy (P6).

## Target translation

| Principle | Source manifestation | Target-medium decision | Literal copy to avoid |
|---|---|---|---|
| P1 — Bounded variation | Similar bowls with small differences | Use shared service and incident components that tolerate differing content without forced visual uniformity | Wobbly geometry or intentionally misaligned UI |
| P2 — Restraint over completion | Sparse, incomplete recurring line | Remove nonfunctional framing; introduce emphasis only for state, impact, or navigation | Incomplete circles, brush lines, decorative underlines |
| P3 — Coherent exception | One tall cup within a quiet family | Give the highest-priority incident stronger hierarchy while preserving the same component grammar | Vessel-like proportions or novelty layouts |
| P4 — Quiet spaciousness | Widely separated objects and non-glossy finish | Use spacing, grouping, and restrained surfaces to reduce noise and support scanning | Linen textures, glaze simulation, faux-matte effects |
| P5 — Matter-of-fact recovery | Visible, unornamented joins | Provide plain incident timelines, resolution timestamps, and persistent history | Crack motifs, repair seams, celebratory “fixed” effects |
| P6 — Utility-led hierarchy | Food dominates decoration | Put overall status, affected services, impact, latest update, and guidance before brand expression | Craft metaphors or decorative storytelling |

## Implementation rules

- Lead with a literal overall status and its last-updated time (P6).
- Organize services into predictable, reusable structures with explicit text states (P1, P6).
- Reserve the strongest emphasis for the most consequential active incident; keep it inside the established system (P3).
- Use whitespace and semantic grouping before adding borders or containers (P2, P4).
- For every incident, expose status, affected scope, impact, start time, update chronology, and resolution state when applicable (P5, P6).
- Keep errors, permissions, security notices, risks, and user actions literal. Extracted character may shape surrounding low-stakes guidance but must not soften meaning (P5, P6).
- Do not fabricate irregularity through random offsets, dimensions, spacing, or typography (P1).
- Do not derive a palette or numeric design tokens from the source; the evidence establishes relationships, not exact values (P2, P4).

## Production sequence

1. Define the status data model and explicit state vocabulary (P5, P6).
2. Establish the information hierarchy for overall status, active incidents, services, history, and user guidance (P6).
3. Create reusable structures that accept natural content variation (P1).
4. Define one accessible escalation treatment for exceptional incidents (P3).
5. Reduce unnecessary framing and separate groups primarily through space (P2, P4).
6. Add incident chronology and resolved-state behavior without ornamental recovery cues (P5).
7. Test accessibility, responsive layouts, long content, simultaneous incidents, stale data, loading, empty, and error states (P1, P5, P6).

## Downstream prompt

Design and implement a public service-status page using this taste contract:

Create a calm, utility-led interface whose components form a coherent family while accommodating real content variation (P1). Keep visual assertions restrained and functional (P2). Allow a major active incident to become clearly prominent without changing the system’s underlying grammar (P3). Use generous separation and low-noise surfaces to support scanning (P4). Show incident progression and recovery plainly, including timestamps and history, without dramatizing or decorating repair (P5). Ensure current status, affected scope, impact, updates, and user guidance dominate the experience (P6).

Use literal, accessible text and semantics for every state. Preserve clarity across normal, loading, stale-data, empty, degraded, major-incident, monitoring, resolved, and error states. Accessibility and operational correctness outrank style.

Do not use pottery colors, vessel forms, incomplete-circle motifs, cracks, brush strokes, glaze or linen textures, handmade-looking misalignment, craft metaphors, or randomized irregularity. Choose implementation technologies and exact visual tokens appropriate to the product; the source does not establish them.

## Rejection tests

Reject the implementation if:

- It resembles pottery through color, texture, shape, marks, repair graphics, or language.
- “Human” character is simulated with random misalignment or inconsistent spacing (P1).
- A major incident looks like a different product rather than a coherent exception (P3).
- Decorative restraint makes severity, impact, or actions ambiguous (P2, P6).
- Recovery is hidden, erased, glamorized, or turned into a visual motif (P5).
- Branding or visual atmosphere outranks service information (P6).
- Spaciousness causes essential context to fragment or disappear below the fold without clear hierarchy (P4, P6).

## Yes/no validation checks

- [ ] Is the overall condition stated literally and exposed semantically? (P6)
- [ ] Can users identify affected services, impact, latest update, and relevant action without interpreting decoration? (P6)
- [ ] Are color-independent labels or symbols used for every operational state? (P3, P6)
- [ ] Do shared components handle natural content variation without randomized styling? (P1)
- [ ] Does exceptional severity remain within the established component language? (P3)
- [ ] Does every border, badge, highlight, and animation serve an informational purpose? (P2)
- [ ] Does spacing improve grouping without separating related facts? (P4)
- [ ] Are active, monitoring, resolved, and historical states structurally and verbally distinct? (P5)
- [ ] Are incident updates and resolution times preserved in a plain chronology? (P5)
- [ ] Are loading, empty, stale-data, degraded, error, and simultaneous-incident states handled explicitly? (P1, P5, P6)
- [ ] Are errors, permissions, security, risk, and user-action statements literal? (P5, P6)
- [ ] Is the result free of prohibited pottery imagery, colors, decoration, and metaphors?

## Confidence and unresolved gaps

The profile is **provisional** because it derives from structured observations rather than direct inspection. Confidence is high for P1–P6 within the described collection. Exact palette, measurements, type characteristics, interaction behavior, motion, and technical implementation are not established and remain open. Direct images, dimensions, material views, and use observations would be the smallest useful additions for refining the physical-source analysis, but they are not required to use this bounded handoff.

The downstream handoff begins at **Implementation rules**.

## Boundary audit

- Read: `task.md`, `taste-extractor/SKILL.md`, and `taste-extractor/references/taste-profile.md`.
- Access outside the current directory: None.
- Files written or modified: None.