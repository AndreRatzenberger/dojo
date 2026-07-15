# Raw run index

Every behavior run has its exact prompt, raw output, and criterion-level score.
Training baselines run without the candidate skill. Skilled and graduation
runs use fresh isolated contexts with only the candidate and the references
their task path naturally requires.

Routing uses two fresh proxy judges because the host does not expose a callable
real dispatcher. Package receipts include validation and a clean-context smoke
invocation.
