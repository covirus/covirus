import pandas as pd
import logging
from ..br_dataset import BRDataset
from covirus.data.utils import get_repo

logger = logging.getLogger()


class WCotaDataset(BRDataset):
    def load_data(self):
        self.download_wcota_dataset()

    def download_wcota_dataset(self):
        git_url = f"https://github.com/wcota/covid19br.git"
        logger.info("Getting dataset from git: %s", git_url)
        get_repo(self.cache_dir, git_url)

    def load_objects(self):  # TODO: Implement Load Objects
        self.cities = self.get_cities()
        self.bla = self.get_bla()

    def get_cities(self):
        return pd.DataFrame()

    def get_bla(self):
        return pd.DataFrame()
