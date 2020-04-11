from abc import abstractmethod
import itertools
from joblib import Memory
import glob

DATA_FORMATS = ["csv", "parquet", "pickle", "pkl"]
CACHE_DIR = "/tmp/covirus/data/"
memory = Memory(CACHE_DIR, verbose=0)


class Dataset:
    def __init__(self):
        self.load_data = memory.cache(self.load_data)
        self.cache_dir = self.get_cache_dir()
        self.joblib_dir = CACHE_DIR + "joblib/covirus/data/"
        self.load_data()
        self.load_objects()

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def load_objects(self):
        pass

    def get_cache_dir(self):
        return CACHE_DIR + "datasets/" + self.get_dataset_dir()

    @abstractmethod
    def get_dataset_dir(self):
        pass

    def list_dataset_files(self):
        dataset_files = [glob.glob(self.cache_dir + f"*.{ext}") for ext in DATA_FORMATS]
        return list(itertools.chain(*dataset_files))
