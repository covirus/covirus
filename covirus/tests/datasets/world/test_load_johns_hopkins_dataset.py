import pytest
from covirus.data import load_dataset
from covirus.data.countries.exceptions import NotValidCountry
import pandas as pd
import os


def test_import_johns_hopkins(cache_dir, johns_hopkins_dataset):
    assert os.path.exists(johns_hopkins_dataset.cache_dir + "csse_covid_19_data")
    assert isinstance(johns_hopkins_dataset.who_report, pd.DataFrame)
    assert isinstance(johns_hopkins_dataset.report("02-02-2020"), pd.DataFrame)
