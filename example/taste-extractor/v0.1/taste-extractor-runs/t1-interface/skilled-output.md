# Taste profile — desktop operations dashboard

## Source and access

- Source artifact: a desktop operations dashboard, represented by structured source observations.
- Source medium: desktop interface/product.
- Downstream target: a new alert-configuration panel in the same product, to be designed by another agent.
- Inspected: the supplied description of composition, grid, geometry, dividers, numeric typography, semantic color, error treatment, labeling, tables, control motion, excluded effects, and whitespace behavior.
- Unavailable: rendered screens; exact color, spacing, type, border, and control tokens; component dimensions; data and labels; hover, focus, disabled, loading, and empty-state examples; responsive behavior; accessibility specifications.
- Constraint: extract a reusable style handoff only. Do not design the alert panel or reuse literal source content.
- Fidelity: preserve the product's governing relationships and explicit invariants; do not invent precision where the evidence stops.

## Observations

- Composition is locked to a strict twelve-column grid over a charcoal field.
- Shape language is almost square, with hairline boundaries rather than soft cards.
- Numerals are monospaced.
- Neon lime has a narrow semantic role: live values and successful state changes.
- Error signaling is a narrow vermilion strip, not a filled error surface.
- Labels are terse nouns.
- Tables carry high information density without zebra striping.
- Controls settle in roughly 120 milliseconds, without bounce.
- Blur, gradients, and decorative illustration are absent.
- Empty space separates systems at the macro level; it does not loosen individual rows.

No observation beyond these supplied facts is treated as source evidence.

## Taste thesis

Operational severity is made legible through a rigid, dense, low-affect system in which structure carries hierarchy and scarce color and motion are reserved for changes that matter.

## Taste trace

| Source evidence | Observation | Inferred principle | Confidence | Downstream consequence |
|---|---|---|---|---|
| Global composition — “strict twelve-column grid on charcoal” | The surface uses a fixed column system and dark ground. | Structural alignment, not ornament, is the primary organizer. | High | Place every panel region and control group on the existing twelve-column logic; use the product's charcoal token rather than inventing a new dark palette. |
| Component geometry — “near-square corners, hairline dividers” | Containers are minimally rounded and boundaries are visually thin. | The interface should feel planar, precise, and mechanically assembled. | High | Keep geometry nearly square and use fine separation; do not introduce soft, floating card language. |
| Numeric typography — “monospaced numerals” | Numeric values have stable character widths. | Scannability and operational comparison outrank typographic warmth. | High | Use the established monospaced numeral treatment wherever the target exposes values, thresholds, counts, durations, or other numbers; do not infer that all copy is monospaced. |
| Live/success states — “Neon lime appears only on live values and successful state changes” | Lime is scarce and semantically restricted. | Bright color is a truth-bearing signal, not a decorative accent. | High | Reserve lime for genuinely live values or confirmed successful transitions; keep labels, borders, focus decoration, and inactive controls out of lime unless the product's accessibility system explicitly requires otherwise. |
| Error state — “errors use a narrow vermilion strip rather than filled cards” | Error color occupies a small linear region instead of flooding a container. | Failure should be unmistakable but spatially disciplined. | High | Express error state with the established narrow vermilion edge/strip pattern plus accessible text or icon semantics; avoid large red fills. |
| Interface language — “Labels are terse nouns” | Labels are short nominal terms rather than conversational instructions. | The product speaks like instrumentation: compressed, neutral, and direct. | High | Name controls and groups with the shortest unambiguous noun labels; place essential explanation in secondary help rather than inflating labels. |
| Table rhythm — “dense but never zebra-striped” | Rows are closely packed and do not alternate background colors. | Density is resolved through alignment and hierarchy, not decorative banding. | High | If repeated structures occur, organize them with grid, type, and hairline rules; never add zebra striping as a shortcut to readability. |
| Control motion — “snap into place in roughly 120 milliseconds with no bounce” | Transitions are brief, direct, and non-elastic. | Interaction should feel mechanical and conclusive rather than playful. | High | Use approximately 120 ms for relevant settling transitions, following existing motion tokens; no overshoot, spring, bounce, or ornamental delay. |
| Surface effects — “no bounce, blur, gradients, or decorative illustration” | Atmospheric and decorative effects are deliberately excluded. | Visual authority comes from reduction and exactness. | High | Keep surfaces flat and crisp; do not compensate for sparse styling with glow, gradient, blur, shadow theater, mascots, or decoration. |
| Spacing — “Empty space is used to separate systems, not individual rows” | Whitespace is concentrated between major groups while row spacing stays compact. | Macro separation and micro density coexist. | High | Spend whitespace between distinct functional systems; maintain tight, regular rhythm inside each system instead of isolating every field or row. |

## Transfer layers

### Source content — do not transfer

- Existing operation names, data values, labels, table columns, alert rules, or domain-specific phrases.
- Any literal arrangement of an existing dashboard screen or table.
- Logos, identifiers, or exact compositions that are not needed to preserve the system's character.

No literal source content was supplied, so none should be invented as a stylistic proxy.

### Surface manifestations — adapt deliberately

- Twelve-column alignment on charcoal.
- Near-square geometry and hairline dividers.
- Monospaced numerals, but only where numerical scanning benefits.
- Neon lime for live/success semantics and vermilion strips for errors.
- Dense, non-zebra repeated structures.
- Roughly 120 ms direct motion.
- Flat surfaces without blur, gradients, bounce, or illustration.
- Whitespace at system boundaries rather than between every row.

Because source and target are interfaces in the same product, these manifestations should normally map through existing design tokens. Their exact values must be retrieved from the product rather than reverse-engineered from adjectives.

### Portable principles — preserve

- Structure before decoration.
- Semantic scarcity: a high-intensity cue earns attention by being rare and truthful.
- Macro breathing room with micro-level density.
- Mechanical, conclusive feedback.
- Instrument-like language.
- Localized severity rather than theatrical alarm surfaces.
- Crisp flatness and numerical scanability.

## Signature principles

1. **Structure carries hierarchy.** The grid, alignment, dividers, and grouping do the organizational work; visual effects do not.
2. **Signal color must tell the truth.** Lime means live or successfully changed, while vermilion marks failure. Neither is ambient branding.
3. **Dense within, open between.** Related controls remain compact; meaningful subsystem boundaries receive the whitespace.
4. **Feedback is mechanical.** Controls resolve quickly, directly, and without personality motion.
5. **Language behaves like telemetry.** Labels are terse nouns, with elaboration kept subordinate and only where necessary for correctness.
6. **Severity is narrow but unmistakable.** Error treatment is localized and sharp, not a filled-card spectacle.
7. **Precision is selective.** Monospaced numerals support comparison; other typography and exact tokens remain governed by the existing product system.

## Productive tensions

- Dense, not cramped.
- Severe, not theatrical.
- Immediate, not playful.
- Sparse in color, not sparse in information.
- Rigid, not visually noisy.
- Flat, not featureless.
- Terse, not cryptic.
- Separated by system, not fragmented into cards.

## Invariants

- Honor the strict twelve-column grid.
- Use the existing charcoal ground and product tokens; do not invent approximate hex values.
- Preserve near-square geometry and hairline separation.
- Keep individual rows and repeated controls dense and consistently aligned.
- Put meaningful whitespace between major functional systems.
- Use monospaced numerals for numerical data and input where appropriate.
- Reserve neon lime for live values and confirmed successful state changes.
- Represent errors with the established narrow vermilion strip grammar, reinforced by non-color semantics.
- Keep relevant settling transitions around the established roughly 120 ms behavior, with no bounce or overshoot.
- Exclude zebra striping, blur, gradients, and decorative illustration.
- Keep primary labels as terse, unambiguous nouns.

## Degrees of freedom

- The alert panel's information architecture, control types, ordering, and column spans may respond to the actual alert workflow.
- The number and size of functional groups may vary, provided they align to the grid and obey the macro-space/micro-density rule.
- Non-numeric type treatment should use the existing product typography; the evidence does not require monospacing all text.
- Secondary guidance, validation detail, and recovery copy may use longer language where terse labels alone would become ambiguous or unsafe.
- Exact spacing, color, border, focus, and motion tokens should come from the product system.
- Error placement can adapt to the validation scope, as long as the narrow vermilion signal remains localized, clear, and accessible.
- Accessibility and functional correctness may add focus indicators, status text, icons, hit-area padding, or reduced-motion behavior. These should be integrated crisply rather than suppressed for stylistic purity.
- Responsive behavior is open pending evidence; do not extrapolate the desktop grid blindly to smaller surfaces.

## Translation into the alert-configuration target

| Principle | Source manifestation | Target-medium decision | Literal copy to avoid |
|---|---|---|---|
| Structure carries hierarchy | Strict twelve-column grid, hairline dividers | Derive the panel's groups and controls from the existing grid and alignment tokens before styling individual components. | Reusing the dashboard's exact table or screen composition. |
| Signal color tells the truth | Lime only on live values and success | Show lime only when alert data is truly live or a configuration change has completed successfully. | Coloring primary actions, headings, selected tabs, or decoration lime merely for emphasis. |
| Dense within, open between | Dense rows; whitespace separates systems | Keep related configuration elements compact and give separation only to materially different functional groups. | Wrapping every field in its own spaced card or collapsing all groups into an undifferentiated slab. |
| Mechanical feedback | Controls settle in roughly 120 ms, no bounce | Make state transitions brief and direct, and provide immediate unambiguous feedback for control changes. | Spring physics, bounce, staged flourish, or slow easing. |
| Instrument-like language | Terse noun labels | Use concise noun labels and subordinate only the explanation needed to prevent mistakes. | Conversational microcopy, slogans, or verbose instructional labels. |
| Localized severity | Narrow vermilion error strip | Attach a narrow vermilion signal to the affected validation scope and pair it with a readable explanation. | Filling an entire section or card with red, or relying on red alone. |
| Selective precision | Monospaced numerals | Apply stable-width numerals to thresholds, durations, counts, and other comparable numeric values. | Turning all prose into monospace or imitating terminal aesthetics without functional cause. |
| Flat exactness | No blur, gradients, or illustration; near-square corners | Keep component layers crisp, planar, and minimally rounded. | Decorative dashboard cosplay: glows, gradients, glass, shadows, illustrations, or exaggerated techno motifs. |

## Anti-patterns and originality guardrails

- Do not treat neon lime as a general brand accent. Its scarcity is part of the taste.
- Do not create filled red error cards; vermilion should remain a narrow, localized severity cue.
- Do not add rounded floating cards, pills everywhere, soft shadows, glass effects, gradients, blur, glow, or decorative imagery.
- Do not use zebra stripes in repeated content.
- Do not loosen every row to make the interface feel “premium”; whitespace belongs between systems.
- Do not compress labels until meaning, safety, or accessibility is lost. Terse means economical, not opaque.
- Do not apply monospace indiscriminately. Only numerals are explicitly evidenced.
- Do not animate for delight. Motion confirms a state change and then gets out of the way.
- Do not copy an existing dashboard layout, table structure, terminology, data, or exact component composition into the alert panel.
- Do not invent exact hex colors, radii, spacing units, font sizes, or motion curves from this description. Resolve them from existing product tokens.
- Do not turn the style into “cyberpunk operations” costume. The character comes from discipline, semantics, and hierarchy, not genre decoration.

## Production sequence

1. Inventory the alert workflow's required information, actions, state changes, validation failures, and numerical values without styling them.
2. Retrieve the product's actual grid, color, typography, divider, radius, spacing, focus, and motion tokens.
3. Identify functional systems, then establish twelve-column alignment and reserve macro whitespace only between those systems.
4. Set a compact internal rhythm for related controls and repeated structures; establish hierarchy through alignment, type, and hairlines.
5. Apply terse noun labels, adding subordinate help only where correctness requires it.
6. Assign semantic states before color: live/success may receive lime; errors receive the narrow vermilion grammar plus text or icon meaning; ordinary emphasis stays neutral.
7. Apply monospaced numeral treatment only to comparable numeric content.
8. Define direct interaction feedback around the existing roughly 120 ms behavior, including reduced-motion handling; exclude bounce and decorative transitions.
9. Produce normal, changed-success, error, focus, disabled, loading, and empty-state variants using real product tokens.
10. Run the yes/no validation checks below and reject the design if any invariant fails.

## Downstream prompt

Design a new alert-configuration panel for the existing desktop operations product. Preserve its operational character without copying any existing dashboard composition, terminology, data, or component arrangement.

The interface is governed by a strict twelve-column grid on the product's charcoal ground. Structure must carry hierarchy: align everything deliberately, use near-square geometry and hairline dividers, keep related controls dense, and spend whitespace only between distinct functional systems. Use the product's actual tokens rather than inventing colors, radii, spacing, or type values.

Treat vivid color as scarce semantic information. Neon lime is permitted only for genuinely live values or confirmed successful state changes. Errors use the established narrow vermilion strip grammar and must also communicate through accessible text or icon semantics; never fill an entire card or section red. Keep ordinary emphasis neutral.

Use terse, unambiguous noun labels. Put essential explanation in subordinate help only when correctness requires it. Apply monospaced numerals to thresholds, durations, counts, and other comparable numeric values, but do not turn all text into terminal typography. Keep repeated structures dense and never zebra-striped.

Controls should settle in roughly 120 milliseconds using the existing motion token, with direct easing and no bounce, overshoot, or decorative delay. Exclude blur, gradients, glows, glass, decorative illustration, and soft floating-card aesthetics. Accessibility and correctness outrank stylistic fidelity: preserve focus visibility, non-color state meaning, adequate hit areas, legibility, and reduced-motion behavior.

You are free to determine the panel's information architecture, control types, ordering, grouping count, and grid spans from the actual alert workflow. Show normal, focus, disabled, loading, empty, changed-success, and error states. The result should feel severe but not theatrical, dense but not cramped, flat but not featureless, terse but not cryptic, and precise without lapsing into techno costume.

## Validation checks

- [ ] Does every region align to the product's twelve-column system?
- [ ] Are major functional systems separated by whitespace while related rows remain compact?
- [ ] Are boundaries hairline and corners near-square rather than soft or card-like?
- [ ] Is neon lime absent everywhere except truly live values and confirmed successful changes?
- [ ] Are errors expressed with a narrow vermilion signal rather than a filled surface?
- [ ] Can live, success, and error states still be understood without color alone?
- [ ] Are primary labels terse nouns while remaining unambiguous?
- [ ] Are numerals monospaced where stable-width comparison is useful, without forcing monospace onto all prose?
- [ ] Are repeated rows or structures readable without zebra striping?
- [ ] Do relevant transitions settle in roughly 120 ms without bounce, overshoot, or ornamental staging?
- [ ] Are blur, gradients, glow, glass effects, and decorative illustration absent?
- [ ] Does the design use real product tokens rather than guessed exact values?
- [ ] Are focus visibility, hit areas, contrast, status text, and reduced-motion behavior functionally sound?
- [ ] Is the panel's composition original to its workflow rather than copied from an existing dashboard screen?
- [ ] Would removing lime and vermilion leave a coherent structural hierarchy? If not, color is doing too much work.
- [ ] Does the result read as an operational instrument rather than a stylized “ops” costume?

## Unknowns and confidence

- High confidence: grid count, dark ground, near-square geometry, hairline dividers, numeric typography, semantic color restrictions, error-strip treatment, terse labels, table density, absence of zebra striping and decorative effects, motion duration/character, and whitespace hierarchy. Each is explicit in the supplied observations.
- Medium confidence: applying those rules to form controls and alert validation. This is a same-product translation, but no alert-panel source state was shown.
- Unknown: exact token values, non-numeric typography, control dimensions, detailed easing curve, focus/hover/disabled/loading/empty behavior, responsive rules, and the product's accessibility implementation.
- Evidence limitation: the source was available only as structured observations, not as a rendered artifact. The handoff therefore makes no claims about visual details outside that description.
- Resolution path: inspect the existing product's design tokens and representative normal, focus, changed-success, error, disabled, loading, and empty states before production decisions are finalized.

## Result

- Source and access status: desktop operations dashboard; structured source observations inspected, rendered interface unavailable.
- Downstream target: new alert-configuration panel in the same product, produced by another agent.
- Strongest evidence-backed thesis: operational authority comes from rigid structure, dense information, and scarce truth-bearing signals rather than ornament.
- Unresolved evidence gaps: exact product tokens, unshown component and interaction states, responsive behavior, and accessibility implementation.
- Downstream handoff begins at `Production sequence`; the standalone producing-agent brief begins at `Downstream prompt`.
