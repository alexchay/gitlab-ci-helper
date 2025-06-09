#!/bin/bash

# Description: Download and install envconsul binary depending on the OS and architecture and version
# specified in the .envconsul_version file, check downloaded binary against checksum in .envconsul_version file
# and unzip binary to bin directory

# get the directory of this script
set -e
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo "$SCRIPT_DIR"
# shellcheck source=scripts/vault/.envconsul_version
source "${SCRIPT_DIR}/.envconsul_version"
curl -4 -fsSL -o envconsul.zip "https://releases.hashicorp.com/envconsul/${ENVCONSUL_VERSION}/envconsul_${ENVCONSUL_VERSION}_linux_${ENVCONSUL_ARCH:-amd64}.zip"
echo "${ENVCONSUL_SHA256SUM} envconsul.zip" | sha256sum -c -
unzip -o envconsul.zip -d "$SCRIPT_DIR/../../bin"
rm envconsul.zip
