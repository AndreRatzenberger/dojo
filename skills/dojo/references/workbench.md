# Local Workbench

The coding agent performs authoring, dispatch, and grading. A small Python
helper records progress and serves a browser for comparisons and feedback.
It does not run models, infer success from output existence, or measure token
usage. Python 3.10+ and a local browser are sufficient; no web dependencies,
account, API key, or frontend build are needed.

Open it for interactive native authoring and substantive revisions. A
`--no-workbench` or `--quiet` invocation stays in chat/files. For a remote host
without a reachable loopback browser, keep the same files and report the
limitation; do not bind to a public interface or invent a reachable URL.

## Coordinator Commands

Resolve `DOJO_HELPER` from the installed skill directory. `DOJO_SESSION` is a
new directory under the collision-checked `~/.dojo/<repo-slug>/<skill>/`
identity from `SKILL.md`. Use one coordinator and one server per session.
Run each command below when its corresponding work actually occurs, not as a
script that manufactures a complete-looking session.

```bash
DOJO_HELPER=<installed-dojo>/scripts/dojo_workbench.py
DOJO_SESSION=~/.dojo/<repo-slug>/<skill>/workbench-<session-id>

python3 "$DOJO_HELPER" init "$DOJO_SESSION" --name release-notes \
  --title "Release notes" --intent-file <request.txt> --lane fast
python3 "$DOJO_HELPER" serve "$DOJO_SESSION" --open
```

`serve` stays running. Use the host's managed background process for it and
retain the process handle. Share the printed `http://127.0.0.1:<port>/#<token>`
link privately with the user; the token grants local session access. Stop that
process when review is finished, or leave it running if the user is still
reviewing. Reopening a saved session creates a new link; files persist.

Define a case from an exact prompt and a JSON array of unique check strings:

```json
["Names the user-visible change", "Does not invent a release date"]
```

```bash
python3 "$DOJO_HELPER" case "$DOJO_SESSION" --id first --title "A small release" \
  --prompt-file <task.txt> --criteria-file <criteria.json>
python3 "$DOJO_HELPER" activity "$DOJO_SESSION" --phase baseline \
  --message "Running the original task" --reason "Find what the agent already gets right."
python3 "$DOJO_HELPER" start "$DOJO_SESSION" --id baseline-1 --case first --variant baseline
```

Now execute the task using the lane's fresh runner. The runner writes only to
its own allowed output directory. After it stops, the coordinator grades it
and finishes the run. For an edit baseline, snapshot the original first and
pass `--revision original` to `start`.

```json
[
  {"criterion": "Names the user-visible change", "status": "passed", "evidence": "notes.md names the corrected export behavior."},
  {"criterion": "Does not invent a release date", "status": "failed", "evidence": "notes.md supplies a date absent from the input."}
]
```

```bash
python3 "$DOJO_HELPER" finish "$DOJO_SESSION" --id baseline-1 --status failed \
  --summary "Introduces an unsupported date." --outputs <runner-output-directory> \
  --checks <graded-checks.json>
python3 "$DOJO_HELPER" snapshot "$DOJO_SESSION" --id v1 \
  --skill <candidate-directory> --reason "Require source support for release facts."
python3 "$DOJO_HELPER" start "$DOJO_SESSION" --id candidate-1 --case first \
  --variant candidate --revision v1
```

Run and finish the candidate in the same way, then record a `review` activity.
Read the user's saved feedback without scraping the page:

```bash
python3 "$DOJO_HELPER" feedback "$DOJO_SESSION"
python3 "$DOJO_HELPER" activity "$DOJO_SESSION" --phase revise \
  --message "Applying the review" --reason "Explain the specific requested change."
```

After an actual edit, snapshot `v2`, start a new run, and compare it. Completed
runs, cases, and snapshot IDs cannot be overwritten through the CLI. Feedback
is versioned per run; stale browser writes return a conflict and retain the
draft. `state` reads the entire session as JSON. The agent can read the same
records the UI shows and can consume every review action programmatically.

## Record Semantics

Activities use phases `scope`, `baseline`, `author`, `evaluate`, `review`,
`revise`, `done`; status is `working`, `waiting`, `blocked`, or `complete`.
An activity's completion says the step ended, not that the candidate passed.

Runs start as `running` and end as `passed`, `failed`, `invalid`, or `unproven`.
A `passed` run needs evidence for every predeclared check. Contamination is
`invalid`; missing required evidence or human judgment is `unproven`. These
are run states, not Audit Lane graduation. `--tokens` and `--duration` accept
measured values only; omit them when unavailable. The browser shows “not
recorded,” never zero or an estimated saving.

Snapshots copy regular files and record their sizes and SHA-256 hashes. The
server verifies those hashes before serving an artifact or diff. Browser text
previews/diffs are limited to 256 KiB and downloads to 20 MiB; larger artifacts
remain on disk. HTML previews disable scripts and network access. Other binary
formats can be downloaded. Feedback and selections survive live updates;
unsaved feedback drafts survive reload in the same browser tab.

The server binds only to `127.0.0.1`, requires its session token for APIs,
rejects foreign origins, and only serves manifest-listed, non-symlink session
artifacts. Keep private inputs in private sessions. This is a local review
tool, not a multi-user or remotely exposed service.

Workbench files are coordinator-visible development evidence. They do not
replace the Audit Lane candidate digest, isolation audit, qualitative gate,
or custody protocol. Never place unopened holdouts or evaluator-only criteria
in this browser or give a runner access to the session tree. Keep the final
lane receipt alongside the session and link to its relevant runs.
