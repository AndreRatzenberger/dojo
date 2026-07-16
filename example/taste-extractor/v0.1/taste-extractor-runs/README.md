# Raw run index

Every behavior run has its exact prompt, raw output, and criterion-level score.
Training baselines run without the candidate skill. Skilled and graduation
runs used fresh contexts instructed to read only the candidate and references
their task path naturally required. These historical v1 receipts predate
canary preflights and complete path/tool traces, so v0.2 classifies them as
`fresh-context only`, not retroactively audited instruction-bounded evidence.

Routing uses two fresh proxy judges because the host does not expose a callable
real dispatcher. Package receipts include validation and a clean-context smoke
invocation.
