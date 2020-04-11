from covirus.data.dataset import Dataset

class BRDataset(Dataset):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.joblib_dir = self.joblib_dir + "countries/brazil/sources/"


    def get_dataset_dir(self):
        return "br/"