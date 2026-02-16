# Clawffee Repository Structure & Interfaces

This document describes how the Clawffee codebase is organized when operating as an OpenClaw plugin. OpenClaw expects plugins to follow a clear, modular structure: each plugin declares metadata, exposes operators in a discoverable way, includes tests, and provides sufficient documentation.

## Top-Level Layout

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

## Key Components

### openclaw_plugin.yaml

This YAML file is the plugin entry point and should define:
- `id`
- `description`
- `authors`
- `version`
- `operators`
- `capabilities`
- `supported_request_types`

Example:

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

### plugins/clawffee/__init__.py

Responsible for operator registration and exports.

```python
from .baseline import BaselineSummaryOperator
from .tot import TreeOfThoughtSummaryOperator

__all__ = [
    BaselineSummaryOperator,
    TreeOfThoughtSummaryOperator,
]
```

### plugins/clawffee/baseline.py

Implements `BaselineSummaryOperator` and required methods:
- `name`
- `version`
- `profile`
- `capabilities`
- `default_config`
- `transform`

### plugins/clawffee/tot.py

Implements `TreeOfThoughtSummaryOperator` with sectioning/reflection steps and output branches.

### tests/

Unit and integration tests mirror operator modules and validate output contracts.

### docs/

Contains specifications, requirements, and design rationale.

### scripts/

Utility scripts for local development and evaluation.

## Interfaces

### Operator Interface

```python
def transform(self, payload: Dict[str, Any], config: Dict[str, Any]) -> Dict[str, Any]:
    """Transform the input payload into a summarisation result.

    Args:
        payload: Input data with at least a `text` field.
        config: User-supplied configuration overriding defaults.

    Returns:
        Dictionary containing `summary`; ToT may also return `branches`.
    """
    raise NotImplementedError
```

### Configuration Interface

Merge runtime config over defaults:

```python
cfg = {**self.default_config(), **config}
```

Common keys:
- `model`
- `max_tokens`
- `section_size`
- `reflection_questions`

### Testing Interface

Tests call `transform` with mocked LLM responses and assert deterministic shape/content constraints.

## Contributing

When adding features/operators:
- Update docs with code changes.
- Increment semantic versioning in `openclaw_plugin.yaml` when needed.
- Add corresponding tests under `tests/`.
