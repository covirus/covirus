cd $(git rev-parse --show-toplevel)
set -o pipefail
set -e

pip install pip-tools
pip-compile requirements.in --no-emit-trusted-host --no-index
pip-compile dev-requirements.in --no-emit-trusted-host --no-index