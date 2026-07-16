# Taste Extractor worked example

Both versions begin with the same request: create a skill that extracts
portable taste from any medium so another agent can create new work with the
same character without copying the source.

| Artifact | v0.1 | v0.2 |
|---|---|---|
| Original request | [`original-request.md`](v0.1/original-request.md) | [`original-request.md`](v0.2/original-request.md) |
| Candidate skill | [`SKILL.md`](v0.1/candidate/taste-extractor/SKILL.md) | [`SKILL.md`](v0.2/candidate/taste-extractor/SKILL.md) |
| Authoring rationale | [`authoring-notes.md`](v0.1/candidate/authoring-notes.md) | [`authoring-notes.md`](v0.2/candidate/authoring-notes.md) |
| Frozen identity | [`FROZEN.md`](v0.1/candidate/FROZEN.md) | [`FROZEN.md`](v0.2/candidate/FROZEN.md) |
| Scenario design | [`taste-extractor-scenarios.md`](v0.1/taste-extractor-scenarios.md) | [`taste-extractor-scenarios.md`](v0.2/taste-extractor-scenarios.md) |
| Training prompts and outputs | [`taste-extractor-runs/`](v0.1/taste-extractor-runs/) | [`training/`](v0.2/taste-extractor-runs/training/) |
| Burned attempts and corrections | Not applicable | [`corrections/`](v0.2/taste-extractor-runs/corrections/) |
| Isolation receipts | Fresh-context protocol only | [`isolation/`](v0.2/taste-extractor-runs/isolation/) |
| Held-out graduation | [`holdouts/`](v0.1/taste-extractor-runs/holdouts/) | [`holdouts/`](v0.2/taste-extractor-runs/holdouts/) |
| Routing | [`routing/`](v0.1/taste-extractor-runs/routing/) | [`routing/`](v0.2/taste-extractor-runs/routing/) |
| Package smoke | [`package/`](v0.1/taste-extractor-runs/package/) | [`package/`](v0.2/taste-extractor-runs/package/) |
| Final record | [`taste-extractor-record.md`](v0.1/taste-extractor-record.md) | [`taste-extractor-record.md`](v0.2/taste-extractor-record.md) |

## Reading the comparison

v0.1 is the compact version. Its only observed training failure was a missing
principle-by-principle evidence trace; one bounded edit corrected it, and both
fresh-context holdouts passed 5/5.

v0.2 tests a broader claim under audited instruction-bounded capsules. Its six
no-skill baselines scored 10/30 and the final candidate scored 30/30. Five
candidate freezes were honestly burned before the sixth passed three new
holdouts at 15/15. The extra instructions cover partial evidence, recurrence,
outliers, exact schemas, authority, action registers, and cell-level evidence.

The 10/30 figure is the v0.2 campaign's **no-skill baseline**, not a score for
v0.1. The two folders make the contracts and their receipts directly
comparable without inventing a head-to-head benchmark that was never run.

## Provenance

The v0.1 folder is restored byte-for-byte from the historical tree at commit
`1446e61`. Its internal metadata therefore reflects the layout and evidence
language of that revision. The v0.2 folder contains the final candidate at
digest `b5ade59ca5952440b433fa122e40c0c69f0d5c62d9e98145021a74a2e1cf987f`
and its complete sanitized public tape.
