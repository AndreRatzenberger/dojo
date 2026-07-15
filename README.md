<p align="center">
  <img alt="Dojo banner" src="docs/assets/dojo-banner.png" width="900">
</p>

<p align="center">
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/Agent%20Skill-open%20format-43d9ad.svg" alt="Open Agent Skill"></a>
  <a href="evidence/dojo-record.md"><img src="https://img.shields.io/badge/evidence-curated%20record-f0a54b.svg" alt="Curated evidence record"></a>
  <a href="skills/dojo/SKILL.md"><img src="https://img.shields.io/badge/output-~%2F.dojo-9b7bff.svg" alt="Output under ~/.dojo"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
</p>

<p align="center">
  <em>"black belts are earned, not declared"</em>
</p>

**Dojo trains your skills for the black belt.**

A rough idea can enter in a white belt. Dojo first watches the untrained agent,
then writes the smallest useful technique, spars against the failure, and keeps
training until the skill is ready for sealed graduation. An existing skill can
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
for a user-level installation. While this repository is private, GitHub access
to it is required.

---

## Enter The Dojo

Graduation-grade evidence requires a host that can launch fresh subagents or
separate clean sessions. Without either, Dojo performs degraded static review
and must not claim baseline, pressure, or graduation evidence.

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
| Scenario ledger | Claims, tier, and observable checks written before seeing results. |
| Baseline prompts, outputs, and scores | What an untrained agent already did well—and where it actually fell. |
| Candidate and authoring notes | The smallest technique chosen to answer an observed failure. |
| Skilled runs | Whether the technique fixed that failure without making strong defaults worse. |
| Freeze digest | The exact candidate that entered graduation; no mid-bout coaching allowed. |
| Sealed holdouts | One-shot tests of transfer beyond the training examples. A failed one is burned. |
| Routing judges | Evidence that the skill enters its own bouts and leaves neighboring skills alone. |
| Package checks and smoke run | Proof that the installable folder is valid, discoverable, and usable cold. |
| Final Dojo record | The honest roll-up: wins, failures, loopholes, limitations, and graduation result. |

Raw evidence normally lives under `~/.dojo/`. A checked-in example must first
replace machine paths and runner identities with neutral placeholders. The
receipts should expose the experiment, never the workstation.

---

## Worked Example: Taste Extractor

The example began with this request:

> With Dojo, create a skill that extracts “taste” out of any medium so other
> agents can produce entities of that medium in the same style.

That sentence became a complete technique-tier run in
[`example/taste-extractor/`](example/taste-extractor/). The baselines were
awkward in the most useful way: three already passed. Dojo did not manufacture
problems to look busy. The prose case scored 4/5 because its principles lacked
a source-by-source evidence trace; the candidate added a mandatory Taste Trace
and brought that case to 5/5 while preserving the others.

| Stage | Receipt | What Happened |
|---|---|---|
| Intake | [`original-request.md`](example/taste-extractor/original-request.md) | Preserves the exact creation prompt. |
| Precommitment | [`taste-extractor-scenarios.md`](example/taste-extractor/taste-extractor-scenarios.md) | Defines four training cases and their checks before any run. |
| Baseline | [`t1-interface/`](example/taste-extractor/taste-extractor-runs/t1-interface/), [`t2-prose/`](example/taste-extractor/taste-extractor-runs/t2-prose/), [`t3-cross-medium/`](example/taste-extractor/taste-extractor-runs/t3-cross-medium/), [`t4-missing-source/`](example/taste-extractor/taste-extractor-runs/t4-missing-source/) | Keeps every raw prompt, raw output, and criterion-level score before and after training. |
| Write | [`authoring-notes.md`](example/taste-extractor/candidate/authoring-notes.md) and [`SKILL.md`](example/taste-extractor/candidate/taste-extractor/SKILL.md) | Shows why the Taste Trace was the smallest justified instruction. |
| Freeze | [`FROZEN.md`](example/taste-extractor/candidate/FROZEN.md) | Seals the candidate tree before either holdout is opened. |
| Graduation | [`sealed-holdouts.md`](example/taste-extractor/taste-extractor-runs/holdouts/sealed-holdouts.md), [`holdout-1-score.md`](example/taste-extractor/taste-extractor-runs/holdouts/holdout-1-score.md), [`holdout-2-score.md`](example/taste-extractor/taste-extractor-runs/holdouts/holdout-2-score.md) | Transfers choreography into a decision protocol and a field-guide system into an IVR; both pass 5/5 once. |
| Routing | [`matrix.md`](example/taste-extractor/taste-extractor-runs/routing/matrix.md), [`judge-1.md`](example/taste-extractor/taste-extractor-runs/routing/judge-1.md), [`judge-2.md`](example/taste-extractor/taste-extractor-runs/routing/judge-2.md), [`routing-score.md`](example/taste-extractor/taste-extractor-runs/routing/routing-score.md) | Two isolated proxy judges match all 15 declared owners: 30/30 decisions. |
| Package | [`package-checks.md`](example/taste-extractor/taste-extractor-runs/package/package-checks.md), [`smoke-output.md`](example/taste-extractor/taste-extractor-runs/package/smoke-output.md), [`smoke-score.md`](example/taste-extractor/taste-extractor-runs/package/smoke-score.md) | Validates the folder, discovers exactly one skill, and invokes it cold. |
| Record | [`taste-extractor-record.md`](example/taste-extractor/taste-extractor-record.md) | Rolls up the evidence and keeps the limitations visible. |

The result is not just a taste-extractor skill. It is the skill plus the
training tape, scorecards, sealed bouts, routing drill, equipment check, and
the note saying exactly where the black belt still does **not** apply.

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
| Quality checks | Structure, clarity, examples, and authoring conventions | Those checks plus baselines, regression runs, sealed holdouts, routing, and package smoke |
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
| Graduation | Face sealed opponents once. A failed holdout is burned, not rehearsed. |
| Trigger eval | Enter the right bouts without stealing a neighboring skill's match. |
| Package | Fold the gi, check the bag, and leave a clean evidence record. |

The metaphor stops where the evidence starts: Dojo uses yes/no process
observations and exact routing results. It does not invent a quality score for
work that has no real grader.

The tier controls which kata apply. Reference skills get source-backed
correctness, trigger, and package checks. Technique skills add baseline and
held-out behavior. Discipline skills also get separate time, sunk-cost, and
authority pressure runs. Narrow edits rerun only the affected gate.

---

## Isolation Matters

The strongest run uses a fresh subagent for every scenario. Separate clean
sessions are an acceptable fallback. A same-context self-review may still find
useful issues, but Dojo marks it as degraded and never calls it graduation.

That boundary is important: clean-looking output is not clean evidence.

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

Dojo resolves the repository root with Git when available and otherwise uses
the current working directory, recording the fallback. It canonicalizes that
root by resolving symlinks and dot segments, using an absolute path with `/`
separators, and lowercasing only a Windows drive letter. The collision suffix
starts with the first eight lowercase hex characters of SHA-256 over that UTF-8
string and extends four characters at a time if needed. An ownership mismatch
at the full digest fails closed rather than sharing evidence.

Raw prompts and outputs may contain sensitive task material. Dojo does not
upload or automatically expire them. Review the directory before sharing it;
remove the corresponding `~/.dojo/<repo-slug>/<skill>/` tree when its retention
period ends. Dojo adds no encryption or permission layer; files inherit the
operating system account and umask. The host may send prompts, source material,
and outputs to one or more model contexts; provider handling and retention are
governed by the host, not Dojo.

Only a curated, leak-checked record belongs in a public repository. This repo's
promotion record is in [`evidence/dojo-record.md`](evidence/dojo-record.md),
with curated scenarios and routing summaries in
[`evidence/eval-fixtures.md`](evidence/eval-fixtures.md). Raw outputs remain
local, so the checked-in evidence is a curated run record rather than a signed
transcript.

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
skills/dojo/       installable Agent Skill
evidence/          curated graduation record
example/           sanitized, receipt-complete worked example
docs/assets/       repository artwork
```

---

## License

MIT © 2026 Andre Ratzenberger
