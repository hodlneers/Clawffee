from plugins.clawffee.security_inspector_operator import SecurityInspectorOperator


def test_operator_capabilities_shape():
    op = SecurityInspectorOperator()
    caps = op.capabilities()

    assert caps["stage"] == ["analysis"]
    assert caps["operation"] == "skill-vetting"


def test_operator_transform(tmp_path):
    sample = tmp_path / "skill.py"
    sample.write_text("import os\nos.environ.get('X')\n")

    op = SecurityInspectorOperator()
    result = op.transform({"text": str(tmp_path)})

    assert "summary" in result
    assert "indicators" in result
    assert result["capabilities"]["env_access"] is True
