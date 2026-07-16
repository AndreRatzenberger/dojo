# Held-out custody — `taste-extractor`

These scenarios are kept held out until the candidate skill is frozen. Run
each once in a fresh context. Supply the runner prompt verbatim and do not
provide any other source material.

## Holdout 1 — Choreography to decision protocol

### Exact runner prompt

```text
Use `taste-extractor` on the complete evidence packet below. The source is a
seven-minute contemporary dance duet, and the destination is a repeatable
45-minute architecture-decision meeting for 5–7 people. Produce a taste
profile and an implementation-ready handoff that a meeting facilitator can
use. The result should preserve the source's portable taste without turning
the meeting into dance, theatre, or a themed imitation.

Do not search for or assume any source beyond this packet. Be explicit about
what is directly observed, what is inferred, what should remain invariant,
and what may adapt. Include concrete yes/no checks for the implemented meeting
format.

EVIDENCE PACKET

- 00:00–00:18 — A bare stage, cool even light, no props. Both performers stand
  far apart on diagonals. Nothing moves until one performer shifts weight; the
  other answers two beats later with a related but non-identical shift.
- 00:18–01:35 — Short phrases pass back and forth. The receiver never repeats
  a phrase exactly: scale, direction, or speed changes, while its underlying
  rhythm remains recognizable. Neither performer dominates for more than
  three exchanges.
- 01:35–02:20 — The duet reaches its first exact unison. It lasts only eight
  seconds and is followed by a long shared pause. Audience attention is drawn
  to the agreement because it is rare, not because it is enlarged.
- 02:20–03:55 — The dancers repeatedly approach contact, stop just short, and
  redirect. Tension accumulates through withheld contact. Music is sparse dry
  clicks with irregular gaps; movement sometimes continues through the gaps.
- 03:55–04:35 — A planned catch arrives late and visibly destabilizes both
  performers. They recover without restarting or disguising the disruption;
  the recovery becomes the next phrase and restores balance gradually.
- 04:35–05:50 — The densest section layers fast individual phrases around a
  slow shared walking path. Complexity sits on top of one legible common
  direction. A single sustained tone replaces the clicks at the peak.
- 05:50–06:35 — Material from the opening returns with roles reversed. It is
  recognizable but compressed: the initial 18-second wait becomes six seconds.
- 06:35–07:00 — Both performers stop at the same time but in separate places.
  The sound cuts first; they remain still for four seconds, exhale audibly,
  and leave by different routes. There is no blackout or bow within the piece.
- Rehearsal note — The choreographer rejects decorative gestures that do not
  alter timing, relation, or balance. She permits changes in exact steps when
  the venue changes, but preserves the exchange structure, rare unison,
  visible recovery, and quiet ending.
```

### Observable yes/no criteria

1. Does the response keep literal stage events separate from inferred taste
   principles and attach every major principle to one or more timestamped
   observations?
2. Does it extract temporal and relational qualities—exchange, delayed
   response, rare convergence, accumulated tension, visible recovery, layered
   complexity, return, and closure—rather than reducing the source to a cool,
   sparse visual mood?
3. Does it distinguish evidence-backed invariants from adaptable choices,
   including the rehearsal note's explicit boundary between structure and
   venue-dependent steps?
4. Does the handoff specify a usable 45-minute meeting sequence with roles,
   timing, exchange rules, convergence/decision moments, disruption recovery,
   and a clear ending that another facilitator could run without interpretation
   work?
5. Does it prohibit literal dance/theatre imitation and provide observable
   yes/no validation checks that test the retained principles rather than
   source-themed decoration?

## Holdout 2 — Printed field-guide series to an IVR

### Exact runner prompt

```text
Use `taste-extractor` on the complete evidence packet below. It describes a
small family of printed field guides plus one limited edition. Extract the
portable taste and hand it off for implementation as the interactive voice
response (IVR) system for a regional public-transport disruption line. Callers
must be able to hear current disruption summaries, check a route, repeat or
slow information, and reach a human during staffed hours.

Do not search for or assume any artifacts beyond this packet. The IVR should
feel related in taste, not copied in subject matter or dressed up with print,
nature, or page-turn gimmicks. Separate observations from inference, explain
how recurrence affects confidence, distinguish invariants from adaptations,
and finish with concrete yes/no checks an IVR reviewer can apply.

EVIDENCE PACKET

CORE SERIES — three pocket guides

- Each closed guide is 105 × 165 mm, 64–80 pages, thread sewn, and printed on
  warm uncoated stock. Covers use a matte charcoal field, a lowercase title,
  one small line drawing, and one saturated accent color unique to that volume.
- Every normal spread follows the same grammar: the left page carries one
  annotated line drawing with numbered callouts; the right page carries a
  70–110 word entry, a blunt two-to-four-word heading, and a tiny location/index
  code. The drawing and entry can each stand alone, but their numbering links
  them precisely.
- Outer margins are generous. Information grows denser toward the gutter,
  where a narrow vertical index gives section, confidence level, and cross-
  references. No paragraph runs across a full page width.
- Section openings remove almost everything: accent-color paper, one black
  heading, one sentence, no illustration. The following spread resumes the
  normal grammar. The pause is brief and functional.
- Uncertain identifications are not hidden. A hollow callout number and the
  phrase “compare before deciding” mark ambiguity; the entry then names the
  two most useful discriminators. Confirmed facts use solid callouts.
- Navigation is redundant but restrained: colored fore-edge marks identify
  sections when the book is closed, while page numbers and the gutter index do
  the same job when open. There are no decorative tabs or icons.
- All three books end with a two-page quick index that favors common-language
  lookup over specialist taxonomy. Technical names remain available as a
  secondary line.

LIMITED FESTIVAL EDITION — one documented variant

- A fourth guide made for a festival keeps the size and internal spread
  grammar but adds a silver-foil cover, a fluorescent wraparound band, and one
  fold-out panoramic illustration. The production note calls these “event-only
  signals, not series rules.” No other guide uses foil, a band, or a fold-out.

EDITOR'S NOTE

- Exact accent colors, page counts, and subjects may change. The editor will
  not approve a volume that loses paired overview/detail, explicit uncertainty,
  compact headings, redundant navigation, short sparse pauses, or
  common-language-first lookup.
```

### Observable yes/no criteria

1. Does the response clearly separate printed-guide content and material
   features from inferred portable principles, with traceable references to
   specific evidence rather than unsupported aesthetic adjectives?
2. Does it reason across the artifact family—treating repeated core-series
   patterns and the editor's note as stronger evidence than the single
   festival variant—and avoid promoting foil, fluorescent wrapping, or the
   fold-out into invariants?
3. Does it state defensible invariants and adaptable qualities, including how
   paired overview/detail, explicit uncertainty, redundant navigation, sparse
   pauses, and common-language-first lookup survive a move from print to audio?
4. Does the handoff turn those principles into an implementable IVR structure,
   covering opening summary/detail, compact prompts, route lookup, uncertainty,
   repeat/slow controls, navigation recovery, and human escalation without
   relying on visual or print mechanics?
5. Does it set originality boundaries against botanical vocabulary, paper or
   page-turn effects, and other literal theming, then supply observable yes/no
   validation checks for the finished call flow?
