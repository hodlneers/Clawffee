from clawffee.models import Severity
from clawffee.openclaw_adapter import capability_envelope, to_openclaw_result
from clawffee.security_inspector import SecurityInspector


def test_openclaw_envelope_shape():
    envelope = capability_envelope()
    assert envelope.stage == ["analysis"]
    assert envelope.operation == "skill-vetting"
    assert envelope.result_type == "security-inspection-report"


def test_openclaw_result_serialization(tmp_path):
    file_path = tmp_path / "sample.py"
    file_path.write_text("import os\nos.environ.get('X')\n")

    report = SecurityInspector().inspect(str(tmp_path))
    result = to_openclaw_result(report)

    assert result["summary"]["overall_profile"] in {
        Severity.INFO.value,
        Severity.LOW.value,
        Severity.MEDIUM.value,
        Severity.HIGH.value,
    }
    assert "capabilities" in result
    assert "indicators" in result
