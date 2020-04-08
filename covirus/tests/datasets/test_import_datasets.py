import pytest
from covirus.datasets import CountryDataLoader
import pandas as pd
import os


def test_import_wcota(cache_dir):
    dataloader = CountryDataLoader()
    wcota_data = dataloader.load("BR", "wcota")
    assert os.path.exists(cache_dir + "covid19br/" + "cases-brazil-cities.csv")
    assert isinstance(wcota_data.cities, pd.DataFrame)


def test_import_invalid_source(cache_dir):
    dataloader = CountryDataLoader()
    with pytest.raises(ValueError) as e:
        assert dataloader.load("BR", "bond")


def test_import_invalid_country(cache_dir):
    dataloader = CountryDataLoader()
    with pytest.raises(ValueError) as e:
        assert dataloader.load("OK")
