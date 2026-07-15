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
7. Run the trigger matrix against the current active skill landscape.

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
into a public repository.

Start both `<skill>-scenarios.md` and `<skill>-record.md` with these exact
identity fields:

```text
Repository root: <normalized absolute root>
Root resolution: <git|cwd-fallback>
Repository slug: <resolved slug, including collision suffix when present>
```

## Record Template

```markdown
# Dojo record — <skill>

*Tier: <discipline|technique|reference> · <date> · <host/model>*

Repository root: <normalized absolute root>
Root resolution: <git|cwd-fallback>
Repository slug: <resolved slug>

## Baseline findings

| Scenario | Failure mode |
|---|---|

## Loopholes closed

| # | Loophole | Bounded edit |
|---|---|---|

## Rejected fixes

| # | Attempt | Why it was rejected |
|---|---|---|

## Graduation

| Holdout | Result | Notes |
|---|---|---|

## Trigger matrix

| # | Prompt | Expected | Actual | Pass |
|---|---|---|---|---|

## Known limitations

- ...
```

Keep non-applicable sections with an explicit rationale rather than deleting
them.
