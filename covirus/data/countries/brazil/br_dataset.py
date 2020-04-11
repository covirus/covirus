from covirus.data.dataset import Dataset

class BRDataset(Dataset):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def get_dataset_dir(self):
        return "br/"