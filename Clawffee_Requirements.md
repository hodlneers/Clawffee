# Clawffee Requirements Document

This document captures the functional and non‑functional requirements for the Clawffee summarisation operator. It should be consulted when implementing the plugin and reviewed whenever the scope changes.

## Functional Requirements

### FR‑1: Transcript Ingestion

The operator SHALL accept a single plain‑text input containing the full content of a meeting, document or log. The input will be provided via the `payload['text']` field of the request.

### FR‑2: Baseline Summarisation

Upon invocation of the baseline operator (`BaselineSummaryOperator`), the operator SHALL produce a concise summary covering the key points, decisions, and action items discussed in the input. The summary SHALL be returned under the `summary` key of the result dictionary.

### FR‑3: Tree‑of‑Thought Summarisation

Upon invocation of the ToT operator (`TreeOfThoughtSummaryOperator`), the operator SHALL:

1. Segment the input into sections of configurable length (`config['section_size']`), or by topic if a segmentation algorithm is available.

2. For each section, iterate over a list of reflection questions (default specified in `default_config` or overridden by `config['reflection_questions']`).

3. Prompt the underlying LLM with each question and collect the answers.

4. Compose a narrative summary that integrates all collected answers and return it under the `summary` key.

5. Return a list of branches under the `branches` key, where each branch contains the question, answer and optional notes.

### FR‑4: Configuration Overrides

The operator SHALL merge user‑supplied configuration values with its default configuration. Any configuration key present in the `config` argument SHALL override the corresponding default. Unrecognised keys MAY be ignored but SHOULD NOT cause an error.

### FR‑5: Error Handling

If the input transcript is empty or missing, the operator SHALL raise a descriptive exception or return an error dictionary indicating invalid input. If the LLM client fails, the operator SHALL propagate the error message to the caller.

### FR‑6: Plugin Registration

The plugin SHALL provide an `openclaw_plugin.yaml` file identifying the plugin and its operators as required by the OpenClaw framework. The plugin SHALL register its operators in `plugins/clawffee/__init__.py`.

## Non‑Functional Requirements

### NFR‑1: Conformance

The operator SHALL conform to the interface defined by `OpenClawOperatorBase`. It SHALL implement all required methods (`name`, `version`, `profile`, `capabilities`, `default_config`, `transform`) and adhere to the expected data structures for input and output.

### NFR‑2: Accuracy

Summaries SHOULD accurately reflect the content of the input. The operator SHOULD minimise hallucination and avoid introducing information that does not appear in the original transcript. Reflection questions SHOULD be phrased to elicit factual responses.

### NFR‑3: Performance

The operator SHOULD process transcripts of up to 100k characters within a reasonable time frame (on the order of seconds to a few minutes, depending on LLM latency). Internal segmentation and prompting SHOULD be efficient and avoid unnecessary API calls.

### NFR‑4: Configurability

All tunable parameters (model name, maximum tokens, section size, reflection questions) SHALL be surfaced via the operator's config argument. Defaults SHALL be provided via `default_config` and documented in the operator profile.

### NFR‑5: Extensibility

The code base SHOULD be organised to allow new operators to be added without modifying existing ones. Shared utilities (e.g. text segmentation, prompt construction) SHOULD be factored into helper modules to avoid duplication.

### NFR‑6: Documentation

All public classes and functions SHALL be documented with docstrings. The `docs/` directory SHALL contain up‑to‑date specifications, requirements, and design rationale. Documentation SHALL be updated concurrently with code changes.

### NFR‑7: Testing

The plugin SHALL include unit tests that exercise both the baseline and ToT operators. Tests SHOULD mock LLM responses to achieve deterministic results. Continuous integration SHOULD run these tests on every commit.

### NFR‑8: Security & Privacy

The operator SHOULD treat transcripts as sensitive data. It SHOULD avoid logging raw transcript content or storing prompts and responses longer than necessary for processing. If additional vetting or token accounting features are added in future releases, they MUST respect security best practices and avoid leaking credentials or personal data.

---

By adhering to these requirements, the Clawffee plugin will provide reliable summarisation while remaining flexible for future enhancements.
