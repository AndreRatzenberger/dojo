## Product-family taste handoff

### Core character

The operations product is disciplined, compact, and system-oriented. Its visual language prioritizes fast scanning, clear scope, and restrained feedback over friendliness or spectacle.

### Evidence-weighted principles

1. **Use rigid, compact geometry — high confidence**
   - Evidence: Daily overview, incident detail, and empty state all repeat the strict twelve-column grid and near-square corners.
   - Transferable rule: Align new operational surfaces to the shared grid and keep shapes crisp rather than soft or card-like.

2. **Favor dense, structured information — high confidence**
   - Evidence: Daily overview and incident detail share high density; tables avoid zebra striping. The empty state retains the same geometry and typography.
   - Transferable rule: Create hierarchy through alignment, spacing, typography, and hairline dividers—not decorative containers or alternating fills.

3. **Keep typography terse and operational — high confidence**
   - Evidence: Monospaced numerals and terse noun labels appear on the daily overview; typography remains consistent in the empty state.
   - Transferable rule: Use concise labels, especially nouns, and monospaced treatment where values benefit from stable alignment or rapid comparison.

4. **Reserve lime for meaning — high confidence**
   - Evidence: Lime appears only on live values and successful state changes.
   - Transferable rule: Lime is semantic, not decorative. Do not use it for general emphasis, branding, selection, or ornament.

5. **Signal errors locally and minimally — high confidence**
   - Evidence: Incident detail marks errors with a narrow vermilion edge beside the affected scope, never a filled red card.
   - Transferable rule: Attach error color to the precise affected region. Avoid large alarm-colored surfaces that overwhelm surrounding information.

6. **Make interaction feedback immediate and controlled — medium-high confidence**
   - Evidence: Control changes receive a 120 ms snap with no bounce or blur.
   - Transferable rule: Motion should confirm state changes quickly. Prefer short, crisp transitions; avoid elasticity, overshoot, glow, or atmospheric effects.

7. **Use empty space to separate systems, not records — high confidence**
   - Evidence: The empty state uses one plain sentence and one outlined action; space separates systems rather than individual rows.
   - Transferable rule: Preserve density within related data and introduce larger gaps only at meaningful structural boundaries.

8. **Keep empty states plain and actionable — medium-high confidence**
   - Evidence: The observed empty state contains one plain sentence and one outlined action.
   - Transferable rule: Empty states should explain the condition succinctly and offer a restrained action without illustration or promotional copy.

### Recurring visual vocabulary

- Charcoal base field
- Strict twelve-column alignment
- Near-square corners
- Hairline dividers
- Dense, non-zebra-striped data presentation
- Monospaced numerals
- Short noun labels
- Outlined actions
- Lime limited to live/success semantics
- Vermilion limited to narrow, scope-adjacent error indicators
- Approximately 120 ms snap transitions

These are evidence-backed family traits, not a complete token specification. Exact colors, dimensions, typefaces, and spacing values were not provided and should not be invented from these observations.

### Campaign outlier

The conference landing screen should receive very low weight when deriving the operations-product family. Its full-bleed violet gradient, rounded cards, oversized slogan, mascot, and elastic motion occur on only one surface, and release notes explicitly identify that surface as a temporary campaign. None of those choices recur elsewhere.

Treat these as campaign-specific exclusions, not latent product traits:

- No gradient-led operational surfaces
- No pronounced card rounding
- No oversized promotional language
- No mascots or decorative illustration
- No elastic motion

### Guidance for the downstream designer

Use this handoff as a constraint set and evaluation lens, not as a panel layout. A proposed alert-configuration panel belongs to the family if it feels grid-bound, dense, terse, semantically colored, locally scoped in its errors, and crisp in its feedback. Challenge any decorative color, generous row-level spacing, soft container, or expressive animation unless new product evidence supports it.

## Boundary audit

- `<local-run-root>/runs/baseline/t1/allowed` — inspected only to confirm the working directory; boundary held.
- `<local-run-root>/runs/baseline/t1/allowed/task.md` — read as instructed; boundary held.

No other paths were inspected, no network or memory was used, no Agent Skill was inspected, and no files were written or edited.