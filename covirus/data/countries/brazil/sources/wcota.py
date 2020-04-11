import pandas as pd
import logging
from ..br_dataset import BRDataset
from covirus.data.utils import get_repo, reset_cache

logger = logging.getLogger()


class WCotaDataset(BRDataset):
    def __init__(self, *args, **kwargs):
        self.repo_name = 'covid19br'
        super().__init__(*args, **kwargs)
        self.cache_dir = f"{self.cache_dir + self.repo_name}/"
        self.joblib_dir = self.joblib_dir + "wcota/load_data/"

    def load_data(self):
        self.download_wcota_dataset()

    def download_wcota_dataset(self):
        git_url = f"https://github.com/wcota/{self.repo_name}.git"
        logger.info("Getting dataset from git: %s", git_url)
        reset_cache(self.cache_dir, self.joblib_dir)
        get_repo(self.cache_dir, git_url)

    def load_objects(self):  # TODO: Implement Load Objects
        self.cities = self.get_cities()
        self.bla = self.get_bla()

    def get_cities(self):
        return pd.DataFrame()

    def get_bla(self):
        return pd.DataFrame()
