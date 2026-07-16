# Packaging And Evidence

## Installed Skill Folder

Keep the installable unit lean:

```text
<skill-name>/
  SKILL.md
  agents/openai.yaml      # optional host metadata
  references/             # optional, loaded on demand
  scripts/                # only for deterministic repeated work
  assets/                 # only when consumed by the skill
```

Keep repository README files, contribution docs, and evaluation history
outside the installable skill folder.

## Portability Rules

- Use Agent Skills terminology rather than assuming one agent product.
- Name host-specific capabilities and provide a degraded path.
- Do not hardcode plugin manifests, reload commands, private paths, or a
  developer's home directory.
- Keep state outside the target project unless the user explicitly requests
  checked-in artifacts.
- Document external tools or network requirements before using them.

## Validation Gate

Before release:

1. Parse the YAML frontmatter with a real parser or the host validator.
2. Confirm `name` matches the skill directory and contains only lowercase
   letters, digits, and hyphens.
3. Confirm `description` is a non-empty string under 1024 characters and says
   both what the skill does and when to use it.
4. Confirm every referenced file exists and can be found directly from
   `SKILL.md`.
5. Search for private paths, credentials, internal repository names, and stale
   host-specific assumptions.
6. Smoke-invoke the installed folder from a clean context.
7. Run the trigger matrix against the current active skill landscape for full
   campaigns and whenever the Narrow Edit Mapping in `SKILL.md` makes routing
   applicable. Otherwise record the exact skip rationale.
8. Verify the record distinguishes audited instruction-bounded,
   fresh-context-only, and degraded evidence without upgrading the claim.

## Runtime Evidence

Store raw evidence under:

```text
~/.dojo/<repo-slug>/<skill>/
  <skill>-scenarios.md
  <skill>-runs/
    README.md
    <run-name>/
  <skill>-record.md
```

Preserve prompts and outputs verbatim. Leak-check before copying curated proof
into a public repository. The orchestrator moves outputs into this tree only
after each runner stops; runners do not share or browse the evidence root.

Place these exact identity fields immediately after the H1 in both
`<skill>-scenarios.md` and `<skill>-record.md`, before any other metadata or
campaign prose:

```text
Repository root: <normalized absolute root>
Root resolution: <git|declared-project|candidate-fallback>
Repository slug: <resolved slug, including collision suffix when present>
Candidate skill path: <normalized absolute path>
```

## Candidate Freeze Identity

Freeze the entire installable candidate directory with one reproducible
content digest. Do not use a Git commit, timestamp, archive byte stream, or an
unspecified “immutable identifier” as the candidate revision.

1. Reject symlinks and special files; materialize any required content as
   regular files before graduation.
2. Enumerate every regular file recursively. Require UTF-8 relative paths,
   render separators as `/`, and sort by the raw UTF-8 path bytes.
3. Initialize SHA-256 and feed the bytes `dojo-candidate-v1` followed by one
   NUL byte.
4. For each file, feed ASCII decimal byte-length of the path, `:`, the path
   bytes, ASCII decimal content-length, `:`, and the exact file bytes.
5. Record the lowercase hexadecimal digest plus a manifest containing each
   relative path, byte length, and per-file SHA-256.

File modes, mtimes, ownership, and the enclosing Git state are not part of this
content identity. Validate executable behavior separately in package smoke.
Recompute the digest before and after every graduation trial and the final
smoke run. A mismatch closes the attempt as `UNPROVEN`; the changed tree is a
new candidate revision.

## Record Template

```markdown
# Dojo record — <skill>

Repository root: <normalized absolute root>
Root resolution: <git|declared-project|candidate-fallback>
Repository slug: <resolved slug>
Candidate skill path: <normalized absolute path>

*Tier: <discipline|technique|reference> · <date> · <host/model> · isolation: <grade>*

Candidate revision: sha256:<lowercase candidate-manifest digest>
Graduation attempt: <attempt identifier or not applicable>

## Claim And Evidence Label

Claim: <the behavior this campaign supports>
Evidence: <audited instruction-bounded | exploratory | static>

## Isolation Manifest

Campaign isolation grade: <weakest supporting role grade>

| Role/config ID | Context and boundary | Allowed reads/writes | Candidate/catalog visibility | Network/memory | Canary | Trace/path audit | Grade | Status |
|---|---|---|---|---|---|---|---|---|
| custodian-... | ... | ... | ... | ... | ... | ... | ... | PASS/INVALID |
| runner-... | ... | ... | ... | ... | ... | ... | ... | PASS/INVALID |
| grader-... | ... | ... | ... | ... | ... | ... | ... | PASS/INVALID |

Add a row for every distinct evidence-bearing role configuration and link each
run to its configuration ID. State the weakest-grade calculation explicitly.

## Coverage Ledger

| Claim cell | Training scenario | Holdout | Trials | Risk |
|---|---|---|---:|---|

## Run Ledger

| Run | Status | Isolation grade | Result | Notes |
|---|---|---|---|---|

Statuses are `PASS`, `FAIL`, or `INVALID`. Invalid runs contribute no score.

## Qualitative judgment gate

Authority: <named human/reviewer | not applicable>
Rubric precommitted: <location or not applicable>
Blinding: <method | unavailable with reason | not applicable>
Decision: <pass/fail/unproven/not applicable>
Notes: <...>

## Baseline findings

| Scenario | Baseline | Skilled | Contribution |
|---|---|---|---|

## Reference correctness

| Claim ID | Exact claim | Authority and version | Check performed | Status | Notes |
|---|---|---|---|---|---|

Use for reference campaigns; otherwise state `not applicable` with the tier
rationale.

## Loopholes closed

| # | Loophole | Bounded edit |
|---|---|---|

## Rejected fixes

| # | Attempt | Why it was rejected |
|---|---|---|

## Graduation

| Holdout | Required trials | Result | Isolation grade | Notes |
|---|---:|---|---|---|

## Invalid Or Burned Evidence

| Run or holdout | Why invalid/burned | Replacement |
|---|---|---|

## Trigger matrix

| # | Prompt | Expected | Actual | Pass |
|---|---|---|---|---|

## Known limitations

- ...

## Verdict

`GRADUATED | NOT GRADUATED | UNPROVEN`

Reason: <mandatory gates and bounded claim>
```

Keep non-applicable sections with an explicit rationale rather than deleting
them.

## Terminal Verdict Gate

Record exactly one terminal outcome for the identified candidate revision and
its latest graduation attempt:

Do not shorten that scope to the candidate digest alone. Whenever the procedure
or answer explains verdict scope, state both parts explicitly: the verdict is
for the immutable candidate revision's latest applicable attempt, and evidence
from older revisions or attempts is preserved as history without counting as a
current gate.

- **GRADUATED** — every applicable training/correctness, pressure, held-out,
  trigger, validation, and smoke gate passes; required traces exist; no
  unresolved invalid run contributes; and at least one bounded value claim is
  supported (`corrected`, demonstrated reliability, routing value, or another
  predeclared contribution).
- **NOT GRADUATED** — valid current-attempt evidence contains a failing
  mandatory gate. Record the failure or burned holdout and the next bounded
  iteration.
- **UNPROVEN** — a mandatory gate is absent or invalid, isolation cannot support
  the claim, the baseline counterfactual is unavailable without an alternative
  value test, or required authority is missing.

Tier applicability comes from `SKILL.md`. Known limitations may reduce the
claim's scope but cannot turn a failed, missing, or invalid gate into a pass.
Preserve earlier candidate revisions, failed attempts, and burned holdouts in
the chronological ledger. Once replaced, they explain history but do not count
as current gates for a later immutable revision and attempt.
