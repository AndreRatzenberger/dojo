# Native Skill Authoring

Dojo can create and revise the installed skill itself. No external creator is
required. Reuse an existing creator only when it supplies a needed capability;
do not stack a second planning or evaluation process on top of this one.

## Make The Job Concrete

From the request and available examples, name the trigger, expected result,
inputs, and meaningful constraints. Ask only for missing information that
changes the behavior. A useful draft can start from one representative task;
do not turn intake into a questionnaire or manufacture a specification tree.

Choose the lane and tier using `SKILL.md`. Declare checks before outputs exist.
For an edit, preserve the original complete package before touching it and use
that revision as the baseline. For a new skill, run the same task without it.
Existing successful behavior is worth preserving; a passing baseline is not
evidence of a correction. Use the selected lane's runner boundary throughout.

For interactive creation or a substantive revision, open the local workbench
using [workbench.md](workbench.md). Record the actual activity before each
meaningful step, including why it is necessary. Keep the workbench outside the
candidate directory so its records cannot become part of an installed skill.

## Write The Smallest Useful Package

Start with `<skill-name>/SKILL.md`. Use a lowercase hyphenated name and a
description that says what it does and when it should activate. A new package
can use this frontmatter; a JSON-quoted description is also valid YAML:

```yaml
---
name: release-notes
description: "Write release notes from supplied changes when asked to summarize a release for users."
---
```

Give the agent the task-specific decisions, constraints, and output shape that
the observed failures require. Explain consequential rules briefly. Leave
general coding, planning, and prose competence to the host model.

- Add a linked `references/` file only for conditional detail or domain facts.
- Add a `scripts/` helper only for repeated deterministic work, and execute it.
- Add `assets/` only for material the skill actually consumes.
- Keep examples, experiments, and development receipts out of the package.

When improving an existing skill, retain supported metadata, host settings,
working references, and useful assets. Do not flatten YAML or delete resources
to satisfy a limited parser. Read referenced resources before changing the
instructions that consume them. Update optional `agents/openai.yaml` if the
visible name, description, or default invocation changes; it is not required
for hosts that do not use it.

## Validate, Compare, Revise

Run the bundled validator from its actual installed location:

```bash
python3 <installed-dojo>/scripts/dojo_harness.py validate-skill <candidate-directory>
```

It checks the package name, description, body, regular files, and Markdown
local references without changing them. With PyYAML already available it
parses full YAML; without it, it accepts the native two-field quoted form.
Other YAML returns `UNPROVEN` (exit 2), not `FAIL` (exit 1). Preserve the package
and use an available host or YAML-capable validator. Do not install a dependency
or rewrite valid metadata merely to turn an unknown result green. `PASS`
(exit 0) is a structural check, not evidence of useful behavior or host routing.

Snapshot the candidate, run the declared cases in fresh contexts, and inspect
actual outputs. In the workbench, connect each completed candidate run to its
revision and record evidence for each check. A helper can store a check result;
it cannot establish that the grader was right.

Invite feedback on the displayed outputs. Read saved feedback through the CLI,
make one bounded revision that addresses it, snapshot with a reason, and rerun
affected cases. Preserve earlier attempts. Silence or an empty comment is not
acceptance; a required human judgment stays `UNPROVEN` until supplied. The
`looks-good` action is a human review, not an automatic campaign verdict.

Finish with the selected lane's fresh check or graduation, applicable routing
and package checks, and a receipt. State the installed candidate path, observed
improvement or preservation, known limitations, and whether human review is
still pending. Do not create downstream copies or publish packages implicitly.
