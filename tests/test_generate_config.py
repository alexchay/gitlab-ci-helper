# pylint: disable=missing-function-docstring

import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest
import yaml
from gitlab_ci.generate_config import generate_config_from_template


@pytest.fixture
def template_file():
    return Path(__file__).parent / "templates" / "config_template.j2"


@pytest.fixture
def data_file():
    return Path(__file__).parent / "data" / "config_data.yaml"


@pytest.mark.vault
def test_generate_config_from_template(template_file, data_file):
    with tempfile.TemporaryDirectory() as tmpdir:
        target_file = Path(tmpdir) / "config.yml"

        generate_config_from_template(template_file, data_file, target_file)

        with Path(target_file).open(encoding="utf-8") as f:
            generated_config = f.read()

        print(generated_config)  # noqa: T201

        assert 'secret {\n    path = "kv/netbox/api/read"\n    format = "netbox_{{ key }}"\n    no_prefix = true\n}' in generated_config


def test_generate_config_from_template_file_not_found(template_file):
    # Pass a non-existent data file path

    with tempfile.TemporaryDirectory() as tmpdir:
        target_file = Path(tmpdir) / "config.yml"
        non_existent_data_file = Path(tmpdir) / "does_not_exist.yaml"
        with pytest.raises(FileNotFoundError) as excinfo:
            generate_config_from_template(template_file, non_existent_data_file, target_file)
        assert "was not found" in str(excinfo.value)


def test_generate_config_from_template_permission_error(template_file):
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_data_file = Path(tmpdir) / "data.yaml"
        tmp_data_file.write_text("foo: bar", encoding="utf-8")
        target_file = Path(tmpdir) / "config.yml"
        with patch("pathlib.Path.open", side_effect=PermissionError("Permission denied")):
            with pytest.raises(PermissionError) as excinfo:
                generate_config_from_template(template_file, tmp_data_file, target_file)
            assert "Permission denied" in str(excinfo.value)


def test_generate_config_from_template_invalid_yaml(template_file):
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_data_file = Path(tmpdir) / "invalid.yaml"
        tmp_data_file.write_text("foo: [unclosed_list", encoding="utf-8")
        target_file = Path(tmpdir) / "config.yml"
        with pytest.raises(yaml.YAMLError) as excinfo:
            generate_config_from_template(template_file, tmp_data_file, target_file)
        assert "Error parsing YAML data" in str(excinfo.value)


def test_generate_config_from_template_creates_parent_dirs(template_file, data_file):
    with tempfile.TemporaryDirectory() as tmpdir:
        nested_dir = Path(tmpdir) / "a" / "b" / "c"
        target_file = nested_dir / "config.yml"
        assert not nested_dir.exists()
        generate_config_from_template(template_file, data_file, target_file)
        assert target_file.exists()
