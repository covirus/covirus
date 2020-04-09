cd $(git rev-parse --show-toplevel)
set -o pipefail
set -e

if [[ $BUILD ]];
    then docker-compose build;
fi

docker-compose run --rm covirus bash -c "
    pytest -x -s -vv -p no:cacheprovider "$@" covirus/tests/
"

if [[ $CLEANUP ]]; then docker-compose stop; fi
