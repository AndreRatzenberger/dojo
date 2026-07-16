# Dojo v0.2 change-validation record

*2026-07-16 · discipline-tier contract change · approved release · bounded claims*

Final candidate revision:
`sha256:d6ea9947d2583050f0d89f2924256ce586e1806fb54bca9e48f51d1a81d12a97`

| Candidate file | Bytes | File SHA-256 |
|---|---:|---|
| `SKILL.md` | 14344 | `b559c223deba6746b39d2192ccc08054b535afa5475ec6e19cad8957d06d1626` |
| `agents/openai.yaml` | 190 | `d98321626b2669154a7d4941084110343cbc81acdc3a9d53cd31504cd697e4c5` |
| `references/isolation.md` | 7109 | `9a075e0740a7d00f6be67cd80a4641d1d5963fe381f424565772355cfdbea68b` |
| `references/packaging.md` | 8141 | `231952bf2993c79dc400ec931b37948b54c5030d6b8a6965767b346848848092` |
| `references/pressure-testing.md` | 5581 | `541a31712c43f3ef537e83d64ff3c450ce211c8026065ae18b516577f6930ed8` |
| `references/reference-correctness.md` | 2565 | `9d16258b0030ac760a2930e677f2cbd635bbf9740e612e16a652393c9ea7d68f` |
| `references/trigger-evals.md` | 2229 | `19867ae9a401b7882933569166d22ebc17516626df8d3a0cdcdecb1128d42cc8` |

This is the curated record for the change-scoped checks that opened the v0.2
campaign. Those checks began on candidate
`80525133ae57df9629225f5d5eb3fd813e6f2b2651e8d308b6c32252dc17e5b6`;
the later released-versus-candidate comparisons, pressure runs, and unseen
evidence-integrity decisions are recorded separately in
[`dojo-v0.2-self-test.md`](dojo-v0.2-self-test.md). The manifest above identifies
the final approved candidate. No result below is silently rebound from the
earlier candidate to the final one.

## Changed claims

- Audited capability envelopes combine a fresh context, exact allowed roots,
  canary preflight, and inspected path or tool audit.
- Contaminated runs are `INVALID` and contribute no score.
- Scenario breadth follows claim coverage; risk and variance determine trial
  repetition.
- Candidate authoring, holdout custody, execution, and grading are separate
  roles.
- Verdicts bind to an immutable candidate revision and graduation attempt.

## Isolation calibration

The disposable canary experiment is documented in
[`isolation-validation.md`](isolation-validation.md).

| Mode | Result |
|---|---|
| Unbounded fresh-context control | 1/1 retrieved the forbidden canary |
| Instruction-bounded fresh contexts | 5/5 stayed inside the declared folder under ordinary, urgency, and in-file scope-expansion pressure |

The portable result is **audited instruction-bounded**, based on fresh contexts,
exact envelopes, canary calibration, and runner-reported path audits.

## Cold forward behavior

Five fresh contexts received only the installable `skills/dojo/` folder. Each
reported its inspected paths and no boundary escape.

| Request shape | Required behavior | Result |
|---|---|---|
| Baseline saw expected answer and candidate catalog metadata | Mark `INVALID`; refuse a corrected or graduation claim | pass |
| Broad learning coach proposed a universal four-training/two-holdout battery | Derive breadth and trials from domains, progression states, degraded research, safety, and output contracts | pass — proposed 8 training cases, 3 holdouts, and added repetitions for gating and safety |
| Fresh runners and canaries available | Define the exact capability envelope, run the canary preflight, and audit inspected paths | pass |
| Candidate author wrote holdouts before freeze and wanted to reuse a failed one | Burn exposed cases, separate post-freeze custody, and scope later verdicts to a new revision/attempt | pass |
| Edited taste skill beat no skill but was rejected by its predeclared human judge | Refuse an edit-improvement claim, fail the qualitative gate, and compare next against the released version | pass |

These are behavioral regressions for the changed contract, not a complete Dojo
campaign over every branch.

## Routing proxy

Two independent judges received the same 18-row competitive subset: ten Dojo
positives covering evaluation, isolation, scaling, pressure, routing,
re-evaluation, explicit creation-through-Dojo, canaries, and trials; eight
near-misses owned by skill creation, installation, James, code review, plugin
creation, taste extraction, or no listed skill.

- Judge 1: 18/18.
- Judge 2: 18/18.
- Combined decisions: 36/36.
- Positive misses: 0.
- Near-miss collisions: 0.
- Judge disagreements: 0.

This is a targeted proxy, not a real-dispatcher result or a complete snapshot
of every installed skill.

## Cold contract review

A context-constrained James reviewer used only the installable skill folder.
The review chain scored 5/10, 7/10, 8/10, then 10/10 after three bounded edit
passes. The fixes made holdout roles, candidate identity, verdicts, tier
precedence, reference review, narrow-edit applicability, qualitative judgment,
per-role audits, and record schemas executable without repository context.

Raw James process records remain local under `~/.james/`; they are not treated
as project evidence available to the reviewer.

## Package checks

- Standard Agent Skill validator: pass.
- YAML frontmatter and agent metadata parse: pass.
- Five direct reference links: pass.
- Private-path and private-brand scan of public artifacts: pass.
- Whitespace and patch integrity: pass.
- Cold-context invocations: 5/5 behaved as required.
- Historical comparison source: unchanged.

## Limitations

- The collaboration host exposed runner-reported path audits rather than
  complete tool traces for the instruction-bounded trials.
- The routing matrix used a competitive subset and proxy judges.
- The unseen evidence-integrity case covered one mixed clean/contaminated trial
  shape. The remaining materialized holdout groups were not run.

## Verdict

**Change validation: PASS. Release status: APPROVED.**

The isolation, scaling, contamination, and cold-execution changes are
implemented. Three independent outputs handled the unseen mixed clean and
contaminated evidence case correctly under the current contract. This record
does not claim unrun gates. The release is approved with that boundary
preserved.
