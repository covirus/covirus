from covirus.data.dataset import Dataset

class BRDataset(Dataset):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cache_dir = self.cache_dir + "br/"