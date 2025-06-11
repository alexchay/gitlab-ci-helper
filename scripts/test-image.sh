#!/bin/bash

# This script is focused on testing the Docker image itself (e.g., checking that files, binaries, or configurations are present in the image,
# but not actually running the containerized application).

set -euo pipefail

echo "task version = " "$(task --version)"
echo "crane version = " "$(crane version)"
echo "envconsul version = " "$(envconsul -v)"

echo ""

export GITLAB_CI_DIR=$(pwd)
export SCRIPTS_DIR=$(dirname "$0")

# Run the script to generate the envconsul config file and if successful, print the contents of the generated file.
( \
VAULT_MATRIX="$GITLAB_CI_DIR/tests/vault/vault_matrix" \
  TARGET_CONFIG="$HOME/.vault/envconsul.hcl" \
 ${SCRIPTS_DIR}/vault/generate_envconsul_config.sh && cat "$HOME/.vault/envconsul.hcl" \
 ) || {
    printf "\033[0;31m✘\033[0m Failed to generate envconsul config file.\n"
    exit 1
}
