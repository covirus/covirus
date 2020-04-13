from covirus.data import load_dataset
import pandas as pd

def test_import_news_dataset():
    data = load_dataset("news")
    assert isinstance(data, pd.DataFrame)