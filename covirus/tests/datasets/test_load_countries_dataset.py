import pytest
from covirus.data import load_dataset
from covirus.data.countries.exceptions import NotValidCountry
import pandas as pd
import os


def test_import_wcota(cache_dir):
    wcota_data = load_dataset(country="BR", source="wcota")
    assert os.path.exists(cache_dir + "covid19br/" + "cases-brazil-cities.csv")
    assert isinstance(wcota_data.cities, pd.DataFrame)


def test_import_invalid_source():
    with pytest.raises(ValueError):
        assert load_dataset(country="BR", source="bond")


def test_import_empty_country():
    with pytest.raises(NotImplementedError):
        assert load_dataset(source="some_source")


def test_import_not_country_parameters():
    with pytest.raises(NotValidCountry):
        assert load_dataset(country="OK")


def test_import_not_country_parameters():
    with pytest.raises(ValueError):
        assert load_dataset()
