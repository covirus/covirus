cd $(git rev-parse --show-toplevel)
set -o pipefail
set -e

if [[  ! $NOBUILD ]];
    then docker-compose build;
fi

docker-compose run --rm covirus bash -c "
    pytest -x -s -vv -p no:cacheprovider --log-level=INFO "$@" covirus/tests/
"
