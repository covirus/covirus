from ..world_dataset import WorldDataset
import os
import pandas as pd

NAMES = ["cbc", "news", "cbc_news", "cbcNews"]
this_dir, this_filename = os.path.split(__file__)

def load():
    return pd.read_csv(this_dir + "/data/news.csv")