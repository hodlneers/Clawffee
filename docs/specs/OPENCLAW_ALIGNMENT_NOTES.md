# OpenClaw Alignment Notes

This file records integration assumptions and alignment goals so Clawffee docs stay compatible with expected OpenClaw workflows.

## Alignment Principles
- Clawffee outputs are informational and advisory.
- Default operation is local-first.
- Skill analysis emphasizes transparent capability mapping.
- Reports should be understandable in under two minutes.

## Expected Inputs For Skill Vetting
- Local skill path, or a repo snapshot cloned locally.
- Skill metadata files and executable code paths.
- Dependency manifests and install scripts.

## Report Expectations
- Capability summary: filesystem, shell, network, env/secrets, dynamic code.
- Risk indicators with evidence locations.
- Change diff between scans/refs.
- Clear disclaimer that output is not a guarantee.

## Language Constraints
Avoid:
- "safe"
- "certified"
- "guaranteed"

Use:
- "observed"
- "detected"
- "indicator"
- "evidence"

## Follow-Up Needed
When implementation starts, validate exact OpenClaw skill metadata shape against the latest upstream source and update this file if field names or loading precedence differ.
