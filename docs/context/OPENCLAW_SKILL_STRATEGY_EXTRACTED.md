# OpenClaw Skill Strategy (Extracted From PDF)

Source file: `OpenClaw Skill Strategy.pdf` (removed after extraction)
Extraction date: 2026-02-16

## Notes
- This is a text extraction and normalization of the PDF content.
- The PDF content reflects an earlier Clawffee direction focused on an OpenClaw summarization plugin.
- This file is preserved for historical context and compatibility references.

## Extracted Content

### Clawffee Repository Structure & Interfaces

This document describes how the Clawffee codebase is organized when operating as an OpenClaw plugin. OpenClaw expects plugins to follow a clear, modular structure: each plugin declares metadata, exposes operators in a discoverable way, includes tests, and provides documentation.

### Top-Level Layout

```text
Clawffee/
├── openclaw_plugin.yaml
├── README.md
├── LICENSE
├── plugins/
│   └── clawffee/
│       ├── __init__.py
│       ├── baseline.py
│       └── tot.py
├── tests/
├── docs/
│   ├── Clawffee_MVP_Spec.md
│   ├── Clawffee_Requirements.md
│   └── Clawffee_PDR.md
└── scripts/
```

### Plugin Metadata Expectations

`openclaw_plugin.yaml` should include:
- `id`
- `description`
- `authors`
- `version`
- `operators` (module + class)
- `capabilities`
- `supported_request_types`

Example shape:

```yaml
id: clawffee
description: Summarisation operators for meeting transcripts with baseline and Tree-of-Thought modes.
authors:
  - name: Stephan (hodlneer)
version: 0.1.0
operators:
  - module: plugins.clawffee.baseline
    class: BaselineSummaryOperator
  - module: plugins.clawffee.tot
    class: TreeOfThoughtSummaryOperator
capabilities:
  stage:
    - analysis
  operation: summarisation
supported_request_types:
  - text/plain
```

### Operator Interface Expectations

Operators subclass `OpenClawOperatorBase` and implement:
- `name()`
- `version()`
- `profile()`
- `capabilities()`
- `default_config()`
- `transform(payload, config)`

`transform` returns a dictionary and typically includes at least `summary`, with optional `branches` for Tree-of-Thought style outputs.

### Configuration Pattern

Merge runtime config over defaults:

```python
cfg = {**self.default_config(), **config}
```

Common keys referenced in the PDF:
- `model`
- `max_tokens`
- `section_size`
- `reflection_questions`

### Testing Expectations

- Unit tests should mirror operator modules.
- LLM calls should be mocked for deterministic testing.
- Validate output dictionary shape (for example `summary`, and `branches` for ToT variants).

### Maintenance Guidance

- Keep docs in sync with code.
- Increment plugin version for new features or breaking changes.
- Add tests for each new operator.

## Context Status

The current canonical Clawffee strategy in this repository is:
- v1: Security Inspector + Skill Vetting
- v1.1: Token Optimizer

This extracted document is retained as historical strategy context and OpenClaw plugin-structure reference.
