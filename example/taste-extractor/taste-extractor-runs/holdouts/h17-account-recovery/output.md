# Recovery interface taste transfer

## Job record

- Source artifacts: `PASSAGE-A`, `PASSAGE-B`, and `PASSAGE-C`
- Source medium: prose
- Downstream target: consequential account-recovery interface copy for a regional credit-union app
- Access status: all three supplied passages were available
- Transfer thesis: Use restrained language, compact sequencing, precise actions, and immediate consequences without transferring source content.

## Passage-by-axis matrix

| Passage | voice | rhythm | specificity | tension | agency | consequence |
|---|---|---|---|---|---|---|
| `PASSAGE-A` | **A-V:** Emotionally restrained third-person observation keeps judgment out of the narration. Quote: “Mara checked the latch twice” | **A-R:** A measured action sequence gives way to a short state change. Quote: “then placed the spare key beneath the blue cup. By dusk, the cup had moved.” | **A-S:** Concrete placement makes the precaution easy to visualize. Quote: “the spare key beneath the blue cup” | **A-T:** Tension emerges from an unexplained change rather than an explicit threat. Quote: “By dusk, the cup had moved.” | **A-A:** Deliberate initial actions contrast with an unidentified later actor. Quote: “Mara checked the latch twice, then placed” | **A-C:** The changed condition implies that the earlier safeguard may no longer be reliable. Quote: “the cup had moved.” |
| `PASSAGE-B` | **B-V:** First-person narration is terse, procedural, and self-possessed. Quote: “I corrected one letter.” | **B-R:** Three compact steps advance without commentary or delay. Quote: “I corrected one letter. He closed the ledger” | **B-S:** A single-character discrepancy receives exact attention. Quote: “I corrected one letter.” | **B-T:** The interaction tightens when correction does not complete verification. Quote: “He closed the ledger and asked for the seal.” | **B-A:** The narrator takes one clear corrective action while the other party controls the next requirement. Quote: “I corrected one letter. He closed the ledger” | **B-C:** Progress depends on satisfying an additional verification requirement. Quote: “asked for the seal.” |
| `PASSAGE-C` | **C-V:** Close third-person narration reports discovery with controlled urgency. Quote: “Tomas unfolded the rain-soft ticket and saw” | **C-R:** A short scarcity statement precedes a longer sentence that reveals the problem. Quote: “Only one ferry remained. Tomas unfolded” | **C-S:** Material condition and date make the source of failure concrete. Quote: “the rain-soft ticket” and “yesterday’s date” | **C-T:** A single remaining opportunity creates immediate pressure. Quote: “Only one ferry remained.” | **C-A:** The character can inspect the evidence but cannot change the condition already present. Quote: “unfolded the rain-soft ticket and saw” | **C-C:** The revealed date threatens the ability to proceed before the remaining opportunity is lost. Quote: “yesterday’s date bleeding through the paper.” |

## Precedence and safety invariants

Accessibility, correctness, and operational clarity outrank extracted style and fidelity. Identity requirements, security conditions, delays, failures, and lock effects must remain literal.

> Security and comprehension override literary resemblance; when they conflict, preserve the literal instruction and remove the stylistic echo.

## Recovery moments

### IDENTITY_CHECK

1. `moment_id`: `IDENTITY_CHECK`
2. `source_trace_ids`: `B-V`, `B-R`, `B-S`, `B-A`, `B-C`
3. `user_state`: The user has started account recovery and must verify account ownership before access can be restored.
4. `eyebrow`: Account ownership check
5. `headline`: Verify that this account belongs to you
6. `body`: Enter the one-time verification code sent to a contact method already registered to this account. We use this code to confirm that you control that contact method.
7. `primary_action`: Enter verification code
8. `secondary_action`: Use a different verification method
9. `consequence`: If verification succeeds, you can continue account recovery. If verification fails, access will not be restored through this step.
10. `support_path`: If you cannot use a registered contact method, contact account recovery support for a manual ownership review.
11. `accessibility_note`: Use one paste-enabled code field, identify errors in text rather than color alone, and announce verification failures to assistive technology without clearing the entered code.
12. `rationale`: `B-S` and `B-A` support asking for one precise action at a time. `B-C` supports stating that another requirement must be satisfied before progress. `B-V` and `B-R` support the restrained voice and compact procedural sequence.

### SECURITY_HOLD

1. `moment_id`: `SECURITY_HOLD`
2. `source_trace_ids`: `A-V`, `A-T`, `A-A`, `A-C`, `C-R`
3. `user_state`: Suspicious account-recovery activity has triggered a protective delay, and recovery cannot continue until the hold ends.
4. `eyebrow`: Protective security delay
5. `headline`: Account recovery is temporarily on hold
6. `body`: We detected recovery activity that did not match this account’s usual security signals. To protect the account, recovery is paused until the date and time shown below. Recovery details cannot be changed during this hold.
7. `primary_action`: Review recovery activity
8. `secondary_action`: Cancel recovery request
9. `consequence`: You cannot regain access or change recovery details until the hold ends. Canceling will stop this recovery request.
10. `support_path`: If you did not start account recovery, cancel the request and contact the credit union’s fraud support team.
11. `accessibility_note`: Show the hold end in the user’s local date, time, and time zone; do not communicate the delay through a countdown alone; and announce any status change to assistive technology.
12. `rationale`: `A-T` and `A-C` support leading with the changed security state and its immediate effect. `A-A` supports distinguishing confirmed user actions from activity whose actor has not been established. `A-V` and `C-R` support a controlled tone that states urgency before explanation.

### FINAL_WARNING

1. `moment_id`: `FINAL_WARNING`
2. `source_trace_ids`: `C-V`, `C-R`, `C-T`, `C-A`, `C-C`, `B-A`
3. `user_state`: The user has failed previous identity checks and has exactly one attempt remaining before account recovery is temporarily locked.
4. `eyebrow`: Final verification attempt
5. `headline`: One attempt remains before a temporary lock
6. `body`: Check your identity information before submitting it. This is your final available attempt.
7. `primary_action`: Submit identity check
8. `secondary_action`: Review my information
9. `consequence`: If this identity check fails, account recovery will be temporarily locked. You will not be able to make another recovery attempt until the lock ends.
10. `support_path`: If you are unsure that your information is correct, contact account recovery support before submitting this attempt.
11. `accessibility_note`: State the remaining-attempt count and lock consequence in text, announce both before focus reaches the submit action, and do not rely on color or an icon to indicate severity.
12. `rationale`: `C-T` and `C-C` support stating the single remaining opportunity and its result immediately. `C-A` supports separating what the user can still correct from the system state they cannot change. `C-R` and `B-A` support a brief warning followed by one explicit action.

## Boundary audit

Read exactly: `task.md`, `taste-extractor/SKILL.md`, and `taste-extractor/references/taste-profile.md`. No other file or path was inspected, and no external resources were used.