from ..br_dataset import BRDataset
from covirus.data.dataset import GitDataset


class WCotaDataset(BRDataset, GitDataset):
    def __init__(self, *args, **kwargs):
        self.repo_name = "covid19br"
        self.git_url = f"https://github.com/wcota/{self.repo_name}.git"
        super().__init__(*args, **kwargs)
        self.cache_dir = f"{self.cache_dir + self.repo_name}/"
        self.joblib_dir = self.joblib_dir + "wcota/load_data/"

    def load_objects(self):
        self.cities_time = self.get_cities_time()
        self.cities = self.get_cities()
        self.states = self.get_states()
        self.total = self.get_total()
        self.cases_with_coordinates = self.get_cases_with_coordinates()
        self.sources = self.get_sources()

    def get_cities_time(self):
        return self.read_file("cases-brazil-cities-time.csv")

    def get_cities(self):
        return self.read_file("cases-brazil-cities.csv")

    def get_states(self):
        return self.read_file("cases-brazil-states.csv")

    def get_total(self):
        return self.read_file("cases-brazil-total.csv")

    def get_cases_with_coordinates(self):
        return self.read_file("cases-gps.csv")

    def get_sources(self):
        return self.read_file("sources.csv")
