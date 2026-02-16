"""OpenClaw operator wrapper for Clawffee security inspection."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from clawffee.openclaw_adapter import capability_envelope, to_openclaw_result
from clawffee.security_inspector import SecurityInspector


class SecurityInspectorOperator:
    """Framework-facing operator adapter.

    This class mirrors common OpenClaw operator method names so the integration
    boundary is explicit even before full runtime wiring.
    """

    def name(self) -> str:
        return "security-inspector"

    def version(self) -> str:
        return "0.1.0"

    def profile(self) -> dict[str, Any]:
        return {
            "description": "Inspects local skill code for evidence-backed risk indicators.",
            "disclaimer": "Informational analysis only; no safety guarantees.",
        }

    def capabilities(self) -> dict[str, Any]:
        envelope = capability_envelope()
        return {
            "stage": envelope.stage,
            "operation": envelope.operation,
            "result_type": envelope.result_type,
        }

    def default_config(self) -> dict[str, Any]:
        return {
            "target_field": "text",
        }

    def transform(self, payload: dict[str, Any], config: dict[str, Any] | None = None) -> dict[str, Any]:
        cfg = {**self.default_config(), **(config or {})}
        target_value = payload.get(cfg["target_field"])

        if not target_value:
            raise ValueError("Expected payload field with target path text")

        target = Path(str(target_value)).expanduser()
        report = SecurityInspector().inspect(str(target))
        return to_openclaw_result(report)
