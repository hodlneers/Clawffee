# Clawffee MVP Specification (v1.0)

## 1. Goal

Ship a local-first security inspector that scans source trees for evidence-backed risk indicators and produces machine-readable plus human-readable reports.

## 2. In-Scope (v1.0)

### 2.1 Scanner Core

Implemented in `src/clawffee/security_inspector.py`:
- inspect a file or directory target
- apply rule patterns line-by-line
- emit indicators with evidence
- derive capability flags and overall severity profile

### 2.2 Supported File Types

v1 scanner processes files with these suffixes:
- `.py`
- `.js`
- `.ts`
- `.sh`
- `.json`
- `.yml`
- `.yaml`
- `.md`

### 2.3 Supported Pattern Families

Current pattern IDs and intent:
- `shell.exec` - command execution capability (HIGH)
- `network.http` - outbound network behavior (MEDIUM)
- `filesystem.write` - local file mutation patterns (MEDIUM)
- `secrets.env` - environment-variable access (HIGH)
- `dynamic.eval` - dynamic code execution patterns (HIGH)

### 2.4 Report Outputs

- JSON renderer: `src/clawffee/reporting.py::to_json`
- Markdown renderer: `src/clawffee/reporting.py::to_markdown`

Both include:
- target path
- summary
- capability profile
- indicator list with evidence
- disclaimer (informational-only)

## 3. Interfaces

### 3.1 CLI Interface

Entrypoint: `src/clawffee/cli.py`

Command:

```bash
clawffee <target> [--format json|md]
```

Defaults:
- output format: `json`

### 3.2 OpenClaw Plugin Interface

Files:
- `openclaw_plugin.yaml`
- `plugins/clawffee/security_inspector_operator.py`
- `src/clawffee/openclaw_adapter.py`

Operator behavior:
- `transform(payload, config)` reads target from payload field `text` by default (`target_field` config key)
- executes local scan
- returns normalized dict for framework transport

Capability envelope returned by adapter:
- stage: `analysis`
- operation: `skill-vetting`
- result_type: `security-inspection-report`

## 4. Data Contracts

### 4.1 Internal Models

`src/clawffee/models.py` provides:
- `Severity`
- `Evidence`
- `Indicator`
- `CapabilityProfile`
- `ScanSummary`
- `ScanReport`

### 4.2 JSON Shape (Top-Level)

```json
{
  "target": "...",
  "summary": {
    "files_scanned": 0,
    "indicators_found": 0,
    "overall_profile": "INFO|LOW|MEDIUM|HIGH"
  },
  "capabilities": {
    "shell_execution": false,
    "network_access": false,
    "filesystem_write": false,
    "env_access": false,
    "dynamic_code": false
  },
  "indicators": [
    {
      "id": "...",
      "severity": "...",
      "title": "...",
      "detail": "...",
      "confidence": "MEDIUM",
      "evidence": {
        "file": "...",
        "line": 1,
        "excerpt": "..."
      }
    }
  ],
  "disclaimer": "..."
}
```

## 5. Default Configuration

### 5.1 CLI defaults
- format: `json`

### 5.2 OpenClaw operator defaults
- `target_field`: `text`

### 5.3 Scanner defaults
- suffix allowlist from `_DEFAULT_SUFFIXES`
- active rules from `_PATTERN_DEFS`

## 6. Non-Goals (v1.0)

- AST/dataflow semantic analysis
- enforcement/sandbox mode
- guarantee/certification scoring
- dependency manifest analysis (planned)
- scan diff mode (planned)

## 7. Quality Gates

- Unit tests in `tests/`
- CI workflow in `.github/workflows/ci.yml` executes tests on push/PR

## 8. Planned Enhancements

Per `docs/project/IMPLEMENTATION_BACKLOG.md`:

1. Detection quality
- configurable rule packs and severities
- duplicate-indicator collapsing
- dependency manifest inspection (`package.json`, `requirements.txt`)
- diff mode between scans

2. OpenClaw integration hardening
- compatibility tests against OpenClaw fixture skills

3. v1.1 roadmap
- token-optimizer features (separate phase)

## 9. Acceptance Criteria (v1.0)

- scanner runs locally via CLI
- OpenClaw operator wrapper can invoke scanner and return structured result
- reports render in both JSON and markdown
- CI executes unit tests on push/PR
