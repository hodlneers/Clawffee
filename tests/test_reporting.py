from clawffee.reporting import to_json, to_markdown
from clawffee.security_inspector import SecurityInspector


def test_report_renderers_emit_expected_sections(tmp_path):
    file_path = tmp_path / "sample.py"
    file_path.write_text("eval('x')\n")

    report = SecurityInspector().inspect(str(tmp_path))

    as_json = to_json(report)
    as_md = to_markdown(report)

    assert '"target"' in as_json
    assert "dynamic.eval" in as_json
    assert "# Clawffee Inspection Report" in as_md
    assert "## Indicators" in as_md
