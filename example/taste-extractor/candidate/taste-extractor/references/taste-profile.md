# Taste Profile Reference

## Medium Axes

Use only axes supported by the accessible source. Add an axis when the medium
requires it; do not force every source into every row.

| Medium | Useful observation axes |
|---|---|
| Interface or product | composition, hierarchy, grid, typography, color, density, components, interaction, feedback, motion, empty/error states, language |
| Prose | syntax, cadence, diction, imagery, point of view, narrative distance, humor, omission, paragraph movement, emotional temperature |
| Still image or illustration | framing, focal hierarchy, palette, light, contrast, mark, texture, shape grammar, depth, negative space, repetition |
| Film, animation, or video | framing, camera behavior, blocking, edit rhythm, transition grammar, motion, typography, sound, silence, temporal arc |
| Music or audio | tempo, meter, rhythm, timbre, register, harmony, dynamics, density, arrangement, repetition, space, tension and release |
| Physical object or craft | form, proportion, material, finish, joinery, tolerance, wear, repair, affordance, tactility, collection rhythm |
| Architecture or place | approach, threshold, sequence, scale, light, material, circulation, compression, release, acoustics, social behavior |
| Service, ritual, or brand | pacing, roles, boundaries, language, feedback, recovery, ceremony, surprise, trust, emotional arc |

## Evidence Coordinates

Prefer coordinates another reviewer can revisit:

- prose: short quote plus paragraph or line position
- interface: surface, component, state, and interaction
- image: region, subject relationship, and visual feature
- video: timestamp or shot sequence
- audio: timestamp, section, instrument, or sonic event
- object: part, material, construction detail, or use state
- experience: step, transition, feedback moment, or recovery path

Use the smallest source fragment needed. Do not reproduce long passages or a
large fraction of the source.

## Taste Trace Template

| Source evidence | Observation | Inferred principle | Confidence | Downstream consequence |
|---|---|---|---|---|
| `<coordinate and small fragment>` | `<what is directly present>` | `<portable relationship>` | high / medium / low | `<rule for the target>` |

## Profile Template

```markdown
# Taste profile — <source>

## Source and access
- Source:
- Source medium:
- Downstream target:
- Inspected:
- Unavailable:

## Taste thesis
<one sentence>

## Taste trace
<evidence rows>

## Transfer layers
### Source content — do not transfer
### Surface manifestations — adapt deliberately
### Portable principles — preserve

## Signature principles
1. ...

## Productive tensions
- ..., not ...

## Invariants
- ...

## Degrees of freedom
- ...

## Translation
<principle-to-target table>

## Anti-patterns and originality guardrails
- ...

## Production sequence
1. ...

## Downstream prompt
<standalone prompt for the producing agent>

## Validation checks
- [ ] ...

## Unknowns and confidence
- ...
```

## Medium-Aware Intake When Evidence Is Missing

Ask for enough material to observe variation and sequence, not only a single
hero fragment:

- interfaces: representative screens plus normal, loading, empty, error, and
  interaction states
- prose: several passages including transitions and endings
- images: multiple representative works or high-resolution regions
- video: ordered clips or timestamped frames plus motion and sound notes
- audio: playable excerpts or timestamped listening notes
- objects and places: multiple views, scale, material, construction, and use
  observations
- services and rituals: steps, roles, feedback, exceptions, and recovery

Until that evidence is supplied, return the intake request and stop.
