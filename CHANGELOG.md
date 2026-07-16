# Changelog

All notable changes to Dojo are documented here.

## 0.2.0 — 2026-07-16

### Added

- Three evidence grades: audited instruction-bounded, fresh-context-only, and
  degraded local review.
- Per-run capability envelopes with canonical read and write allowlists,
  network and memory policy, missing-context behavior, and path audits.
- Unique run capsules that keep criteria, sibling fixtures, prior outputs,
  authoring notes, and unopened holdouts outside the runner's declared scope.
- Canary preflights for calibrating the selected host, model, tool policy, and
  skill-catalog configuration before real evaluation runs.
- `PASS`, `FAIL`, and `INVALID` run states. Contaminated or uninterpretable
  runs now contribute no score and must be replaced.
- Coverage ledgers spanning modes, archetypes, state transitions, dependency
  states, output contracts, safety boundaries, and important interactions.
- Predeclared independent trial counts for risky or stochastic behavior.
- Separate author/trainer, holdout-custodian, runner, grader, and orchestrator
  roles. Concrete holdouts are materialized only after candidate freeze.
- Capability envelopes, canaries, and audits for every evidence-bearing role;
  the weakest role determines the campaign's isolation grade.
- A per-role isolation manifest plus a canonical SHA-256 candidate-tree digest
  covering every packaged file by normalized path and exact bytes.
- Isolation manifests, invalid-run ledgers, and evidence labels in the record
  template.
- A reference-correctness claim inventory with source authority, version,
  conflict, and pass/fail/unresolved semantics.
- Deterministic `GRADUATED`, `NOT GRADUATED`, and `UNPROVEN` verdicts scoped to
  an immutable candidate revision and its latest graduation attempt.
- Precommitted qualitative gates for claims that process checks alone cannot
  judge, without turning taste into a fake scalar.
- A curated isolation validation showing that bounded runners resist ordinary,
  urgency, and in-file scope-expansion pressure.
- A curated self-test receipt comparing the released revision with the final
  candidate across nine behaviors, three discipline pressures, and unseen
  evidence-integrity decisions.

### Changed

- Audited capability prompting is the highest portable evidence grade and may
  support baseline, pressure, and graduation when its canary and audit pass.
- Fixed behavior counts were replaced with coverage- and risk-scaled starting
  bands. Small skills remain inexpensive; broad claims require broader proof.
- Routing matrices now expand beyond the initial 10–15 prompts when a skill's
  modes, exclusions, or neighboring owners require more coverage.
- Baseline results distinguish corrected, preserved, regressed, and
  counterfactual-unproven behavior instead of manufacturing RED.
- New criteria discovered after a run must become precommitted regression
  cases rather than retroactive scores.
- Holdout trial counts are declared before candidate freeze; any required-trial
  failure burns the holdout.
- Runtime outputs are copied into `~/.dojo/` by the orchestrator after a runner
  stops instead of making the shared evidence tree part of the runner scope.
- Repository identity is anchored to the candidate skill directory rather than
  the caller's ambient working directory.
- Mixed-tier skills use the highest-risk load-bearing behavior; rationalizable
  safety, permission, or evidence gates take discipline-tier rigor.
- Narrow edits use an explicit change-to-kata map instead of an undefined
  “touched kata” shortcut.
- Edit-improvement claims compare against the released version; no-skill
  baselines remain valid only for absolute skill-value claims.
- Rebuilt the Taste Extractor worked example as a native v0.2 campaign: six
  counterfactual training pairs, role canaries, invalid-run accounting, bounded
  corrections, five honestly burned candidate freezes, three fresh final
  holdouts at 15/15, routing, package smoke, and a receipt-backed v0.1 versus
  v0.2 comparison.

### Evidence migration

- The original standalone campaign remains a v1 historical record and is not
  retroactively upgraded.
- The v0.1 Taste Extractor remains available through repository history; the
  checked-in worked example now carries fresh v0.2 evidence and an explicit
  comparison with that earlier candidate.

## 0.1.0 — 2026-07-15

- Initial standalone release.
- Introduced the seven-kata workflow, tier-specific rigor, bounded edits,
  held-out graduation, trigger evaluation, external evidence storage, and the
  receipt-complete taste-extractor example.
