# Clawffee Preliminary Design Report (PDR)

## 1. Purpose

This PDR documents the v1 architecture for Clawffee's local-first security inspector and skill-vetting workflow. It reflects the current implementation under `src/clawffee` and the OpenClaw-facing adapter under `plugins/clawffee`.

Primary objective:
- provide fast, evidence-backed risk visibility for skill/source trees before runtime enablement.

Non-objective:
- certify code as safe or guarantee security outcomes.

## 2. System Architecture

Clawffee v1 is organized into five layers:

1. Detection layer
- `src/clawffee/security_inspector.py`
- walks files, applies regex-based rules, generates indicators and capability flags.

2. Data model layer
- `src/clawffee/models.py`
- defines `Severity`, `Evidence`, `Indicator`, `CapabilityProfile`, `ScanSummary`, and `ScanReport`.

3. Integration/translation layer
- `src/clawffee/openclaw_adapter.py`
- serializes reports to framework-safe dicts and provides OpenClaw capability envelope metadata.

4. Reporting/output layer
- `src/clawffee/reporting.py`
- renders reports as JSON or markdown.

5. Interface layer
- CLI: `src/clawffee/cli.py`
- OpenClaw operator wrapper: `plugins/clawffee/security_inspector_operator.py`

## 3. Detection Design

### 3.1 Scan Workflow

`SecurityInspector.inspect(target)` performs:

1. Validate target path exists.
2. Enumerate files by suffix.
3. Read each file as UTF-8 with latin-1 fallback.
4. Evaluate each line against pattern definitions.
5. Emit one `Indicator` per pattern match, with evidence:
- relative file path
- line number
- excerpt
6. Set capability booleans based on matched indicator IDs.
7. Compute overall profile using highest observed severity.
8. Return `ScanReport` with disclaimer.

### 3.2 Current Rule Set

Current indicator IDs in `_PATTERN_DEFS`:
- `shell.exec` (HIGH)
- `network.http` (MEDIUM)
- `filesystem.write` (MEDIUM)
- `secrets.env` (HIGH)
- `dynamic.eval` (HIGH)

Each rule contains:
- indicator ID
- severity
- title/detail text
- compiled regex
- capability attribute mapping

### 3.3 File Coverage

Current suffix allowlist (`_DEFAULT_SUFFIXES`):
- `.py`, `.js`, `.ts`, `.sh`, `.json`, `.yml`, `.yaml`, `.md`

## 4. OpenClaw Integration

### 4.1 Plugin Metadata

`openclaw_plugin.yaml` declares:
- plugin identity/version
- operator class: `plugins.clawffee.security_inspector_operator.SecurityInspectorOperator`
- capability envelope:
  - stage: `analysis`
  - operation: `skill-vetting`

### 4.2 Operator Contract

`SecurityInspectorOperator` provides conventional framework methods:
- `name()`
- `version()`
- `profile()`
- `capabilities()`
- `default_config()`
- `transform(payload, config)`

`transform` behavior:
- reads target path from payload field configured by `target_field` (default `text`)
- runs `SecurityInspector.inspect`
- returns normalized dict via `to_openclaw_result`

## 5. Reporting Model

### 5.1 JSON

`to_json(report)` emits:
- target
- summary (`files_scanned`, `indicators_found`, `overall_profile`)
- capabilities
- indicators (with evidence)
- disclaimer

### 5.2 Markdown

`to_markdown(report)` emits:
- summary header
- capabilities section
- indicator list
- disclaimer

## 6. Assumptions

- Source is available locally at scan time.
- Regex-based heuristics are acceptable for v1 speed/simplicity.
- False positives/false negatives are expected and manageable with evidence-first output.
- OpenClaw integration uses adapter dictionaries rather than direct framework internals.

## 7. Risks and Mitigations

1. Rule accuracy risk
- Risk: noisy or missed detections.
- Mitigation: evidence included per finding; roadmap includes configurable rule packs and deduping.

2. Scope drift risk
- Risk: docs promise deeper analysis than code implements.
- Mitigation: this PDR is implementation-grounded; MVP spec explicitly marks planned enhancements.

3. Integration mismatch risk
- Risk: OpenClaw runtime contract differences.
- Mitigation: keep operator wrapper thin and isolated; add compatibility fixture tests (backlog milestone).

4. Performance risk
- Risk: large trees increase scan time.
- Mitigation: suffix filtering and line-based scanning; future optimization via rule partitioning and cached scans.

## 8. Limitations (v1)

- Static regex matching only (no AST/dataflow analysis).
- No diff mode yet.
- No dependency manifest risk scoring yet.
- No runtime sandbox enforcement.
- No in-tool policy engine.

## 9. Validation Strategy

- Unit tests cover scanner, rendering, adapter serialization, and operator path.
- CI workflow (`.github/workflows/ci.yml`) runs tests on push and pull request.

## 10. Forward Path

Planned work from `docs/project/IMPLEMENTATION_BACKLOG.md`:
- detection-quality improvements (rule packs, dedupe)
- diff mode
- dependency manifest scanning
- deeper OpenClaw compatibility testing
- token optimizer phase (v1.1)
