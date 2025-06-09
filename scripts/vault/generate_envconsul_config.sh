#!/bin/bash

# Description: Generate envconsul config file from vault matrix file
if [ -n "$VAULT_MATRIX" ]; then
    echo "$VAULT_MATRIX"
    CI_PROJECT_NAME_LC=$(echo "$CI_PROJECT_NAME" | awk '{print tolower($0)}'); export CI_PROJECT_NAME_LC;
    CI_ENVIRONMENT_NAME_LC=$(echo "$CI_ENVIRONMENT_NAME" | awk '{print tolower($0)}'); export CI_ENVIRONMENT_NAME_LC;
    cat "$VAULT_MATRIX"; echo

    python3 "${GITLAB_CI_DIR}/scripts/vault/generate_envconsul_config.py" \
        "${GITLAB_CI_DIR}/scripts/vault/envconsul_config.j2" "${VAULT_MATRIX}" .vault/envconsul.hcl
fi
