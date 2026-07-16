# Candidate freeze

Final graduation attempt: `taste-v02-a6`

The entire installable candidate directory was frozen before the final
holdout custodian materialized H16-H18.

## Content identity

Dojo's candidate digest feeds `dojo-candidate-v1`, a NUL byte, and then each
regular file's sorted relative path length, path bytes, content length, and
exact content bytes into SHA-256.

Final tree digest:

```text
b5ade59ca5952440b433fa122e40c0c69f0d5c62d9e98145021a74a2e1cf987f
```

Manifest:

```text
SKILL.md                         9538  4938e535c1fe8c2e38a4f57913386ec7707e493a6b3d44c18b721d6f525e5706
agents/openai.yaml               240  59c8599c09abce4eb63a5295fd692ab9e9f208ead60050ea1ecffb97961b613f
references/taste-profile.md     4107  94ca418c17076d94045bef6e4fe4fcdea6009f85f442753a79e06c6529311b3e
```

Only regular files were present. No symlink or special file entered the
candidate identity.

## Earlier attempts

| Attempt | Digest | Outcome |
|---|---|---|
| a1 | `350f293ea8b887bc493dd0a8688e3f240b10fa2e52471b659d6aa9d8fccefc06` | burned after a missing-video intake criterion failed |
| a2 | `3158495d436f8043a4a9c90b6075a52c21c68bd54b145f447f8001a534c0dce6` | burned after trace, action-register, audio-intake, and authority gaps surfaced |
| a3 | `9d86958a94ab23f7eedd0cf75f8f1281d513954647c392e956e7b60930c49445` | three holdouts passed, but the required final training regression reopened T1 and T2 |
| a4 | `b684444b850b6fb98a85ba45757e5fa11e32aaa9a9684dba5464237c385cb9c0` | burned after exact-schema and per-axis coordinate failures |
| a5 | `59f01ca89225c2c3804af86a4f9f764f452513f4f7d8ed57a7e017fa7bd101de` | burned after two prose matrix cells lacked their own source quote |
| a6 | `b5ade59ca5952440b433fa122e40c0c69f0d5c62d9e98145021a74a2e1cf987f` | graduated: H16-H18 each scored 5/5 with qualitative PASS |

The a6 digest matched before holdout materialization, after all three final
grades, and after the cold package smoke. No mid-holdout edit occurred.
