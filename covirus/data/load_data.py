from .countries.load_data import get_country_data
from .dataset import COVIDDataset
from abc import abstractmethod


def load_dataset(source=None, country=None) -> COVIDDataset:
    if is_all_null(source, country):
        raise ValueError("You must specify a source or/and country argument")
    return get_data(country, source)


def get_data(country, source):
    if country is not None:
        data = get_country_data(country, source)
    else:
        raise NotImplementedError
    return data


def is_all_null(*args):
    return all(v is None for v in args)
