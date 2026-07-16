# Dojo scenarios — taste-extractor v0.2 redo

Repository root: `<repository-root>`
Root resolution: `git`
Repository slug: `dojo`
Candidate skill path:
`<repository-root>/example/taste-extractor/v0.2/candidate/taste-extractor`

Date: 2026-07-16
Tier: technique
Host: clean ephemeral Codex CLI contexts
Model: `gpt-5.6-sol`
Evidence: audited instruction-bounded
Training trials: one per case
Final holdout trials: one per cell

## Claim

Compared with no skill, `taste-extractor` more reliably converts accessible
evidence from varied media into an original, evidence-traced,
implementation-ready taste handoff and handles partial or missing evidence
without invention.

## Predeclared coverage ledger

| Claim cell | Training case | Reserved holdout shape |
|---|---|---|
| Same-medium extraction across states | T1 interface family | recurring corpus with an outlier |
| Voice without copying content | T2 prose family | cross-medium originality transfer |
| Temporal cross-medium translation | T3 audio to facilitation | time-based source to an operational protocol |
| Physical relationships without decorative copying | T4 craft collection to status service | corpus recurrence and functional translation |
| Service sequence, exception, and recovery | T5 ritual to onboarding flow | breakdown, authority, and staged recovery |
| Partial or absent evidence | T6 partial video | partial or fully unavailable modality |
| Complete downstream contract | T1-T5 | implementation-ready held-out handoff |

Six training cases and three holdout cells were chosen because the broad medium
claim has more uncertainty across kinds of evidence than across repeated
samples of the same prompt. The one-trial design is breadth evidence, not a
statistical reliability claim.

## Isolation contract

Runner, grader, and custodian preflights each returned `MISSING_CONTEXT`, saw no
outside canary, and reported only their allowed task path. Baselines saw one
task. Skilled runners saw one task plus the candidate. Graders saw one task,
its prewritten criteria, and one blinded output. The final custodian saw only
the claim, interface, abstract cells, and trial count.

## Attempt ledger

| Attempt | Result | Disposition |
|---|---|---|
| a1 | H1 5/5, H2 5/5, H3 4/5 | burned; missing-video substitute package corrected |
| a2 | new cases exposed trace reuse, action-register, audio-intake, and authority gaps | burned; each affected case became regression evidence |
| a3 | H7-H9 each 5/5, but final training regression returned T1 4/5 and T2 3/5 | burned; priority, prose-axis, and quotation rules tightened |
| a4 | H10 5/5, H11 4/5, H12 4/5 | burned; exact schema/count semantics and per-axis coordinates corrected |
| a5 | H13 5/5, H14 4/5, H15 5/5 | burned; every supported prose matrix cell required its own quote |
| a6 | H16 5/5, H17 5/5, H18 5/5; all qualitative gates PASS | graduated |

One a2 criterion was invalidated because it required an append-only test absent
from the task. It contributed no score. The final custodian had to quote the
task basis for every criterion before release.

## Status

Final candidate revision:
`sha256:b5ade59ca5952440b433fa122e40c0c69f0d5c62d9e98145021a74a2e1cf987f`.

Terminal outcome: **GRADUATED**.
