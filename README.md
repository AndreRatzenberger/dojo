<p align="center">
  <img alt="Dojo banner" src="docs/assets/dojo-banner.png" width="900">
</p>

<p align="center">
  <a href="https://github.com/AndreRatzenberger/dojo/stargazers"><img src="https://img.shields.io/github/stars/AndreRatzenberger/dojo?style=flat-square" alt="GitHub stars"></a>
  <a href="https://github.com/AndreRatzenberger/dojo/commits/main"><img src="https://img.shields.io/github/last-commit/AndreRatzenberger/dojo?style=flat-square" alt="Last commit"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/AndreRatzenberger/dojo?style=flat-square" alt="License"></a>
</p>

<p align="center">
  <em>"black belts are earned, not declared"</em>
</p>

**Dojo trains your skills for the black belt.**

A rough idea can enter in a white belt. Dojo first watches the untrained agent,
then writes the smallest useful technique, spars against the failure, and keeps
training until the skill is ready for held-out graduation. An existing skill can
walk onto the same mat for hardening.

Dojo awards no belts for beautiful prose. A skill earns trust only through the
rigor appropriate to its tier, and every stumble, burned holdout, and surviving
fix leaves a receipt.

---

## Install

Install with the [Skills CLI](https://skills.sh/docs/cli):

```bash
npx skills add AndreRatzenberger/dojo
```

The CLI detects supported agents and asks where to install the skill. Add `-g`
for a user-level installation.

---

## Enter The Dojo

Dojo now opens with two doors and tells you what each one costs before anybody
starts doing push-ups.

| Lane | Best For | What Happens |
|---|---|---|
| **Fast Lane** | Early creation, ordinary hardening, focused edits, quick feedback | Fresh runners receive explicit “do not spelunk” boundaries; Dojo runs the affected comparison, bounded fixes, one fresh check, and applicable routing/package work. No custody bureaucracy or fake graduation claim. |
| **Audit Lane** | Graduation, publishing, benchmarks, high-risk or contamination-sensitive claims | Full v0.2 isolation: exact envelopes, canaries, inspected traces, frozen candidates, role-separated held-outs, and invalid-run accounting. Machine manifests appear only when the package actually has hidden evaluator files, scripts, tool receipts, artifacts, or portability claims. |

With no argument, `--lane auto` shows a compact overview of both lanes,
recommends one, explains why, and starts without a confirmation ritual. Lane
controls evidence rigor; discipline, technique, and reference still control
which kata apply.

```text
Use $dojo --lane auto to harden this skill.
```

For deterministic automation and benchmark matrices, pin the lane:

```text
Use $dojo --lane fast --quiet to run the focused skill check.
Use $dojo --lane audit --quiet to run the audit-grade campaign.
```

Dojo also accepts `--fast-lane true` and `--audit-lane true` as convenience
aliases. Conflicting selectors fail as `INVALID_LANE`; an explicit lane never
silently changes underneath a benchmark.

These are arguments in the skill invocation, not a `dojo` shell executable.
Automation sends them with the prompt or host skill call.

Interactive campaigns include a compact milestone/ETA ticker. It stays out of
final answers, runner prompts, evidence, JSON, exact-output tasks, and every
`--quiet` invocation.

Graduation-grade evidence still requires a fresh context and an audited
information boundary: exact allowed roots, a canary preflight, and an inspected
path or tool audit. Fast Lane provides useful working confidence, not a black
belt with the serial number filed off.

```text
Use $dojo to prove this skill changes behavior before we publish it.
```

```text
Run this SKILL.md through Dojo. Pay special attention to trigger collisions.
```

```text
Build this new skill through Dojo and keep two scenarios held out.
```

Dojo also activates for requests such as “test this skill,” “harden this
SKILL.md,” and “why is this skill triggering?” It deliberately does not take
over ordinary first-draft skill creation unless Dojo is explicitly requested.

---

## The Receipts

The skill is only half the artifact. The other half is the evidence trail that
explains why this particular skill deserves to exist.

| Receipt | What It Means |
|---|---|
| Original request | The exact job the student entered the dojo to learn. |
| Coverage ledger | The modes, archetypes, state transitions, dependencies, and risk boundaries the claim actually spans. |
| Scenario ledger | Observable checks and trial counts written before seeing results. |
| Isolation manifest | Allowed roots, candidate visibility, active skill catalog, network policy, canary result, trace availability, and evidence grade. |
| Baseline prompts, outputs, and scores | What an untrained agent already did well—and where it actually fell. |
| Candidate and authoring notes | The smallest technique chosen to answer an observed failure. |
| Skilled runs | Whether the technique fixed that failure without making strong defaults worse. |
| Freeze digest | The exact candidate that entered graduation; no mid-bout coaching allowed. |
| Held-out trials | Predeclared coverage cells materialized by a separate custodian only after freeze. A failed or exposed holdout is burned. |
| Invalid-run ledger | Contamination and harness failures that contribute no score but remain visible. |
| Routing judges | Evidence that the skill enters its own bouts and leaves neighboring skills alone. |
| Package checks and smoke run | Proof that the installable folder is valid, discoverable, and usable cold. |
| Final Dojo record | The honest roll-up: wins, failures, loopholes, limitations, and one terminal verdict. |

Fast Lane compresses these into one lightweight record: exact prompts and
results, affected checks, bounded edits, a fresh different-in-kind check,
applicable routing/package results, limitations, and `FAST-LANE PASS`,
`FAST-LANE FAIL`, or `UNPROVEN`. Audit Lane keeps the complete receipt set.

Raw evidence normally lives under `~/.dojo/`. A checked-in example must first
replace machine paths and runner identities with neutral placeholders. The
receipts should expose the experiment, never the workstation.

---

## Worked Example: Taste Extractor

The example began with this request:

> With Dojo, create a skill that extracts “taste” out of any medium so other
> agents can produce entities of that medium in the same style.

The [side-by-side example index](example/taste-extractor/) keeps the complete
[`v0.1`](example/taste-extractor/v0.1/) and
[`v0.2`](example/taste-extractor/v0.2/) trees intact. In the v0.2 redo, six
no-skill baselines all sounded plausible and all passed their qualitative
gates—yet together they scored only 10/30 on the prewritten implementation
criteria. The final skill scored 30/30. This is why Dojo spars: vibes said
“fine”; the scorecards found twenty missing pieces of traceability, transfer
discipline, and handoff detail.

The first five frozen candidates still did not graduate. Early bouts exposed
an underspecified missing-video intake, principles escaping their evidence
trace, actions escaping their coordinate table, a loose audio request, and
collapsed decision authority. The third freeze passed its fresh holdouts but
then failed the required final training regression. The fourth and fifth found
exact-schema, per-axis-coordinate, and per-cell-quotation gaps. Each miss earned
one bounded rule. The sixth freeze passed three new post-freeze holdouts at 5/5
with every qualitative gate green.

| Stage | Receipt | What Happened |
|---|---|---|
| Intake | [`original-request.md`](example/taste-extractor/v0.2/original-request.md) | Preserves the exact creation prompt. |
| Precommitment | [`taste-extractor-scenarios.md`](example/taste-extractor/v0.2/taste-extractor-scenarios.md) | Declares the claim, six training cells, three holdout shapes, trials, and evidence grade before scoring. |
| Isolation | [`preflight.md`](example/taste-extractor/v0.2/taste-extractor-runs/isolation/preflight.md), [`invalid-runs.md`](example/taste-extractor/v0.2/taste-extractor-runs/isolation/invalid-runs.md) | Shows the three role canaries and keeps overwritten captures and a hidden criterion out of the score. |
| Counterfactual | [`training-scorecard.md`](example/taste-extractor/v0.2/taste-extractor-runs/training/training-scorecard.md), [`training/`](example/taste-extractor/v0.2/taste-extractor-runs/training/) | Preserves all six tasks, criteria, no-skill outputs, final skilled outputs, and the 10/30 → 30/30 result. |
| Corrections | [`corrections/`](example/taste-extractor/v0.2/taste-extractor-runs/corrections/) | Keeps burned-attempt failures and affected-case regressions visible. |
| Candidate | [`authoring-notes.md`](example/taste-extractor/v0.2/candidate/authoring-notes.md), [`SKILL.md`](example/taste-extractor/v0.2/candidate/taste-extractor/SKILL.md), [`FROZEN.md`](example/taste-extractor/v0.2/candidate/FROZEN.md) | Connects every added instruction to an observed miss and pins the final candidate bytes. |
| Graduation | [`held-out-custody.md`](example/taste-extractor/v0.2/taste-extractor-runs/holdouts/held-out-custody.md), [`H16`](example/taste-extractor/v0.2/taste-extractor-runs/holdouts/h16-craft-to-notifications/), [`H17`](example/taste-extractor/v0.2/taste-extractor-runs/holdouts/h17-account-recovery/), [`H18`](example/taste-extractor/v0.2/taste-extractor-runs/holdouts/h18-partial-video-posters/) | Three new post-freeze tasks score 5/5 with qualitative PASS. |
| Routing | [`matrix.md`](example/taste-extractor/v0.2/taste-extractor-runs/routing/matrix.md), [`judge-1.md`](example/taste-extractor/v0.2/taste-extractor-runs/routing/judge-1.md), [`judge-2.md`](example/taste-extractor/v0.2/taste-extractor-runs/routing/judge-2.md), [`routing-score.md`](example/taste-extractor/v0.2/taste-extractor-runs/routing/routing-score.md) | Two clean proxy judges match all 15 declared owners: 30/30 decisions. |
| Package | [`package-checks.md`](example/taste-extractor/v0.2/taste-extractor-runs/package/package-checks.md), [`smoke-output.md`](example/taste-extractor/v0.2/taste-extractor-runs/package/smoke-output.md), [`smoke-score.md`](example/taste-extractor/v0.2/taste-extractor-runs/package/smoke-score.md) | Validates YAML and structure, discovers exactly one skill, invokes it cold, and rechecks the freeze digest. |
| Record | [`taste-extractor-record.md`](example/taste-extractor/v0.2/taste-extractor-record.md) | Rolls up the wins, burned attempts, invalid evidence, limits, and terminal verdict. |

### Taste Extractor v0.1 vs v0.2

**Verdict: v0.2 is the better skill for the promise this example makes.** v0.1
was a good compact extractor; v0.2 is a dependable handoff protocol. The gain
is not more adjectives. It is making source access, recurrence, inference,
authority, and every downstream action inspectable.

This is a comparison of the two finished skill contracts and their receipts,
not a claim that v0.1 scored 10/30: that 10/30 result belongs to the no-skill
baseline. The current campaign did not pretend those are the same control.

| | v0.1 | v0.2 | Why v0.2 is better |
|---|---|---|---|
| Evidence trace | One row for each major principle | Stable IDs for every inference, with every later use linked back | Principles cannot quietly mutate or appear without evidence. |
| Multi-work corpora | Could cite several works | Requires source IDs, recurrence weight, and outlier quarantine | One seductive exception cannot hijack the supposed shared taste. |
| Partial evidence | Strong unavailable-source refusal, but no explicit partial mode | Provisional label, supported-axis accounting, named unknowns, bounded rules | Four stills no longer become imaginary motion or sound. |
| Missing-media intake | General clips, frames, or listening notes | Concrete visual, spatial, material, motion, sound, lawful-audio, and authorized-substitute requirements | The next evidence request is actually sufficient to continue. |
| High-stakes language | Accessibility and correctness outrank style | Errors, identity, consent, fees, security, permissions, and risk stay literal | Extracted voice cannot blur consequential product language. |
| Operational translation | Useful target rules and checks | Complete action register, explicit authorities, handoffs, prohibitions, and uniqueness invariants | Another agent can implement the protocol without reconstructing hidden context. |
| Exact contracts | General output structure | Exact labels, enumerations, state lists, counts, per-row coordinates, and per-cell quotes survive handoff | Dense implementation contracts no longer pass while quietly dropping fields. |
| Evidence behind the claim | Earlier fresh-context campaign | Canary-preflighted roles, six counterfactual pairs, five burned freezes, three final holdouts, routing, and cold smoke | The claim now rests on an auditable v0.2 campaign. |
| Cost | 5,207-byte main skill; 3,723-byte reference | 9,538-byte main skill; 4,107-byte reference | About 53% more instruction material buys the stronger contract. |

v0.1 still wins one narrow contest: it is lighter. If the job is casual
inspiration and nobody downstream needs to audit or implement the result, its
smaller contract may be enough. For “extract from any medium so another agent
can reliably create from it,” v0.2 wins decisively.

The result is not just a taste-extractor skill. It is the skill plus the
training tape, burned belts, scorecards, held-out bouts, routing drill,
equipment check, and the note saying exactly where the black belt still does
**not** apply.

---

## Dojo vs. A Generic Skill-Creation Framework

There is real overlap: Dojo is excellent at creating skills. It can begin with
a one-line idea, design scenarios, observe the baseline, author the skill, and
iterate it into shape. The difference is not “creation versus testing.” It is
where the creation loop stops and what evidence survives it.

| | Generic skill-creation framework | Dojo |
|---|---|---|
| Starting point | An idea, task, or existing draft | An idea, task, existing draft, or released skill |
| Creation method | Apply authoring patterns, examples, and structural guidance | Observe untrained behavior, then write the smallest technique justified by the failure |
| Iteration | Improve the skill until its instructions look and feel ready | Preserve raw attempts, make bounded edits, and rerun the affected bout |
| Quality checks | Structure, clarity, examples, and authoring conventions | Those checks plus baselines, regression runs, held-out trials, routing, and package smoke |
| Receipts | Often the finished skill and perhaps examples | Prompts, outputs, scores, freeze, holdouts, judges, package checks, and final record |
| Finish line | A well-formed, useful skill | A useful skill with tier-appropriate evidence for what it can—and cannot—claim |

Both can teach a skill. Dojo keeps the mats, sparring partners, scorecards, and
graduation bout around long enough to show how the student earned the belt.

---

## The Seven Kata

| Kata | What Happens On The Mat |
|---|---|
| Intake | Bow in. Name the claim, the tier, and the observable win condition. |
| Baseline | Let the untrained version onto the mat. Where does it fall? |
| Write | Teach the smallest technique that answers the observed failure. |
| Pressure | Spar against shortcuts, rationalization, time, sunk cost, and authority. |
| Graduation | Freeze first; then a separate custodian materializes held-out opponents for the predeclared trials. A failed holdout is burned, not rehearsed. |
| Trigger eval | Enter the right bouts without stealing a neighboring skill's match. |
| Package | Fold the gi, check the bag, and leave a clean evidence record. |

The metaphor stops where the evidence starts: Dojo uses yes/no process
observations and exact routing results. It does not invent a quality score for
work that has no real grader.

The tier controls which kata apply. Reference skills get source-backed
correctness, trigger, and package checks. Technique skills add baseline and
held-out behavior. Discipline skills also get separate time, sunk-cost, and
authority pressure runs. Narrow edits rerun only the affected gate.

The lane controls how strongly those results may be claimed. Fast Lane uses
fresh instruction-bounded runners and stays non-graduation evidence. Audit Lane
adds the boundary and custody work required for a black belt.

---

## Isolation Matters

A fresh mind is not a locked room. A new subagent can still search sibling
fixtures, prior runs, authoring notes, installed skill metadata, and the
candidate itself.

| Grade | What the runner receives | What Dojo may claim |
|---|---|---|
| **Audited instruction-bounded** | A fresh context, exact read/write envelope, unique folder, canary preflight, and inspected trace/path audit | Clean baseline, pressure, and graduation evidence |
| **Fresh-context only** | A new context without a verified information boundary | Exploratory behavior only |
| **Degraded local** | The authoring context reviews itself | Static findings only |

Capability prompting matters. In the v0.2 validation, an unbounded control
retrieved a forbidden random canary, while five fresh instruction-bounded
trials—including urgency and an in-file attempt to expand scope—stayed inside
their assigned folders. A compact rerun against the current contract then held
3/3 boundaries under parent-search, urgent-authority, and explicit broad-search
pressure. The result validates capability envelopes as Dojo's portable audited
boundary. See
[`evidence/isolation-validation.md`](evidence/isolation-validation.md).

Every behavioral run is `PASS`, `FAIL`, or `INVALID`. Contamination is invalid
evidence, not a known limitation attached after graduation.

---

## Evidence Lives Outside The Project

Raw runs stay out of the repository by default:

```text
~/.dojo/<repo-slug>/<skill>/
  <skill>-scenarios.md
  <skill>-runs/
  <skill>-record.md
```

`repo-slug` comes from the repository directory name, normalized to lowercase
letters, digits, and hyphens. A short path hash disambiguates collisions. For
example, a `csv-tools` repository testing `csv-import` writes under
`~/.dojo/csv-tools/csv-import/`.

Dojo resolves the repository root from the candidate skill directory with Git.
For a non-Git candidate it uses an explicitly declared containing project, or
the candidate directory itself—not the agent's ambient working directory. It
canonicalizes that root by resolving symlinks and dot segments, using an
absolute path with `/` separators, and lowercasing only a Windows drive letter.
The collision suffix starts with the first eight lowercase hex characters of
SHA-256 over that UTF-8 string and extends four characters at a time if needed.
An ownership mismatch at the full digest fails closed rather than sharing
evidence.

Raw prompts and outputs may contain sensitive task material. Dojo does not
upload or automatically expire them. Review the directory before sharing it;
remove the corresponding `~/.dojo/<repo-slug>/<skill>/` tree when its retention
period ends. Dojo adds no encryption or permission layer; files inherit the
operating system account and umask. The host may send prompts, source material,
and outputs to one or more model contexts; provider handling and retention are
governed by the host, not Dojo.

Only a curated, leak-checked record belongs in a public repository. The v0.2
targeted validation is in
[`evidence/dojo-v0.2-change-record.md`](evidence/dojo-v0.2-change-record.md),
with its canary experiment in
[`evidence/isolation-validation.md`](evidence/isolation-validation.md). The
historical promotion summary remains in
[`evidence/dojo-record.md`](evidence/dojo-record.md), with curated scenarios and
routing expectations in [`evidence/eval-fixtures.md`](evidence/eval-fixtures.md).
Raw outputs remain local. Those v1 runs predate the v0.2 isolation grades and
are classified as fresh-context-only evidence rather than retroactively claimed
as audited transcripts.

The reported counts are curator-attested summaries, not independently
reproducible benchmark results. The fixtures disclose the prompts, checks, and
routing expectations; raw run outputs stay local.

Dojo prefers the host's real dispatcher for trigger evidence. When none is
callable, it uses two independent routing judges and labels the result as a
proxy.

---

## What Dojo Is Not

- Not a replacement for every skill creator or scaffolder.
- Not a generic document or code reviewer.
- Not a benchmark generator that turns subjective taste into fake precision.
- Not proof when the run reused contaminated context.

Dojo is the trust gate between “this instruction sounds plausible” and “this
behavior has survived contact with reality.”

---

## Repository Layout

```text
skills/dojo/                         installable Agent Skill
skills/dojo/assets/harness-template/ optional complex Audit Lane template
skills/dojo/scripts/dojo_harness.py  portable contract validator
evidence/                            curated evidence and validation records
example/taste-extractor/v0.1/        historical compact campaign
example/taste-extractor/v0.2/        audited expanded campaign
tests/test_dojo_harness.py            focused validator regressions
docs/assets/                         repository artwork
```

---

## License

MIT © 2026 Andre Ratzenberger

---

## Changelog

### 0.3.0 — 2026-07-16

- Added Fast Lane and Audit Lane with a compact default comparison and an
  automatic recommendation that does not pause for ceremony.
- Added deterministic `--lane auto|fast|audit`, compatibility aliases, and
  `--quiet` for exact-output automation and benchmark matrices.
- Added the interactive milestone/ETA ticker without contaminating finals,
  runner output, evidence, or machine-readable artifacts.
- Added a complexity-triggered portable Audit Lane harness for hidden
  evaluator material, dependency closure, trace-derived receipts, and external
  artifact hashes.
- Rejected nested symlink leakage, empty required telemetry, undeclared events,
  host allowlist bypasses, traversal references, malformed artifact roots, and
  timestamp reversal with focused standard-library regressions.

### 0.2.0 — 2026-07-16

- Added audited instruction-bounded, fresh-context-only, and degraded evidence
  grades.
- Added run capsules, capability envelopes, canary preflights, path/tool
  audits, and the `INVALID` contamination state.
- Replaced the fixed behavior battery with coverage- and risk-scaled scenario
  and trial budgets.
- Separated candidate authoring from post-freeze holdout custody and added
  deterministic tier, narrow-edit, reference-review, and release verdict rules.
- Self-tested the contract against its released version, preserved two strong
  defaults, corrected seven gaps, passed all three pressure variants, and
  rejected contaminated evidence in unseen trials.
- Reclassified the original checked-in campaigns as historical v1 evidence.
- Rebuilt Taste Extractor under v0.2, preserved five burned freezes, graduated
  the sixth on three fresh 5/5 holdouts, and compared it honestly with v0.1.
- Preserved both complete campaigns under side-by-side `v0.1/` and `v0.2/`
  folders with an artifact-level comparison index.

See [`CHANGELOG.md`](CHANGELOG.md) for the complete release history.

---

## Dojo Put Itself On The Mat

**v0.3 focused change: PASS.** Dojo exercised its own lane selectors, progress
tracker, no-spelunk boundary, and portable validator before presenting them as
the new default.

| v0.3 check | Result |
|---|---:|
| Auto, explicit, alias, quiet, and conflicting selector behavior | **5/5** |
| Fresh Fast Lane no-spelunk calibration | **boundary held** |
| Audited lane-contract calibration | **boundary held** |
| Intermediate updates with ticker / final answers with ticker | **3/3 / 0/1** |
| Portable harness regressions | **11/11** |
| Bundled run and package preflights | **2/2** |

The first audited run also caught an invocation ambiguity: a runner tried to
find a `dojo` executable. The bounded fix made lane arguments explicitly
prompt-level, and a clean regression parsed them without probing for a CLI.
Read the scoped receipt in
[`evidence/dojo-v0.3-change-record.md`](evidence/dojo-v0.3-change-record.md).

**v0.2 foundation: APPROVED.** Dojo compared its released contract with the
new candidate, tested the changed behavior under pressure, and made
contamination handling survive unseen cases.

| Self-test result | Score |
|---|---:|
| Released behaviors corrected | **7** |
| Strong released defaults preserved | **2** |
| Time, sunk-cost, and authority pressure variants | **3/3 at 5/5** |
| Audited capability-envelope calibrations | **5/5 boundaries held** |
| Current-contract boundary proof | **3/3 boundaries held** |
| Unseen evidence-integrity decisions | **3/3 satisfy the current five checks** |
| Contaminated runs counted as evidence | **0** |

The unseen evidence-integrity case mixed two clean trials with one scorer-
contaminated trial. Every independent runner preserved the clean observations,
marked the contaminated trial `INVALID`, required a fresh replacement, and
withheld graduation until the missing evidence exists. That is the behavior
Dojo exists to produce. Read the complete curated receipt in
[`evidence/dojo-v0.2-self-test.md`](evidence/dojo-v0.2-self-test.md).
