from ..world_dataset import WorldDataset
from covirus.data.dataset import GitDataset
from datetime import datetime

NAMES = ["jhu", "johns_hopkins", "johnshopkins"]

"CSSEGISandData"


class JohnsHopkinsDataset(WorldDataset, GitDataset):
    def __init__(self, *args, **kwargs):
        self.repo_name = "COVID-19"
        self.git_url = f"https://github.com/CSSEGISandData/{self.repo_name}.git"
        super().__init__(*args, **kwargs)
        self.cache_dir = f"{self.cache_dir + self.repo_name}/"
        self.joblib_dir = self.joblib_dir + "johns_hopkins/load_data/"

    def load_objects(self):
        self.iso_codes = self.get_iso_entities_codes()
        self.who_report = self.get_who_report()
        self.load_timeline_data()

    def get_iso_entities_codes(self):
        data_dir = "csse_covid_19_data/"
        filename = "UID_ISO_FIPS_LookUp_Table.csv"
        return self.read_file(data_dir + filename)

    def get_who_report(self):
        data_dir = "who_covid_19_situation_reports/who_covid_19_sit_rep_time_series/"
        filename = "who_covid_19_sit_rep_time_series.csv"
        return self.read_file(data_dir + filename)

    def report(self, date):
        formatted_date = JohnsHopkinsDataset.format_date(date)
        daily_reports_path = "csse_covid_19_data/" + "csse_covid_19_daily_reports/"
        file_path = daily_reports_path + f"{formatted_date}.csv"
        return self.read_file(file_path, ignore_repo=True)

    def load_timeline_data(self):
        self.load_global_timeline_data()
        self.load_us_timeline_data()

    def load_global_timeline_data(self):
        self.timeline = dict(
            deaths=self.read_timeline_file("deaths"),
            recovered=self.read_timeline_file("recovered"),
            confirmed=self.read_timeline_file("confirmed"),
        )

    def load_us_timeline_data(self):
        self.timeline["US"] = dict(
            deaths=self.read_timeline_file("deaths", US=True),
            confirmed=self.read_timeline_file("confirmed", US=True),
        )

    def read_timeline_file(self, info_name, US=False):
        timeseries_dir = "csse_covid_19_data/csse_covid_19_time_series/"
        location_modifier = "global"
        if US:
            location_modifier = "US"
        return self.read_file(
            timeseries_dir + f"time_series_covid19_{info_name}_{location_modifier}.csv"
        )

    @staticmethod
    def format_date(date):
        date = JohnsHopkinsDataset.get_date(date)
        return date.strftime("%d-%m-%Y")

    @staticmethod
    def get_date(date):
        if not isinstance(date, datetime):
            if isinstance(date, str):
                date = datetime.strptime(date, "%d-%m-%Y")
            else:
                raise TypeError
        return date.date()
