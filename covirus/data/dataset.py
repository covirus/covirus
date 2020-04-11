from abc import abstractmethod
from joblib import Memory


CACHE_DIR = "/tmp/data/"
memory = Memory(CACHE_DIR, verbose=0)


class Dataset:
    def __init__(self, dataset_cache_dir="datasets/"):
        self.cache_dir = CACHE_DIR + dataset_cache_dir
        self.load_data = memory.cache(self.load_data)
        self.load_data()
        self.load_objects()

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def load_objects(self):
        pass
