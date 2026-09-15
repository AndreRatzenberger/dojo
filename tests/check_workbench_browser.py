"""Run with Python 3.10+ and the optional agent-browser CLI on PATH."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills/dojo/scripts"))
import dojo_workbench as wb


def main():
    session = f"dojo-browser-check-{os.getpid()}"

    def browser(*args):
        return subprocess.check_output(["agent-browser", "--session", session, *args], text=True, timeout=30).strip()

    def value(expression):
        return json.loads(browser("eval", expression))

    def wait_for(expression):
        browser("eval", "(async()=>{for(let i=0;i<60;i++){if(" + expression + ")return true;await new Promise(r=>setTimeout(r,100));}throw Error('Condition did not arrive')})()")

    with tempfile.TemporaryDirectory(prefix="dojo-browser-") as temporary:
        base = Path(temporary)
        root = base / "session"
        wb.init_session(root, "release-notes", "Review a release", "Keep facts supported.", "fast")
        wb.add_case(root, "first", "Export fix", "Names now export correctly.", ["No invented date"])
        skill = base / "release-notes"
        skill.mkdir()
        (skill / "SKILL.md").write_text("Original instructions")
        wb.snapshot(root, "original", skill, "Keep the original")
        (skill / "SKILL.md").write_text("Only include a supplied date")
        wb.snapshot(root, "v1", skill, "Remove unsupported dates")
        server = wb.make_server(root)
        requests = []
        handler = server.RequestHandlerClass
        original_get = handler.do_GET

        def track_get(request):
            requests.append(request.path)
            original_get(request)

        handler.do_GET = track_get
        outputs = base / "outputs"
        outputs.mkdir()
        (outputs / "notes.md").write_text("# Release notes\nNames now export correctly.")
        (outputs / "preview.html").write_text(f'<h1>Release notes</h1><script>parent.document.body.dataset.escape="unsafe"</script><img src="http://127.0.0.1:{server.server_port}/probe">')
        checks = [{"criterion": "No invented date", "status": "passed", "evidence": "notes.md contains no date."}]
        for variant in ("baseline", "candidate"):
            wb.start_run(root, variant, "first", variant, "v1" if variant == "candidate" else "original")
            wb.finish_run(root, variant, "passed", "No invented date", outputs, checks)
        worker = threading.Thread(target=server.serve_forever, daemon=True)
        worker.start()
        try:
            browser("open", server.workbench_url)
            wait_for("document.querySelector('#review-run').value==='candidate'")
            browser("fill", "#comment", "Keep the short opening.")
            browser("select", "#decision", "needs-changes")
            browser("click", "#save")
            wait_for("document.querySelector('#feedback-status').textContent.startsWith('Saved at')")
            assert wb.records(root, "feedback")[0]["comment"] == "Keep the short opening."
            browser("reload")
            wait_for("document.querySelector('#comment').value==='Keep the short opening.'")
            browser("fill", "#comment", "Unfinished draft")
            browser("click", "#candidate .files button:nth-child(2)")
            wait_for("document.querySelector('#candidate iframe')!==null")
            wb.activity(root, "revise", "working", "Applying feedback", "Keep the concrete example")
            wait_for("document.querySelector('#activity-message').textContent==='Applying feedback'")
            assert value("document.querySelector('#comment').value") == "Unfinished draft"
            assert value("document.querySelector('#candidate .files [aria-pressed=true]').textContent") == "preview.html"
            assert value("document.body.dataset.escape||false") is False
            assert "/probe" not in requests
            browser("reload")
            wait_for("document.querySelector('#comment').value==='Unfinished draft'")
            browser("focus", "#comment")
            browser("press", "Tab")
            assert value("document.activeElement.id") == "save"
            browser("set", "offline", "on")
            wait_for("!document.querySelector('#error').hidden")
            assert value("document.querySelector('#comment').value") == "Unfinished draft"
            browser("set", "offline", "off")
            wait_for("document.querySelector('#error').hidden")
            wb.save_feedback(root, {"run_id": "candidate", "decision": "comment", "comment": "Another tab", "version": 1})
            wait_for("!document.querySelector('#reload-feedback').hidden")
            browser("click", "#save")
            wait_for("document.querySelector('#feedback-status').textContent.includes('another tab')")
            assert value("document.querySelector('#comment').value") == "Unfinished draft"
            assert wb.records(root, "feedback")[0]["version"] == 2
            browser("click", "#reload-feedback")
            assert value("document.querySelector('#comment').value") == "Another tab"
            browser("click", "[data-tab=changes]")
            wait_for("document.querySelector('#diff').textContent.includes('+Only include a supplied date')")
            for width in (1440, 390):
                browser("set", "viewport", str(width), "900")
                assert value("document.documentElement.scrollWidth<=innerWidth")
            browser("click", "[data-tab=outputs]")
            assert value("document.documentElement.scrollWidth<=innerWidth")
            assert not browser("errors")
            print("PASS: live updates, persisted feedback/drafts, conflicts, offline recovery, diffs, sandbox, keyboard, desktop/mobile")
        finally:
            browser("close")
            server.shutdown()
            worker.join()
            server.server_close()


if __name__ == "__main__":
    main()
