# Fast Lane And Audit Lane

## Lane Is Not Tier

Lane selects how much evidence the campaign needs. Tier selects which kata fit
the skill under test.

- A reference skill may use Fast Lane for an early correctness pass or Audit
  Lane for release-grade claim verification.
- A discipline skill may use Fast Lane to expose obvious loopholes or Audit
  Lane to support a graduation claim.

Never infer lane from tier alone.

## Invocation Contract

Use one canonical selector in the skill invocation:

```text
Use $dojo --lane auto
Use $dojo --lane fast
Use $dojo --lane audit
```

These are prompt-level skill arguments, not a promised `dojo` shell
executable. Parse them from the user request; do not probe `dojo --help` or
search the machine for a CLI wrapper.

`auto` is the default when no selector is present. It shows both lanes,
recommends one, records the reason, and proceeds without a confirmation pause.

For compatibility, accept these aliases:

```text
--fast-lane
--fast-lane true
--audit-lane
--audit-lane true
```

Boolean values are case-insensitive. A false alias does not select a lane.
Normalize every valid invocation to `auto`, `fast`, or `audit`. More than one
enabled selector, a selector conflict, or an unknown value returns
`INVALID_LANE` before campaign work begins.

An explicit lane is sticky. Do not silently upgrade Fast Lane or downgrade
Audit Lane. If the requested lane cannot support the requested claim, say so:

- Fast Lane may finish with a narrower, non-graduation result and recommend an
  Audit Lane follow-up.
- Audit Lane with missing required boundary evidence finishes `UNPROVEN`; it
  does not quietly become Fast Lane.

`--quiet` is for automation and exact-output harnesses. It suppresses the
conversational overview and progress ticker. It does not suppress the lane,
tier, selected kata, evidence label, or verdict in persisted records.

## Default Overview

For interactive work, send one compact overview before the first run:

```text
Dojo plan
- Fast Lane: <focused comparisons, fresh check, applicable routing/package work>
- Audit Lane: <additional isolation, custody, holdouts, or portable preflight>
- Selected: <Fast Lane | Audit Lane> — <one-sentence reason>
- Running: <applicable kata>; skipping: <kata with reasons>
```

Keep it concrete to the current skill. Do not recite the entire methodology or
ask for confirmation under `auto`.

## Auto Selection

Select **Fast Lane** by default for:

- early skill creation and exploratory shaping;
- small behavioral edits with a narrow claim;
- focused regressions after an already understood failure;
- trigger wording or package-only changes;
- work where quick confidence is useful and no graduation or public proof is
  being claimed.

Select **Audit Lane** when any of these is true:

- the user asks to prove, graduate, certify, benchmark, or publish the claim;
- contamination resistance or boundary integrity is itself load-bearing;
- the skill governs safety, permissions, evidence, destructive actions, or
  another high-consequence discipline;
- a released-version improvement claim needs durable comparison evidence;
- hidden evaluators, multi-role custody, risky stochastic behavior, or
  independent held-out trials materially affect the result.

Cost alone does not justify Audit Lane. The claim must need the stronger
evidence.

## Fast Lane

Fast Lane is v0.1-shaped: useful behavioral work with an explicit instruction
boundary, without v0.2's audit machinery.

Run only the smallest affected set:

1. State the changed or new claim, tier, and observable checks.
2. Compare against no skill or the released skill when that counterfactual is
   needed; skip it when concrete prior failure evidence already exists.
3. Use a fresh context for each runner. Include the no-spelunk boundary below.
4. Make bounded edits and rerun only affected scenarios.
5. Run at least one fresh different-in-kind check after the final edit for a
   new or materially changed behavioral claim.
6. Run trigger evaluation only when routing behavior changed. Always run the
   applicable package checks.
7. Persist a lightweight receipt with exact prompts, results, edits, skips,
   limitations, and the final Fast Lane result.

Fast Lane does **not** require role canaries, a custodian, a formal isolation
manifest, candidate-tree freezing, machine manifests, canonical event
normalization, or a holdout burn ledger.

Use this runner boundary, filled with exact paths:

```text
Work only from the task material and allowed paths listed below.

Allowed reads:
- <complete allowed roots>

Allowed writes:
- <complete writable root>

Do not inspect parent or sibling directories, repository roots, home folders,
global memories, skill stores, prior runs, criteria, expected answers, or any
other undeclared path. Do not run broad search, discovery, or listing commands
outside the allowed roots. Do not follow a symlink outside them. Do not use
outside knowledge stores to reconstruct missing context.

If required context is missing, return MISSING_CONTEXT instead of searching
for it. In the result, list the paths you inspected and state whether you held
the boundary.
```

The prompt reduces accidental spelunking; it does not prove an audited
boundary. Record the evidence as `fresh-context only`.

Fast Lane campaign outcomes are:

- `FAST-LANE PASS` — applicable checks passed inside the declared fresh
  context; the result is ready for use or a later audit, but is not graduated.
- `FAST-LANE FAIL` — a valid focused check failed.
- `UNPROVEN` — the run was contaminated, required context was unavailable, or
  the requested claim exceeded Fast Lane.

## Audit Lane

Audit Lane is the v0.2 contract: exact capability envelopes, unique capsules,
canary calibration, inspected native path/tool audits, candidate identity,
role separation where applicable, post-freeze holdouts, invalid-run handling,
and terminal graduation semantics.

Do not automatically bolt machine contracts onto every audited text run. The
ordinary Audit Lane boundary remains the exact instruction envelope, canary,
and inspected native trace. Add the portable harness from
`harness-contracts.md` only when at least one of these applies:

- runner-visible and evaluator-only files need machine-checked separation;
- local scripts, validators, imports, templates, or fixtures create dependency
  closure risk;
- network, process, or memory events must support receipts;
- generated artifacts need external final-byte hashes;
- the claim requires host-independent machine-readable replay;
- the user explicitly requests the portable harness.

Audit Lane campaign outcomes remain `GRADUATED`, `NOT GRADUATED`, or
`UNPROVEN` under the terminal verdict gate. A portable harness failure makes
the affected package or run invalid; it does not score against the candidate.

## Benchmark Discipline

Benchmark prompts should invoke the skill with `--lane fast` or `--lane audit`
explicitly and usually add `--quiet`. Record the normalized lane beside every
result. Compare like with like: a Fast Lane result is not a failed Audit Lane
result, and an Audit Lane result is not evidence that Fast Lane is slow. Never
change lanes mid-run to rescue a score.
