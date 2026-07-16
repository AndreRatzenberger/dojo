# Voice handoff — password recovery

## Source and access

- **Source:** Three excerpts from one fictional essay collection, plus collection-level voice observations.
- **Source medium:** Literary prose.
- **Downstream target:** Password-recovery microcopy for a calm financial app.
- **Access:** All supplied text was inspected.
- **Unavailable:** Broader collection context, dialogue, longer paragraph transitions, and product-state examples.

## Taste thesis

A calm, concrete voice that states reality plainly, permits one restrained humanizing turn, and closes with dry composure rather than emotional display or flourish. **[T1–T5]**

## Evidence inventory

| Axis | Evidence and observation |
|---|---|
| Syntax | **P1:** “The vents lifted one reluctant inch.” Short declarative clauses alternate literal reporting with restrained personification. |
| Cadence | **P1:** “A pipe coughed in the wall.” **P3:** “The apology arrived Thursday…” Plain setup precedes a slightly angled final beat. |
| Diction | **P2:** “seven boxes”; **P3:** “Tuesday… Thursday.” Concrete nouns, counts, and time markers carry meaning. |
| Imagery | **P1–P3:** Physical actions and ordinary objects anchor each passage; imagery remains small-scale and observable. |
| Point of view | **P2:** “I had completed none of them…” First person appears without confession or heightened self-analysis. |
| Narrative distance | **P2:** Failure is reported with measured detachment, then lightly reframed. |
| Humor | **P2:** “which at least made the page visually coherent.” The joke arrives late, dry, and without emphasis. |
| Omission | Across **P1–P3**, emotional labels and explanations of how the reader should feel are absent. |
| Paragraph movement | Collection note: paragraphs end on a small reversal rather than an exclamation; **P2** and **P3** demonstrate this late turn. |
| Emotional temperature | Across **P1–P3**, inconvenience and awkwardness remain cool, humane, and unalarmed. |

## Taste trace

| ID | Source evidence | Observation | Inferred principle | Confidence | Downstream consequence |
|---|---|---|---|---|---|
| **T1** | P1, “vents lifted…”; collection note on alternating observation and personification | Literal description is followed by one modest human-like quality. | Humanize sparingly after establishing the fact. | High | State the recovery status first; allow at most one gentle turn in low-stakes supporting text. |
| **T2** | P2, “seven boxes”; P3, weekday sequence; collection note on concrete nouns | Counts, objects, and times replace abstraction. | Concrete information creates calm. | High | Name the action, destination, time limit, and next step when known. |
| **T3** | P2’s final clause; P3’s final clause; collection note on late, dry humor | Humor follows the useful information and stays understated. | Wit is a quiet afterbeat, never the payload. | High | Use dry warmth only after instructions, and never in errors, warnings, or security decisions. |
| **T4** | P1–P3; collection note that emotional labels are rare | Feeling is implied through events rather than named or amplified. | Emotional restraint communicates respect. | High | Avoid telling users to relax, assigning emotions, or dramatizing failure. |
| **T5** | Collection note on small reversals; P2 and P3 endings | Endings slightly reframe the setup without spectacle. | Close with a modest shift toward orientation or progress. | High | End low-stakes guidance with the next useful fact, not celebration, suspense, or an exclamation. |
| **T6** | P1–P3, predominantly compact declarative sentences | Clauses are short and legible, with controlled variation. | Plain syntax should carry most of the voice. | High | Prefer direct sentences and familiar verbs; vary rhythm without reproducing source sentence patterns. |

## Transfer layers

### Source content — never transfer

Do not reuse story facts, characters, distinctive phrases, greenhouse imagery, domestic objects, weekday sequences, jokes, metaphors, or recognizable sentence constructions from the excerpts.

### Surface manifestations — adapt selectively

Short declarations, concrete nouns, restrained personification, delayed dry humor, and understated endings may be adapted only when they improve comprehension and trust. **[T1–T3, T5–T6]**

### Portable principles — preserve

- Fact before personality. **[T1]**
- Concrete orientation over abstraction. **[T2]**
- Warmth as a quiet secondary beat. **[T3]**
- Emotional restraint without coldness. **[T4]**
- End on useful forward movement. **[T5]**
- Plain syntax with controlled rhythm. **[T6]**

## Productive tensions

- Human, not chatty. **[T1, T4]**
- Dry, not flippant. **[T3]**
- Calm, not vague. **[T2, T4]**
- Concise, not abrupt. **[T5, T6]**
- Distinctive, not literary. **[T1, T6]**
- Reassuring through clarity, not promises. **[T2, T4]**

## Target invariants

1. Accessibility, correctness, security, and operational clarity outrank stylistic fidelity.
2. Errors, identity checks, consent, fees, permissions, security conditions, risk, time limits, delivery channels, and recovery outcomes must remain literal and unambiguous.
3. Never imply that recovery succeeded, an account exists, or a message was delivered unless the system confirms it.
4. Do not reveal whether an entered identifier belongs to an account when enumeration resistance is required.
5. Never joke about blocked access, fraud, lost funds, identity, security, or user mistakes. **[T3–T4]**
6. Every state must provide a clear next step or truthful stopping condition. **[T2, T5]**

## Degrees of freedom

The producing agent may vary sentence length, button labels, information order, and the amount of low-stakes warmth according to screen size and recovery state. Personification and humor are optional, never quotas. **[T1, T3, T6]**

## Translation

| Principle | Source manifestation | Target-medium decision | Literal copy to avoid |
|---|---|---|---|
| **T1** | One restrained personifying turn after observation | Put factual status first; reserve a subtle human touch for optional helper text | Source imagery, objects, or anthropomorphic security behavior |
| **T2** | Concrete objects, counts, and times | Specify what users should do, where information was sent, and when it expires—only when verified | Invented precision or decorative detail |
| **T3** | Late, dry humor | Permit a quiet afterbeat only in reversible, low-stakes guidance | Jokes in errors, lockouts, warnings, or identity checks |
| **T4** | Rare emotional labeling | Acknowledge inconvenience without naming the user’s feelings | “Don’t worry,” forced empathy, urgency, or blame |
| **T5** | Small closing reversal | Close with the next step or a modest orientation toward progress | Punchlines, triumph, suspense, and exclamation marks |
| **T6** | Compact declarative cadence | Use familiar verbs, short clauses, and scannable hierarchy | Mimicking the excerpts’ exact sentence shapes |

## Production rules

- Lead with the state or required action. **[T1, T2]**
- Put the most useful noun and verb early. **[T2, T6]**
- Use one idea per sentence where security or recovery behavior is involved. **[T6]**
- Explain delays, expiration, retry limits, and alternative routes concretely when confirmed. **[T2]**
- Let clarity provide reassurance; do not promise safety or success beyond known facts. **[T2, T4]**
- Keep personality out of headings, buttons, error causes, and security notices. **[T3]**
- If warmth is appropriate, place it after the operational instruction and keep it removable without loss of meaning. **[T1, T3]**
- End with a next step, fallback, or truthful status. **[T5]**

## Production sequence

1. Identify the exact recovery state and verified system facts.
2. Draft literal status, instruction, action label, and fallback.
3. Check privacy, enumeration, security, accessibility, and legal constraints.
4. Simplify into concrete nouns and familiar verbs. **[T2, T6]**
5. Add restrained warmth only in low-stakes supporting copy. **[T1, T3]**
6. Finish on practical forward movement. **[T5]**
7. Remove any stylistic element that weakens clarity or trust.

## Downstream prompt

> Write password-recovery microcopy for a calm financial app. Use a plain, concrete, emotionally restrained voice: establish the verified fact first, name the action and next step precisely, and use short, familiar sentences. A subtle humanizing turn may appear once in low-stakes helper text, but it must remain optional. Dry humor may follow useful information only when the state is harmless and reversible; never use it for errors, identity, consent, fees, security, permissions, risk, lockouts, fraud, or access to funds. End with practical orientation rather than celebration or an exclamation. Do not copy any source story facts, phrases, imagery, objects, jokes, or sentence structures. Accessibility, correctness, security, and operational clarity outrank voice fidelity. Do not expose account existence or claim unverified delivery or success. Provide copy by UI element and state, plus a plain-language rationale referencing principles T1–T6.

## Rejection tests

Reject the draft if it:

- Could conceal or soften a security condition.
- Uses whimsy as the main voice.
- Makes a joke before the user understands what happened.
- Labels the user’s emotions or tells them how to feel.
- Sounds urgent without an actual deadline or risk.
- Uses decorative metaphor where concrete status is available.
- Mimics a supplied passage’s content, imagery, punchline, or syntax.
- Ends with applause, suspense, or an exclamation instead of a next step.
- Omits a fallback from a blocked or delayed state.

## Yes/no validation checks

- [ ] Does every screen state lead with a verified fact or clear action?
- [ ] Are identity, security, permissions, risk, fees, consent, and errors literal?
- [ ] Does the copy avoid revealing whether an account exists where required?
- [ ] Are delivery, timing, and success claims supported by system state?
- [ ] Is every actionable state paired with a next step or fallback?
- [ ] Is any humor confined to harmless, low-stakes supporting text?
- [ ] Can all personality be removed without changing operational meaning?
- [ ] Are emotional labels, blame, false reassurance, and unnecessary urgency absent?
- [ ] Are source content, distinctive imagery, and sentence structures absent?
- [ ] Do accessibility, correctness, security, and clarity prevail over style?

## Confidence and gaps

Confidence is high for cadence, diction, humor, omission, paragraph movement, and emotional temperature because these are both demonstrated and explicitly summarized. Point-of-view transfer is intentionally limited because product microcopy does not need the collection’s narrative stance. Longer-form transitions, dialogue behavior, and actual recovery states remain unestablished; the producing agent should derive those from product requirements, not from this profile.

**Downstream handoff begins:** “Target invariants.”

**Boundary audit:** Read only `task.md`, `taste-extractor/SKILL.md`, and `taste-extractor/references/taste-profile.md` within the current directory. No files were created, changed, or written.