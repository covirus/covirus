import pytest
from covirus.data import load_dataset
from covirus.data.countries.exceptions import NotValidCountry
import pandas as pd
import os


def test_import_wcota(cache_dir, wcota_dataset):
    assert os.path.exists(wcota_dataset.cache_dir + "cases-brazil-cities.csv")
    assert isinstance(wcota_dataset.cities, pd.DataFrame)
    assert "RJ" in wcota_dataset.states["state"].values


def test_import_invalid_source():
    with pytest.raises(ValueError):
        assert load_dataset(country="BR", source="bond")


def test_import_not_country_parameters():
    with pytest.raises(NotValidCountry):
        assert load_dataset(country="OK")


def test_import_not_country_parameters():
    with pytest.raises(ValueError):
        assert load_dataset()
