from covirus.datasets import load_br
import pandas as pd


def test_import_brazillian_dataset():
    dataset = load_br()
    assert isinstance(dataset, pd.DataFrame)
