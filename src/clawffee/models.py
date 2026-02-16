"""Data models for security inspection reports."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Severity(str, Enum):
    INFO = "INFO"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


@dataclass(frozen=True)
class Evidence:
    file: str
    line: int
    excerpt: str


@dataclass(frozen=True)
class Indicator:
    id: str
    severity: Severity
    title: str
    detail: str
    evidence: Evidence
    confidence: str = "MEDIUM"


@dataclass
class CapabilityProfile:
    shell_execution: bool = False
    network_access: bool = False
    filesystem_write: bool = False
    env_access: bool = False
    dynamic_code: bool = False


@dataclass
class ScanSummary:
    files_scanned: int
    indicators_found: int
    overall_profile: Severity


@dataclass
class ScanReport:
    target: str
    summary: ScanSummary
    capabilities: CapabilityProfile
    indicators: list[Indicator] = field(default_factory=list)
    disclaimer: str = (
        "Informational analysis only. Clawffee reports observed indicators and does not "
        "provide safety or security guarantees."
    )
