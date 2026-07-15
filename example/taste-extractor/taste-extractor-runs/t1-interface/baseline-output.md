# T1 interface taste extraction

## Scope boundary

- Input: a verbal description of an existing desktop operations dashboard.
- Output: a reusable taste contract for a separate agent.
- Explicit exclusion: no alert-configuration panel layout, component tree, field set, copy set, or interaction flow is designed here.
- Evidence policy: source facts are separated from derived rules and unresolved choices.

## Observations

### Direct source evidence

1. The product is a desktop operations dashboard.
2. Layout follows a strict twelve-column grid.
3. The base surface is charcoal.
4. Corners are near-square.
5. Boundaries are expressed with hairline dividers.
6. Numerals are monospaced.
7. Neon lime is reserved for live values and successful state changes.
8. Errors are represented by a narrow vermilion strip, not a filled card.
9. Labels are terse nouns.
10. Tables are dense and do not use zebra striping.
11. Controls snap into place in approximately 120 milliseconds.
12. Motion has no bounce.
13. The interface uses no blur, gradients, or decorative illustration.
14. Empty space separates systems, not individual rows.

### Salient pattern clusters

- **Structural precision:** twelve-column discipline, near-square geometry, and hairline dividers make alignment and boundaries do most of the compositional work.
- **Signal scarcity:** bright color is not decoration or branding spread across the surface. It carries a small number of operational meanings.
- **Dense calm:** information is compact, but density is controlled through alignment and dividers rather than alternating row fills or generous row-by-row whitespace.
- **Mechanical response:** controls move quickly and settle directly. The motion vocabulary resembles an instrument changing state, not a soft consumer interface reacting playfully.
- **Low-ornament authority:** there are no atmospheric effects or illustrative flourishes. The interface earns character from proportion, rhythm, typography, and state behavior.
- **System-first grouping:** spacing communicates boundaries between subsystems. Items within a system remain tightly coupled.

## Derivation trace

The following is a compact rationale record, not additional source evidence.

| Observation | Abstraction | Reusable implication |
|---|---|---|
| Strict twelve-column grid | Geometry is a governing system, not a loose guide | New work should visibly share column starts, spans, baselines, and edges with surrounding product surfaces |
| Charcoal base plus hairline dividers | Hierarchy is low-amplitude at rest | Prefer boundaries and alignment over shadows, floating cards, or large tonal jumps |
| Near-square corners | The product favors engineered over soft geometry | Keep radii restrained and consistent; avoid pill-heavy or rounded-card language |
| Lime only for live/success | Attention is budgeted | A neutral default state is essential; lime cannot become a general accent, selection color, or decorative highlight |
| Vermilion error strip instead of filled error card | Failure should be unmistakable but spatially contained | Mark the affected region with a slim edge signal and concise status rather than flooding its surface |
| Terse noun labels | Copy behaves like instrumentation | Name entities, states, and parameters directly; remove conversational prompts where a precise noun works |
| Dense, non-zebra tables | Repetition is carried by rhythm | Use consistent baselines and dividers; avoid alternating backgrounds as a substitute for structure |
| Roughly 120 ms, no bounce | State changes are immediate and deterministic | Transitions should be short, direct, and settled; avoid overshoot, spring, elastic, or theatrical easing |
| No blur, gradients, illustration | Ornament is considered interference | Build distinction from layout, typography, rules, and semantic signals only |
| Space between systems, not rows | Whitespace has architectural meaning | Use larger gaps at conceptual boundaries and compressed cadence inside each group |

## Taste abstractions

### Core character

**A disciplined operational instrument: compact, low-noise, exact, and selectively electric.**

The interface should feel as though every visible distinction has a job. Its default posture is quiet charcoal structure. It becomes vivid only when the system is live, a change has succeeded, or a fault demands attention.

### Six governing principles

1. **Grid before component.** Start with the shared column system and let components inherit its geometry.
2. **Neutral until meaningful.** Most of the interface should remain chromatically quiet so state color retains force.
3. **Density through order.** Compactness is acceptable when alignment, typography, and dividers make scanning reliable.
4. **Boundaries over containers.** Prefer rules and spacing to an accumulation of self-contained cards.
5. **Motion confirms, never performs.** Animation exists to register a state or placement change, then disappears.
6. **Language labels the machine.** Copy is concise, nominal, and operational rather than friendly, promotional, or explanatory by default.

### Taste tensions to preserve

- **Dense, not cramped:** compression must not destroy scan paths.
- **Vivid, not colorful:** lime and vermilion matter because nearly everything else is restrained.
- **Severe, not hostile:** hard geometry and terse language should communicate precision, not punishment.
- **Fast, not abrupt:** approximately 120 ms should register as responsive while still making the state change perceivable.
- **Minimal, not empty:** the dashboard can carry substantial information; minimalism applies to decoration and signal count, not necessarily content count.

## Reusable handoff for the downstream agent

### Style intent

Treat the new surface as an extension of a desktop control system, not as a standalone SaaS card. Establish a precise twelve-column skeleton, keep the resting surface charcoal and neutral, cluster closely related controls into compact systems, and create separation only when the conceptual system changes. Let hairlines, shared edges, and typographic rhythm establish hierarchy. Reserve vivid color for operational truth.

### Layout contract

#### Must

- Resolve the surface onto the existing twelve-column grid.
- Align headings, labels, controls, values, and dividers to recurring column starts and baselines.
- Use larger whitespace intervals only between distinct systems or responsibility areas.
- Keep repeated rows compact and rhythmically consistent.
- Use hairline dividers where row or region boundaries need reinforcement.
- Maintain near-square geometry across containers and controls.

#### Should

- Make the large-scale grouping legible from silhouette and alignment before color is applied.
- Prefer a few structurally meaningful regions over a mosaic of independent cards.
- Let dense repeated content behave like a table even when the controls are editable.
- Keep edges visually deliberate; accidental one-off insets would weaken the grid character.

#### Avoid

- Floating-card layouts with large gutters around every item.
- Row-by-row whitespace that fragments one system into isolated pieces.
- Zebra striping.
- Pills as a default container or label shape.
- Soft, oversized radii.
- Drop shadows used as the primary hierarchy mechanism.

### Surface and color contract

#### Resting state

- Charcoal is the environmental base.
- Build most hierarchy with neutral text levels, line contrast, spacing, and alignment.
- Keep ordinary controls and values neutral unless they satisfy a documented semantic state.

#### Neon lime

- Allowed meanings: a value that is currently live; a successful state change.
- Not allowed as a generic brand accent, decorative rule, ordinary button fill, routine focus ornament, section heading color, or blanket selected state without evidence that selection is also a live state.
- Its scarcity is part of the style. If many unrelated elements are lime at once, the semantic hierarchy has failed.

#### Vermilion

- Use as a narrow strip associated with the affected region when representing an error.
- Do not wash or fill the whole region with vermilion.
- Pair the strip with concise, legible status information so color is not the sole carrier of meaning.

#### Unsupported color semantics

- No additional severity palette is established by the source.
- A configured alert, an active alert, a validation error, and a system failure are not automatically the same semantic state.
- Do not invent amber, blue, or multi-level rainbow severity conventions merely because the downstream artifact concerns alerts. Resolve those semantics from product evidence or keep them neutral.

### Typography and language contract

- Use monospaced numerals for quantities, thresholds, timestamps, counts, durations, identifiers with numeric structure, and changing numeric values.
- Preserve stable digit widths so changing values do not disturb alignment.
- Use terse noun labels wherever the meaning remains unambiguous.
- Prefer labels such as entity or parameter names over conversational instructions.
- Keep helper prose exceptional and subordinate. When explanation is necessary for safety or comprehension, precision outranks forced terseness.
- Do not infer that all text must be monospaced; only numeral treatment is established by the source.

### Density contract

- Repeated items belong to a compact scan field.
- Establish row identity through alignment, consistent cadence, and hairlines rather than alternating fills.
- Keep controls in repeated rows dimensionally consistent.
- Allow meaningful whitespace at a system boundary, then return to the compact internal rhythm.
- Do not use oversized headings or generous card padding to create hierarchy that the grid should provide.

### Motion contract

- Target approximately 120 ms for control placement and state-change transitions.
- Motion should read as a direct snap into the resolved state.
- No bounce, overshoot, spring, elastic response, or ornamental choreography.
- No blur-based transitions.
- Do not animate merely to make a static hierarchy feel more interesting.
- Exact easing is unresolved; choose a direct, non-theatrical curve consistent with the existing product rather than inventing a signature motion style.

### State grammar

| State class | Visual posture | Constraint |
|---|---|---|
| Rest/default | Neutral charcoal hierarchy | Must remain legible without semantic accent color |
| Live value | Neon lime on the live value or its minimal state marker | Do not spread lime across the containing region |
| Successful state change | Brief or otherwise product-consistent lime confirmation | Persistence and exact duration are not specified |
| Error | Narrow vermilion strip plus concise status | No full-card error fill |
| Disabled, pending, inactive, warning, selected | Not defined by source | Derive from existing product evidence; do not misuse lime or vermilion by assumption |

### Component-shape guidance without panel design

- A component should look integrated into the grid, not dropped onto it.
- A boundary should be as light as it can be while remaining scannable.
- Repeated components should share measurements and baselines strictly.
- State decoration should occupy the smallest area that communicates the state reliably.
- Default controls should not compete visually with live data.
- Decorative illustration, gradients, frosted glass, glow haze, and blur are outside the vocabulary.

## Decision rules for ambiguous moments

1. If a choice improves alignment but adds no ornament, it is probably compatible.
2. If a choice makes every item more individually prominent, it is probably incompatible; the source prioritizes systems over isolated rows.
3. If a bright color does not communicate live, success, or error semantics, remove it.
4. If hierarchy still works in grayscale, the structural logic is likely sound.
5. If a transition calls attention to itself after the state is understood, shorten or remove it.
6. If copy sounds like a sentence from a friendly assistant, test whether a precise noun can replace it.
7. If density becomes hard to scan, repair alignment, cadence, and dividers before adding alternating fills or large row gaps.
8. If an alert-related semantic is not covered by the source, mark it unresolved rather than borrowing a conventional color palette uncritically.

## Anti-pattern inventory

- Lime primary-action buttons used everywhere.
- Lime section headings or decorative underlines.
- Full vermilion error cards.
- Amber warning fills invented without product evidence.
- Rounded pastel status pills.
- Elevated cards with shadows on a soft background.
- Alternating row backgrounds.
- Large vertical gaps between every setting.
- Gradient strokes, glow effects, glass blur, or atmospheric overlays.
- Animated springs, bounce, overshoot, or long fades.
- Friendly sentence-case microcopy where a terse operational label would suffice.
- Decorative empty-state artwork.
- Numeric values in proportionally spaced type that visibly shift as they update.
- Local component geometry that ignores the twelve-column structure.

## Unresolved variables

These must not be fabricated from the available evidence:

- Exact charcoal, lime, vermilion, neutral text, and divider color values.
- Exact typefaces, text sizes, weights, tracking, and line heights.
- Exact grid margins, gutters, and column widths.
- Exact corner radius.
- Exact divider thickness and opacity; “hairline” is the reliable instruction.
- Exact control heights, row heights, and spacing increments.
- Exact easing curve for the approximately 120 ms transition.
- Duration or persistence of success indication.
- Focus, hover, disabled, pending, inactive, selection, and warning treatments.
- Responsive behavior outside the stated desktop context.
- Alert severity taxonomy and whether product alerts share the same vermilion semantics as interface errors.
- Iconography rules; decorative illustration is prohibited, but functional icons are neither required nor forbidden by the source.

When possible, the downstream agent should sample these values from the live product or its design tokens. Until then, preserve them as relational constraints rather than false precision.

## Verification checklist

### Structure

- [ ] Every major edge and span can be explained by the twelve-column grid.
- [ ] Larger gaps correspond to real system boundaries.
- [ ] Repeated rows remain compact and share baselines.
- [ ] Dividers and alignment, not shadows or zebra fills, carry the scan structure.
- [ ] Corners remain near-square and consistent.

### Signal

- [ ] The surface is coherent and legible before lime or vermilion is applied.
- [ ] Every lime element can be justified as live or successful.
- [ ] Every vermilion element denotes an actual error.
- [ ] Error color is spatially narrow rather than a filled region.
- [ ] Color is accompanied by readable state information.

### Language and data

- [ ] Labels are terse nouns unless clarity genuinely requires more.
- [ ] Numerals use stable monospaced treatment.
- [ ] Dense content can be scanned by row and column without zebra striping.
- [ ] No invented alert-severity color system has slipped into the artifact.

### Motion and ornament

- [ ] Control transitions settle in roughly 120 ms.
- [ ] No transition bounces, overshoots, blurs, or performs decoratively.
- [ ] There are no gradients, blur effects, or decorative illustrations.
- [ ] No ornamental device competes with operational state.

### Final gestalt

- [ ] The artifact reads as part of an operational instrument rather than a generic consumer SaaS form.
- [ ] It feels dense but ordered, severe but usable, vivid only when the system has something meaningful to say.

## Result

Reusable taste fingerprint:

> **Twelve-column operational precision on charcoal. Near-square geometry, hairline structure, terse noun labels, and monospaced changing numerals create a dense neutral field. Empty space marks system boundaries rather than individual rows. Neon lime is scarce and semantic—live or successfully changed—while errors occupy only a narrow vermilion strip. Controls resolve in about 120 ms with direct, non-bouncing motion. No zebra stripes, gradients, blur, or decorative illustration.**

Transfer criterion: a downstream design is faithful when its hierarchy survives without accent color, its geometry visibly belongs to the shared grid, and every moment of vividness corresponds to a specific operational truth.
