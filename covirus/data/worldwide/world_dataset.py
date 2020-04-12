from ..dataset import Dataset


class WorldDataset(Dataset):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.joblib_dir = self.joblib_dir + "world/sources/"

    def get_dataset_dir(self):
        return "world/"
