import pytest
from covirus.data import load_dataset


@pytest.fixture(scope="session")
def cache_dir():
    return "/tmp/data/"


@pytest.fixture(scope="session")
def wcota_dataset():
    return load_dataset(country="BR", source="wcota")


@pytest.fixture(scope="session")
def johns_hopkins_dataset():
    return load_dataset(source="JHU")


@pytest.fixture(scope="session")
def ministerio_da_saude_dataset():
    return load_dataset(country="BR", source="ministerio_da_saude")
