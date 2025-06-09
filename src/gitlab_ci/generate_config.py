"""Generate configuration files from Jinja2 templates and YAML data."""
# pylint: disable=wrong-import-order
import json
import logging
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from yaml.error import YAMLError

logger = logging.getLogger(__name__)


def generate_config_from_template(template_file: str | Path, data_file: str | Path, target_file: str | Path) -> None:
    """
    Generate a configuration file from a Jinja2 template and a YAML data file.

    :param template_file: The path to the Jinja2 template file.
    :param data_file: The path to the YAML data file.
    :param target_file: The path to the target configuration file to be generated.

    :raises FileNotFoundError: If the data file is not found.
    :raises PermissionError: If the data file cannot be read due to permissions.
    :raises YAMLError: If the YAML data is invalid.
    """
    # Load YAML data into structured data, handle potential YAMLError
    try:
        with Path(data_file).open("r", encoding="utf-8") as data_yaml:
            data = yaml.safe_load(data_yaml)
    except FileNotFoundError:
        msg = f"The data file '{data_file}' was not found."
        raise FileNotFoundError(msg) from None
    except PermissionError:
        msg = f"Permission denied when trying to read the data file '{data_file}'."
        raise PermissionError(msg) from None
    except YAMLError as err:
        msg = f"Error parsing YAML data from file '{data_file}': {err}"
        raise YAMLError(msg) from err

    # Setup the jinja2 templating environment and render the template
    j2_env = Environment(
        loader=FileSystemLoader(Path(template_file).parent), trim_blocks=True, autoescape=select_autoescape(["html", "xml", "j2"])
    )
    j2_env.filters["to_json"] = json.dumps

    # Render template with YAML data
    template = j2_env.get_template(Path(template_file).name)
    generated_config = template.render(data=data)

    # Ensure the parent directories exist; create them if necessary (parents=True),
    # and avoid raising an error if they already exist (exist_ok=True).
    Path(target_file).parent.mkdir(parents=True, exist_ok=True)
    with Path(target_file).open("w", encoding="utf-8") as target_file_out:
        target_file_out.write(generated_config)
        logger.info("Generated config file was saved to %s", target_file_out.name)
