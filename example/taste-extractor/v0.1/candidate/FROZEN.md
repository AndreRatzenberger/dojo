# Candidate freeze

Frozen after the four skilled training runs and before opening either holdout.

Tree digest algorithm:

```text
sha256(concatenated sorted sha256sum lines for every candidate file)
```

Frozen tree digest:

```text
01117cd40581534f188dc93461d53e96740ddd0d95815e23119853afc74d6643
```

The original graduation command included local absolute filenames in the
concatenated `sha256sum` lines. That digest pins the local run, but it is not
relocation-stable. The skill files also have these path-independent hashes:

```text
e63a56103dbabc0fa9380b9c6ce60edb6736aa44280864d5b2b80037f3e042b2  SKILL.md
59c8599c09abce4eb63a5295fd692ab9e9f208ead60050ea1ecffb97961b613f  agents/openai.yaml
8a3ef8d4d5d6e2f1c40ba017b33536fffe0561b03b58123c06e1848b93df537f  references/taste-profile.md
```

Hashing those sorted manifest lines produces the portable content digest:

```text
62704fed613ecb6751e106e20b1e98e133ad802882edf0028d73445483409cdd
```

No candidate edit is permitted between holdout runs. If a holdout fails, it is
burned and a new graduation attempt requires a new freeze and new holdout.
