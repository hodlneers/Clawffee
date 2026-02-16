# Requirements: Security Inspector And Skill Vetting (v1)

## Functional
1. Accept local skill directory or local clone path as scan target.
2. Detect capability indicators for:
- shell execution
- network egress
- filesystem read/write/delete
- environment variable access
- dynamic code execution patterns
3. Produce machine-readable JSON report.
4. Produce human-readable Markdown report.
5. Include evidence (file and line where possible) for each indicator.
6. Support diffing two scans or refs to highlight newly introduced risk indicators.
7. Run fully local by default.

## Non-Functional
1. No telemetry by default.
2. Deterministic output for same input and config.
3. No guarantee/certification language in outputs.
4. Clear failure behavior for invalid paths and parse errors.
5. Report generation target: under 2 minutes for typical skill-sized repos.

## Output Contract (Minimum)
- target metadata
- summary profile
- capability map
- indicator list with severities
- disclaimer

## Explicit Exclusions
- No automatic blocking/enforcement in v1.
- No cloud dependency for core scan.
- No malware-certification claim.
