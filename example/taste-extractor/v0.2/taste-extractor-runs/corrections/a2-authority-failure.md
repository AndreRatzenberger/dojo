1. **FAIL** — Not every action has all six coordinates. For example: “Potential medical emergencies bypass administrative escalation and go immediately to the clinical liaison or emergency response procedure.” This action lacks an explicit system surface, input state, output state, responsible-role attribution for execution, and required record.

2. **PASS** — The service safeguards are translated into technical controls. Evidence: “A routine queue-selection function must sort by arrival time”; “Triage conversations occur on an access-controlled surface”; “The system must enforce these permissions”; and “Reject an implementation if it merely reproduces the source service’s visible rituals or language.”

3. **PASS** — All seven states are explicitly listed under “Triage states.” Role ownership is defined in “Roles and exclusive authority,” including initial coordinator, triage worker, clinical liaison, bed coordinator, verifier, and supervisor. Permitted transitions are explicit, for example: “`needs_clinical_review` → `eligible_for_bed`, `waitlisted`, or `declined_with_referral`, after clinical clearance.”

4. **PASS** — The required incident timeline and recovery are covered explicitly: “At 23:15, the shared bed board is unavailable”; “23:40, report that a supposedly free bed is occupied”; “00:05, unrecorded cleaning hold identified”; and “00:20, network returns.” Recovery includes timestamp-ordered replay, independent verification, quarantine, final reconciliation, and authority transfer.

5. **PASS** — The invariants are both stated and tested in acceptance checks. Exact examples include: “No bed is assigned while a case is in `needs_clinical_review`”; “A bed cannot simultaneously be free, held, occupied, reserved, or assigned”; “A reserved accessible bed is not assigned…”; “Every state change and assignment is attributable and append-only”; “When occupancy integrity is uncertain, assignments stop”; and “Offline continuity records remain authoritative until recovery reconciliation is completed and signed.”

**Total: 4/5**

**Qualitative gate: PASS** — Despite the coordinate-completeness defect, the runbook is operationally structured, conservative during uncertainty, independently verified, privacy-preserving, and sufficiently usable by an experienced incident lead under pressure.

**Boundary audit:** Read only:

- `<local-run-root>/holdouts-a2/grading/h5/allowed/task.md`
- `<local-run-root>/holdouts-a2/grading/h5/allowed/criteria.md`
- `<local-run-root>/holdouts-a2/grading/h5/allowed/output.md`

Nothing outside the current directory was accessed. No files were written.