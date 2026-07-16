# Invalid-run ledger

Invalid runs contribute no score.

| Run | Defect | Disposition |
|---|---|---|
| First training capture set | The runner wrote `output.md`, and the harness also used that filename for the CLI final-response capture. Several complete artifacts were overwritten by short completion pointers. | Entire capture set invalidated before grading. All six baseline and skilled runs were repeated in clean capsules using final-response-only capture to `result.md`. |
| First grader attempt | Began reading the invalid overwritten captures. | Interrupted before any score was accepted. |
| Attempt a2 H5 criterion 5 | The criterion demanded an explicit append-only acceptance test although the task never exposed append-only behavior as a requirement. | Marked invalid as a hidden criterion. The candidate was not taught to guess it; the final custodian had to trace every criterion to an exact task phrase. |

The invalid evidence remains listed because hiding harness mistakes would make
the successful receipts less trustworthy, not more.
