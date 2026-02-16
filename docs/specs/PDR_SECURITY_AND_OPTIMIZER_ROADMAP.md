# PDR: Clawffee v1 to v1.1

## Scope
- v1: Security Inspector + Skill Vetting
- v1.1: Token Optimizer

## Architecture (High Level)
1. Scanner core ingests local skill source.
2. Detector modules emit evidence-backed indicators.
3. Aggregator builds capability map and summary profile.
4. Reporter emits JSON/Markdown outputs.
5. Diff engine compares scans across refs/runs.

## Key Risks
1. False sense of safety from report wording.
2. False positives reducing trust.
3. Performance degradation on large repos.
4. Drift from real OpenClaw conventions.

## Mitigations
1. Strict informational language and explicit disclaimer.
2. Evidence-first reporting and confidence levels.
3. Configurable depth and scan timeouts.
4. Periodic compatibility checks against OpenClaw upstream.

## Delivery Phases
1. Baseline detector set + JSON report.
2. Markdown report + diff mode.
3. Usability pass and docs hardening.
4. Token optimizer add-on.
