"""OpenClaw-facing adapter helpers.

This module keeps integration boundaries explicit and lets the scanner remain
framework-agnostic while still exposing OpenClaw-friendly metadata.
"""

from __future__ import annotations

from dataclasses import dataclass

from .models import ScanReport, Severity


@dataclass(frozen=True)
class OpenClawCapabilityEnvelope:
    stage: list[str]
    operation: str
    result_type: str


def capability_envelope() -> OpenClawCapabilityEnvelope:
    """Return default capability metadata for OpenClaw pipeline registration."""
    return OpenClawCapabilityEnvelope(
        stage=["analysis"],
        operation="skill-vetting",
        result_type="security-inspection-report",
    )


def to_openclaw_result(report: ScanReport) -> dict:
    """Serialize a ScanReport into a plain dict suitable for framework transport."""
    return {
        "target": report.target,
        "summary": {
            "files_scanned": report.summary.files_scanned,
            "indicators_found": report.summary.indicators_found,
            "overall_profile": report.summary.overall_profile.value,
        },
        "capabilities": {
            "shell_execution": report.capabilities.shell_execution,
            "network_access": report.capabilities.network_access,
            "filesystem_write": report.capabilities.filesystem_write,
            "env_access": report.capabilities.env_access,
            "dynamic_code": report.capabilities.dynamic_code,
        },
        "indicators": [
            {
                "id": i.id,
                "severity": i.severity.value,
                "title": i.title,
                "detail": i.detail,
                "confidence": i.confidence,
                "evidence": {
                    "file": i.evidence.file,
                    "line": i.evidence.line,
                    "excerpt": i.evidence.excerpt,
                },
            }
            for i in report.indicators
        ],
        "disclaimer": report.disclaimer,
    }


def profile_from_indicators(severities: list[Severity]) -> Severity:
    """Compute a summary profile using highest observed severity."""
    if not severities:
        return Severity.INFO
    if Severity.HIGH in severities:
        return Severity.HIGH
    if Severity.MEDIUM in severities:
        return Severity.MEDIUM
    if Severity.LOW in severities:
        return Severity.LOW
    return Severity.INFO
