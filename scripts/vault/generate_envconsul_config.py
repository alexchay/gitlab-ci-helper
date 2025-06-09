import sys

from gitlab_ci.generate_config import generate_config_from_template

if __name__ == "__main__":
    # pylint: disable=invalid-name
    _, _template_name, _matrix_file, _target_file, *script_args = sys.argv
    # the execution starts here
    generate_config_from_template(_template_name, _matrix_file, _target_file)
