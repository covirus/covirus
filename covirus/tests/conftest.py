import pytest
from covirus.data import load_dataset


@pytest.fixture(scope="session")
def cache_dir():
    return "/tmp/data/"


@pytest.fixture(scope="session")
def wcota_dataset():
    return load_dataset(country="BR", source="wcota")
