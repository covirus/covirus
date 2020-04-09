from abc import abstractmethod
from joblib import Memory


CACHE_DIR = "/tmp/data/br"
memory = Memory(CACHE_DIR, verbose=1)


class COVIDDataset:
    def __init__(self, cache_dir="/tmp/data/br"):
        self.cache_dir = cache_dir
        self.load_data = memory.cache(self.load_data)
        self.load_data()
        self.load_objects()

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def load_objects(self):
        pass
