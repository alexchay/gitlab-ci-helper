#!/bin/bash
#
set -e

if [ -n "${VAULT_ROLE}" ]; then
    curl -4 -v "${VAULT_ADDR}/v1/sys/health"
    VAULT_LOGIN_OUTPUT=$(curl -4 --request POST --data "{\"jwt\": \"${CI_JOB_JWT}\", \"role\": \"${VAULT_ROLE}\"}" "${VAULT_ADDR}/v1/auth/jwt/login"); export VAULT_LOGIN_OUTPUT;
    VAULT_TOKEN=$(echo "$VAULT_LOGIN_OUTPUT" | jq -r '.auth.client_token'); export VAULT_TOKEN;
    VAULT_ACCESSOR=$(echo "$VAULT_AUTH_OUTPUT" | jq -r '.auth.accessor'); export VAULT_ACCESSOR;
    #
    if [ -n "$VAULT_TOKEN" ] || [ "$VAULT_TOKEN" == "null" ]; then
        echo "ERROR: \$VAULT_TOKEN is empty, could be a bad login.";
        echo "$VAULT_LOGIN_OUTPUT";
        exit 1;
    else
        echo "\$VAULT_TOKEN is NOT empty, proceeding ..";
    fi
fi
