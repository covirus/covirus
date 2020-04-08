from covirus.datasets import load_br
import pandas as pd
import os
from unittest import mock


def test_import_brazillian_dataset(cache_dir):
    load_br(cache_dir, use_cache=False)
    assert os.path.exists(cache_dir + "covid19br/" + "cases-brazil-cities.csv")
