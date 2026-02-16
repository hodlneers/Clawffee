# Requirements: Token Optimizer (v1.1)

## Functional
1. Track token usage per run/session.
2. Estimate model cost from token usage.
3. Identify waste patterns:
- repeated rephrasing
- runaway verbosity
- low-value continuation
4. Generate optimization suggestions:
- summarize context
- restate intent
- add stop conditions
5. Output before/after efficiency comparison where baseline exists.

## Non-Functional
1. Recommendations are advisory, not mandatory.
2. Must not expose secrets in reports.
3. Keep signal-to-noise high; avoid generic tips.
4. Minimize added latency to normal workflows.

## Sequencing Constraint
This is v1.1 and depends on adoption and trust established by v1 inspector.
