#!/bin/bash

# This script is used to run tests in the GitLab CI environment.
export GITLAB_CI_DIR=$(pwd)
# Get the directory of this script
export SCRIPTS_DIR=$(dirname "$0")

# Run the script to generate the envconsul config file and if successful, print the contents of the generated file.
(VAULT_MATRIX=$GITLAB_CI_DIR/tests/vault/vault_matrix ${SCRIPTS_DIR}/vault/generate_envconsul_config.sh && cat .vault/envconsul.hcl) || {
    printf "\033[0;31m✘\033[0m Failed to generate envconsul config file.\n"
    exit 1
}
