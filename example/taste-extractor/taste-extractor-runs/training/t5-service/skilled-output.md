# Taste profile — observed check-in ritual

## Source and access

- Source: structured observations in `task.md`
- Source medium: service ritual
- Downstream target: asynchronous onboarding for a collaborative writing app
- Inspected: pacing, requested information, progressive disclosure, exception handling, return behavior, closure
- Unavailable: direct observation, exact language, visual design, accessibility behavior, technical constraints, analytics, and broader edge cases
- Status: provisional where implementation details exceed the supplied observations

## Taste thesis

A calm, restrained onboarding that acknowledges the person, asks only what is immediately necessary, discloses guidance progressively, states delays plainly, and ends as soon as the user chooses what to do next.

## Taste trace

| Source evidence | Observation | Inferred principle | Confidence | Downstream consequence |
|---|---|---|---|---|
| Opening: personal greeting followed by ten quiet seconds | Recognition precedes questions; a deliberate pause allows settling | **P1 — Recognition before demand:** establish context before requesting effort | High | Open with a brief personalized acknowledgment, then present no immediate form pressure |
| Initial request: exactly three facts | Early information collection is sharply bounded | **P2 — Minimum viable intake:** ask only for information required for the next useful state | High | Keep initial setup to at most three decisions; defer optional profile and preference fields |
| One spoken orientation sentence; details placed elsewhere | Essential direction is immediate, while depth remains available without interruption | **P3 — Layered guidance:** foreground one next-step cue and make details self-serve | High | Show one concise orientation line plus a clearly labeled, non-blocking guide |
| Unready state: direct disclosure, alternatives, specific update time, personal closure | Recovery combines candor, agency, time certainty, and accountable follow-through | **P4 — Owned recovery:** name the problem plainly, provide viable choices, commit to a time, and close the loop | High | Delayed setup must display status, alternatives, an exact next-update time, ownership, and a later completion notification |
| Returning visitors skip orientation unless something changed | Repetition is suppressed unless new information justifies interruption | **P5 — Respect remembered context:** recognize prior completion and surface only meaningful changes | High | Returning users bypass introductory material; changed capabilities or policies appear as a compact delta |
| Ending occurs when a direction is chosen; no promotional addition | User choice is the terminal event; institutional asks do not hijack completion | **P6 — Clean release:** stop once agency is established | High | After destination selection, navigate immediately; do not append upgrades, invitations, surveys, or promotional prompts |

## Transfer layers

### Source content — do not transfer

Do not reuse domain-specific nouns, props, offers, scripts, spatial metaphors, or ceremonial styling from the observed service.

### Surface manifestations — adapt deliberately

- Translate the quiet pause into low-pressure interface pacing, not a forced countdown.
- Translate the single orientation sentence into concise product guidance.
- Translate the small reference card into an optional guide, checklist, or help surface.
- Translate personal follow-through into explicit system ownership, status updates, and notifications.

### Portable principles — preserve

P1 recognition before demand; P2 minimum viable intake; P3 layered guidance; P4 owned recovery; P5 remembered context; P6 clean release.

## Signature principles

1. **P1:** Acknowledge identity or invitation context before requesting input.
2. **P2:** Collect only what unlocks immediate collaboration.
3. **P3:** Keep the primary path sparse while making deeper guidance easy to find.
4. **P4:** Treat delays as commitments requiring transparent follow-through.
5. **P5:** Never make returning users repeat settled context without cause.
6. **P6:** Let the user’s chosen direction end onboarding.

## Productive tensions

- Personal, not chatty — **P1**
- Quiet, not inert — **P1, P3**
- Minimal, not ambiguous — **P2, P3**
- Direct about failure, not alarming — **P4**
- Familiar, not repetitive — **P5**
- Complete, not promotional — **P6**

## Invariants

- **P1:** No required input appears before a contextual acknowledgment.
- **P2:** First-time setup contains no more than three required decisions.
- **P3:** Detailed education never blocks the primary path.
- **P4:** A delayed or failed prerequisite always includes plain status, usable alternatives, a specific update time, and an owned follow-up.
- **P5:** Completed setup is not replayed unless a relevant change occurred.
- **P6:** Choosing a destination immediately exits onboarding.
- Identity, permissions, consent, security, errors, fees, and risk statements remain literal and unambiguous.

## Degrees of freedom

The designer may choose visual style, typography, layout, transition behavior, exact field types, help format, notification channel, and destination labels. The flow may be modal, full-page, or embedded, provided the invariants survive. The settling moment may be expressed through whitespace and gentle pacing rather than a literal delay.

## Target translation

| Principle | Source manifestation | Target-medium decision | Literal copy to avoid |
|---|---|---|---|
| P1 | Personal recognition, then silence | Show the user’s name or invitation context with a calm opening state before setup controls | Service-role dialogue or staged ceremony |
| P2 | Three initial facts | Ask at most three decisions such as display identity, collaboration intent, and notification preference; require only what is operationally necessary | Reproducing the original facts or arbitrary numeric mimicry |
| P3 | One-line orientation plus separate detail | Provide one next-step sentence and an optional “How collaboration works” surface | Prop-like reference artifacts |
| P4 | Direct delay handling with alternatives and timed follow-up | Provide status, retry/background continuation, safe independent work, exact update time, and completion notification | Themed consolation offers |
| P5 | Abbreviated return path | Route recognized users directly onward; show only a concise “What changed” notice when applicable | Replaying welcome content for warmth |
| P6 | Ends at chosen direction | Offer clear destinations such as opening assigned work, creating a draft, or reviewing shared content; navigate on selection | Post-completion promotion or feedback solicitation |

# Implementation-ready flow handoff

## State and action register

| State | Trigger | Required presentation | Available actions | Transition and ownership |
|---|---|---|---|---|
| **First-time: acknowledgment** | New user opens a valid invitation or account | Name or invitation context; one calm sentence; no required controls in the opening beat — P1 | Continue | User continues to minimal setup |
| **First-time: minimal setup** | Acknowledgment completed | At most three necessary decisions; optional items visibly deferred — P2 | Confirm; access literal help for identity, consent, or permissions | Valid input advances; invalid input remains in place with field-specific correction |
| **First-time: orientation** | Setup succeeds | One sentence explaining the immediate collaboration model; optional detailed guide — P3 | Open guide; choose destination | Guide returns to the same state; destination selection exits onboarding — P6 |
| **Returning: unchanged** | Prior setup recognized; no relevant changes | Brief recognition only — P5 | Choose destination | Selection exits immediately — P6 |
| **Returning: changed** | Prior setup recognized; relevant product, policy, or permission change exists | Compact delta stating only what changed; consequential terms remain literal — P5 | Acknowledge required change; inspect details; choose destination when permitted | Required acknowledgment is stored separately; destination choice remains user-owned |
| **Delayed setup** | Workspace provisioning, document synchronization, or another prerequisite is incomplete | Plain status, affected capability, exact next-update time, responsible system actor — P4 | Continue with an unaffected task; leave and be notified; retry if safe | System monitors the prerequisite and sends the promised update |
| **Delayed setup: resolved** | Prerequisite completes | Clear completion notice and restored action | Resume intended destination; choose another destination | User selection exits onboarding — P4, P6 |
| **Recovery: correctable input** | Validation fails | Literal field-level error explaining what must change | Correct; cancel where safe | User correction retries only the affected step |
| **Recovery: access or invitation problem** | Link invalid, expired, revoked, or account mismatch | Literal cause when known; no reassuring euphemism — P4 | Request a new invitation; switch account; contact the responsible collaborator | System confirms request receipt and gives a specific response expectation |
| **Recovery: system failure** | Setup cannot complete | Plain failure statement, preserved-data status, safe alternatives, reference identifier, next-update time — P4 | Retry; continue with unaffected work; leave and be notified | System owns monitoring and explicitly reports success or continued failure |
| **Exit** | User chooses a valid destination | No intermediate completion page unless technically necessary — P6 | None beyond destination-native actions | Onboarding is complete |

## Production sequence

1. Model eligibility, first-time, returning, changed, delayed, recovered, and exit states.
2. Separate prerequisite clearance from the user’s destination decision.
3. Implement the P1 acknowledgment state without a forced timer.
4. Reduce required setup to three or fewer operational decisions under P2.
5. Write one primary orientation sentence and move all depth to optional guidance under P3.
6. Add P4 recovery contracts: status, alternatives, exact update time, owner, and follow-up event.
7. Persist completion and change versions so P5 routing is deterministic.
8. Make destination selection the final onboarding event under P6.
9. Test keyboard, screen-reader, reduced-motion, narrow-screen, offline, and notification-denied behavior.

## Downstream prompt

Design an asynchronous onboarding flow for a collaborative writing app using principles P1–P6 from this handoff. Include first-time, returning-unchanged, returning-changed, delayed-setup, correctable-error, access-error, system-failure, resolved, and exit states.

Begin with contextual recognition before required input (P1). Limit initial required setup to three operational decisions (P2). Give one concise orientation sentence and place detailed guidance behind an optional, non-blocking surface (P3). For every delay or failure, state the condition plainly, offer usable alternatives, provide a specific next-update time, identify the responsible system actor, and explicitly close the loop (P4). Skip completed material for returning users and show only meaningful deltas (P5). End immediately when the user chooses a destination; add no promotion, upgrade, invitation request, survey, or review request (P6).

Keep identity, permissions, consent, security, errors, fees, and risks literal. Do not use source-domain vocabulary, props, spatial metaphors, consolation motifs, or ceremonial decoration. Deliver a state diagram, screen inventory, component specifications, final interface copy, transition rules, accessibility notes, and acceptance criteria.

## Anti-patterns and originality guardrails

- A long welcome carousel or tutorial tour — violates P2 and P3.
- A fake countdown or unskippable pause — shallow imitation of P1.
- Collecting optional biography, preferences, or marketing data before value — violates P2.
- Vague states such as “Almost there” without cause or timing — violates P4.
- Claiming work continues without sending a later result — violates P4.
- Replaying setup for recognized users — violates P5.
- Treating a system acknowledgment as permission to choose on the user’s behalf.
- Adding upsells, invitations, ratings, or surveys after destination selection — violates P6.
- Reusing source-domain language, objects, gestures, or visual theming.

## Validation checks

- [ ] Does the opening acknowledge the person or invitation context before requesting input? **P1**
- [ ] Is there no artificial waiting requirement? **P1**
- [ ] Are there three or fewer initially required decisions? **P2**
- [ ] Is every required decision necessary for the immediate next state? **P2**
- [ ] Is primary orientation limited to one concise cue? **P3**
- [ ] Can detailed guidance be skipped without blocking progress? **P3**
- [ ] Does every delay or failure name the condition plainly? **P4**
- [ ] Does each delayed state offer at least one viable alternative? **P4**
- [ ] Does each delayed state show a specific next-update time and accountable owner? **P4**
- [ ] Does the system explicitly notify the user when the condition resolves or persists? **P4**
- [ ] Do returning users bypass unchanged material? **P5**
- [ ] Are changes shown as deltas rather than a replay? **P5**
- [ ] Does destination selection exit onboarding immediately? **P6**
- [ ] Are promotional and feedback requests absent from the exit path? **P6**
- [ ] Are high-stakes statements literal and accessible?
- [ ] Is all source-domain decoration absent?

## Unknowns and confidence

The behavioral thesis and P1–P6 are strongly supported by the supplied sequence. Exact copy, visual language, timing beyond the observed pause, collaboration roles, mandatory setup data, notification guarantees, and technical failure taxonomy remain unresolved. Validate those choices through product requirements and accessibility testing rather than attributing them to the source.

## Boundary audit

Read only `task.md`, `taste-extractor/SKILL.md`, and `taste-extractor/references/taste-profile.md` within the current directory. No files were written or modified, and no external resources were accessed.