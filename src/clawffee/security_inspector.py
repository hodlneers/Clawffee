"""Core local-first security inspector implementation."""

from __future__ import annotations

import re
from pathlib import Path

from .models import CapabilityProfile, Evidence, Indicator, ScanReport, ScanSummary, Severity
from .openclaw_adapter import profile_from_indicators

_PATTERN_DEFS: list[tuple[str, Severity, str, str, re.Pattern[str], str]] = [
    (
        "shell.exec",
        Severity.HIGH,
        "Shell execution detected",
        "Pattern indicates command execution capability.",
        re.compile(r"\b(subprocess\.|os\.system\(|child_process\.|execSync\(|spawn\()"),
        "shell_execution",
    ),
    (
        "network.http",
        Severity.MEDIUM,
        "Network access detected",
        "Pattern indicates outbound network calls.",
        re.compile(r"\b(requests\.|urllib\.|fetch\(|axios\.|http\.client|https?://)"),
        "network_access",
    ),
    (
        "filesystem.write",
        Severity.MEDIUM,
        "Filesystem write capability detected",
        "Pattern indicates local file mutation behavior.",
        re.compile(r"\b(write_text\(|write_bytes\(|open\([^\n]*['\"]w|fs\.writeFile|shutil\.rmtree|rm -rf)"),
        "filesystem_write",
    ),
    (
        "secrets.env",
        Severity.HIGH,
        "Environment variable access detected",
        "Pattern indicates env access that may include secrets.",
        re.compile(r"\b(os\.environ|process\.env|getenv\()"),
        "env_access",
    ),
    (
        "dynamic.eval",
        Severity.HIGH,
        "Dynamic code execution detected",
        "Pattern indicates eval/exec style execution.",
        re.compile(r"\b(eval\(|exec\(|Function\()"),
        "dynamic_code",
    ),
]

_DEFAULT_SUFFIXES = {".py", ".js", ".ts", ".sh", ".json", ".yml", ".yaml", ".md"}


class SecurityInspector:
    """Scan source trees for evidence-backed risk indicators."""

    def inspect(self, target: str) -> ScanReport:
        base = Path(target)
        if not base.exists():
            raise FileNotFoundError(f"Target does not exist: {target}")

        files = self._list_files(base)
        capabilities = CapabilityProfile()
        indicators: list[Indicator] = []

        for file_path in files:
            try:
                text = file_path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                text = file_path.read_text(encoding="latin-1", errors="ignore")

            file_indicators = self._scan_text(file_path, base, text)
            for indicator in file_indicators:
                setattr(capabilities, self._capability_attr(indicator.id), True)
            indicators.extend(file_indicators)

        profile = profile_from_indicators([i.severity for i in indicators])
        summary = ScanSummary(
            files_scanned=len(files),
            indicators_found=len(indicators),
            overall_profile=profile,
        )

        return ScanReport(
            target=str(base.resolve()),
            summary=summary,
            capabilities=capabilities,
            indicators=indicators,
        )

    def _list_files(self, base: Path) -> list[Path]:
        if base.is_file():
            return [base]
        return [
            p
            for p in base.rglob("*")
            if p.is_file() and p.suffix.lower() in _DEFAULT_SUFFIXES and ".git" not in p.parts
        ]

    def _scan_text(self, file_path: Path, base: Path, text: str) -> list[Indicator]:
        indicators: list[Indicator] = []
        lines = text.splitlines()

        for idx, line in enumerate(lines, start=1):
            for indicator_id, severity, title, detail, pattern, _ in _PATTERN_DEFS:
                if not pattern.search(line):
                    continue
                indicators.append(
                    Indicator(
                        id=indicator_id,
                        severity=severity,
                        title=title,
                        detail=detail,
                        evidence=Evidence(
                            file=str(file_path.relative_to(base)) if base.is_dir() else str(file_path),
                            line=idx,
                            excerpt=line.strip()[:200],
                        ),
                    )
                )
        return indicators

    def _capability_attr(self, indicator_id: str) -> str:
        for pid, _, _, _, _, attr in _PATTERN_DEFS:
            if pid == indicator_id:
                return attr
        raise ValueError(f"Unknown indicator id: {indicator_id}")
