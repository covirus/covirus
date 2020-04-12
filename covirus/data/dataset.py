import pandas as pd
from abc import abstractmethod
import itertools
from joblib import Memory
import glob
from covirus.data.utils import get_repo, reset_cache
import logging

logger = logging.getLogger()

DATA_FORMATS = ["csv", "parquet", "pickle", "pkl"]
CACHE_DIR = "/tmp/covirus/data/"
memory = Memory(CACHE_DIR, verbose=0)


class Dataset:
    def __init__(self):
        self.download = memory.cache(self.download)
        self.cache_dir = self.get_cache_dir()
        self.joblib_dir = CACHE_DIR + "joblib/covirus/data/"
        self.load_data()
        self.load_objects()

    def load_data(self):
        self.download()

    @abstractmethod
    def download(self):
        pass

    @abstractmethod
    def load_objects(self):
        pass

    @abstractmethod
    def read_file(self, filename: str) -> pd.DataFrame:
        pass

    def get_cache_dir(self):
        return CACHE_DIR + "datasets/" + self.get_dataset_dir()

    @abstractmethod
    def get_dataset_dir(self):
        pass

    def list_dataset_files(self):
        dataset_files = [glob.glob(self.cache_dir + f"*.{ext}", recursive=True) for ext in DATA_FORMATS]
        return list(itertools.chain(*dataset_files))


class GitDataset(Dataset):
    def download(self):
        logger.info("Getting dataset from git: %s", self.git_url)
        reset_cache(self.cache_dir, self.joblib_dir)
        get_repo(self.cache_dir, self.git_url)
