from clawffee.models import Severity
from clawffee.security_inspector import SecurityInspector


def test_inspector_detects_expected_indicators(tmp_path):
    target = tmp_path / "skill.py"
    target.write_text(
        """
import os
import subprocess
import requests

def run():
    token = os.environ.get('API_KEY')
    subprocess.run(['echo', 'ok'])
    requests.get('https://example.com')
""".strip()
    )

    report = SecurityInspector().inspect(str(tmp_path))

    ids = {indicator.id for indicator in report.indicators}
    assert "shell.exec" in ids
    assert "secrets.env" in ids
    assert "network.http" in ids
    assert report.capabilities.shell_execution is True
    assert report.capabilities.env_access is True
    assert report.capabilities.network_access is True
    assert report.summary.overall_profile == Severity.HIGH


def test_inspector_handles_missing_target():
    inspector = SecurityInspector()
    missing_path = "/path/that/does/not/exist"

    try:
        inspector.inspect(missing_path)
        assert False, "Expected FileNotFoundError"
    except FileNotFoundError:
        assert True
