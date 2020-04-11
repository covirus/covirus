from abc import abstractmethod
from joblib import Memory


CACHE_DIR = "/tmp/covirus/data/"
memory = Memory(CACHE_DIR, verbose=0)


class Dataset:
    def __init__(self):
        self.load_data = memory.cache(self.load_data)
        self.cache_dir = self.get_cache_dir()
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