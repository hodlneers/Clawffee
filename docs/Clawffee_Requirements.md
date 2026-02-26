# Clawffee Requirements Document

This document captures functional and non-functional requirements for the Clawffee security inspector MVP described in `/Users/hodlneer/Clawffee/docs/Clawffee_MVP_Spec.md`.

## Functional Requirements

### FR-1: Local Target Intake
The system SHALL accept a local file or directory path as scan input through the CLI and OpenClaw operator interface.

### FR-2: File Enumeration by Allowlist
The scanner SHALL enumerate only supported suffixes from its configured/default allowlist.

### FR-3: Pattern-Based Indicator Detection
The scanner SHALL evaluate source lines against the active pattern rules and emit indicators with evidence (`file`, `line`, `excerpt`) for matches.

### FR-4: Capability Profile Derivation
The system SHALL derive capability booleans from matched indicator IDs (shell, network, filesystem-write, env access, dynamic code).

### FR-5: Severity Profile Computation
The system SHALL compute an overall profile based on the highest observed severity in the scan result.

### FR-6: Dual Report Rendering
The system SHALL render scan results as both JSON and Markdown, including summary, capabilities, indicators, and disclaimer text.

### FR-7: CLI Contract
The CLI SHALL support:
1. required target argument
2. `--format` option with `json|md`
3. default output format of `json`

### FR-8: OpenClaw Operator Contract
The OpenClaw operator SHALL:
1. implement the expected operator methods (`name`, `version`, `profile`, `capabilities`, `default_config`, `transform`)
2. read target from payload field configured by `target_field` (default: `text`)
3. return adapter-normalized result dictionaries

### FR-9: Local-First Processing
The scanner SHALL execute locally and SHALL NOT require cloud upload or remote processing for baseline scanning.

### FR-10: Error Handling
The system SHALL return actionable errors for invalid target paths and unreadable files, while continuing scan work where safe.

### FR-11: Informational Positioning
Reports SHALL include explicit informational-only language and SHALL NOT label targets as "safe/unsafe certified."

## Non-Functional Requirements

### NFR-1: Determinism
Given the same target and rule set, the scanner SHOULD produce stable indicator output.

### NFR-2: Reliability
The scanner SHOULD complete repeated local scans without unhandled exceptions.

### NFR-3: Setup Time
A new contributor SHOULD be able to run the local scanner and tests in under 30 minutes using project docs.

### NFR-4: Extensibility
Rule packs, severities, and output formats SHOULD be extensible with minimal refactor.

### NFR-5: Testability
Core scanner, adapter, and renderer behaviors SHALL be covered by tests runnable in CI.

### NFR-6: Documentation Quality
README and docs SHALL include setup, execution, troubleshooting, and extension guidance.

### NFR-7: Performance
Suffix filtering and line-oriented scanning SHOULD keep scans practical for typical skill/source trees.

### NFR-8: Privacy and Data Handling
The baseline scanner SHOULD avoid transmitting source content externally and SHOULD minimize sensitive data exposure in logs.

## Acceptance Criteria
- CLI scan runs end-to-end for supported target paths.
- JSON and Markdown reports render with required sections.
- OpenClaw operator invocation returns structured report dictionaries.
- Existing CI test suite passes.
- Requirement language is consistent with `/Users/hodlneer/Clawffee/docs/Clawffee_PDR.md` and `/Users/hodlneer/Clawffee/docs/Clawffee_MVP_Spec.md`.
