"""Report rendering utilities."""

from __future__ import annotations

import json

from .models import ScanReport


def to_json(report: ScanReport) -> str:
    payload = {
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
    return json.dumps(payload, indent=2)


def to_markdown(report: ScanReport) -> str:
    lines = [
        f"# Clawffee Inspection Report",
        "",
        f"- Target: `{report.target}`",
        f"- Files scanned: `{report.summary.files_scanned}`",
        f"- Indicators: `{report.summary.indicators_found}`",
        f"- Overall profile: `{report.summary.overall_profile.value}`",
        "",
        "## Capabilities",
        f"- shell_execution: `{report.capabilities.shell_execution}`",
        f"- network_access: `{report.capabilities.network_access}`",
        f"- filesystem_write: `{report.capabilities.filesystem_write}`",
        f"- env_access: `{report.capabilities.env_access}`",
        f"- dynamic_code: `{report.capabilities.dynamic_code}`",
        "",
        "## Indicators",
    ]

    if not report.indicators:
        lines.append("- No indicators detected.")
    else:
        for i in report.indicators:
            lines.extend(
                [
                    f"- `{i.id}` ({i.severity.value}): {i.title}",
                    f"  - file: `{i.evidence.file}:{i.evidence.line}`",
                    f"  - excerpt: `{i.evidence.excerpt}`",
                ]
            )

    lines.extend(["", "## Disclaimer", report.disclaimer, ""])
    return "\n".join(lines)
