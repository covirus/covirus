cd $(git rev-parse --show-toplevel)
set -o pipefail
set -e

pip-compile requirements.in --no-emit-trusted-host --no-index
pip-compile dev-requirements.in --no-emit-trusted-host --no-index