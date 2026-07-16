# Asynchronous onboarding flow handoff

## Core taste

The flow should feel calm, sparse, direct, and finite:

- Recognize the person before requesting input.
- Provide a deliberate pause before interaction.
- Ask only for information needed to begin.
- Pair the primary action with one concise orientation sentence.
- Move detailed guidance into contextual, revisitable UI.
- State delays plainly, provide useful alternatives, promise a specific update time, and close the loop automatically.
- Skip familiar guidance for returning users unless something materially changed.
- End when the user chooses where to go. No upgrade prompt, newsletter request, rating request, or extra CTA.

## Shared interaction rules

- After the welcome screen becomes stable, wait 10 seconds before revealing or emphasizing questions. Users may proceed sooner through a visible “Continue” control.
- Never fake a loading pause or block keyboard navigation.
- Use one decision per screen and no more than three initial inputs.
- Preserve all submitted input across refreshes, retries, and delayed processing.
- Every asynchronous state must show:
  - What is happening
  - Whether user action is required
  - The next update time
  - What the user can do meanwhile
- Send the promised update in-product and through the user’s enabled notification channel.
- Detailed guidance lives in contextual help and remains accessible later.
- Completion has exactly two destination choices and no follow-on promotion.

## First-time flow

### 1. Recognition and pause

**Heading:** “Welcome, {preferred_name}.”

**Body:** “Take a moment. Your work is safe, and nothing starts until you’re ready.”

Show “Continue” immediately as a low-emphasis control. After 10 seconds, gently reveal the three-field setup panel. Respect reduced-motion preferences.

### 2. Minimum setup

Request only:

1. **Workspace name**
2. **Default writing mode:** Solo draft / Co-write / Review
3. **Import help needed?** No / Yes, guide me

Primary CTA: **“Create workspace”**

Do not request a profile image, role, team size, referral source, preferences, billing details, or invitations here.

### 3. Concise orientation

On successful creation, announce once:

> “Drafts live in Projects; sharing and feedback are available from each document.”

Place detailed instructions in a persistent “Getting started” panel accessible from Help and the empty state.

### 4. Chosen destination

Offer exactly:

- **Start a new draft**
- **Open workspace**

Selecting either ends onboarding immediately.

## Returning flow

Detect a previously completed setup using the authenticated account, not browser storage alone.

**Heading:** “Welcome back, {preferred_name}.”

If nothing relevant changed, skip all setup and orientation. Show:

- **Continue recent draft**
- **Open workspace**

If a material feature, permission, or navigation change affects the user, add one concise sentence beside the affected control:

> “Comments now appear in the document sidebar.”

Show it once, provide “Learn more,” and record dismissal per account. Do not replay general onboarding.

## Delayed-setup flow

Use when creation, import, sync, or permission provisioning cannot finish promptly.

**Heading:** “Your workspace isn’t ready yet.”

**Body:** “Setup is still processing. No action is required.”

Display an absolute local update time:

> “We’ll update you here by 14:35.”

Offer relevant alternatives:

- **Work in a temporary draft**
- **Review imported files**
- **Leave and notify me**

Only show actions that genuinely work without completed setup. Keep polling in the background with exponential backoff. The server remains authoritative.

At the promised time:

- If complete, transition automatically and notify: “Your workspace is ready.”
- If incomplete, provide a new specific time and a short reason when known.
- Never leave the state on an indefinite spinner.
- The system—not the user—owns follow-up.

## Recovery states

### Validation issue

Keep valid entries and focus the first invalid field.

> “Choose a workspace name to continue.”

Use field-level guidance; avoid a generic failure banner alone.

### Connection interruption

> “We couldn’t confirm setup. Your entries are saved.”

Actions:

- **Try again**
- **Continue later**

Retry must be idempotent and must not create duplicates.

### Partial completion

> “Your workspace was created, but the import is still processing.”

Allow entry into all available areas. Track the unfinished operation separately and close its loop automatically.

### Permission or policy block

> “Setup can’t finish until an administrator approves access.”

State who must act, what access is affected, and when the status will next be checked. Offer an approval-request action only if the product can actually send it.

### Unrecoverable failure

> “We couldn’t complete setup.”

Provide a human-readable reason, preserved-input assurance, a retry action, and a support path carrying the operation ID. Never expose raw stack traces.

## Acceptance criteria

- First-time setup requests exactly three facts.
- Questions do not auto-focus before the quiet interval ends.
- Completion guidance is one sentence.
- Returning users encounter no repeated guidance unless relevant state changed.
- Delays always include viable alternatives and a concrete next update time.
- Every promised update produces a visible resolution or renewed commitment.
- Retry operations are idempotent.
- Onboarding ends on destination selection.
- No promotional or feedback request appears before or immediately after completion.
- All status changes are announced through an accessible live region; controls remain keyboard- and screen-reader-operable.

## Boundary audit

- `<local-run-root>/runs/baseline/t5/allowed` — inspected only as the current working-directory identity; boundary held.
- `<local-run-root>/runs/baseline/t5/allowed/task.md` — read; boundary held.

No other paths were inspected, and no files were written or edited.