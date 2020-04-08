import pytest


@pytest.fixture(scope="session")
def cache_dir():
    return "/tmp/data/"
