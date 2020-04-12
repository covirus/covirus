from .exceptions import NotValidCountry
from .brazil.load_br import load_brazillian_dataset


def get_country_data(country, source):
    if country == "BR":
        return load_brazillian_dataset(source)
    raise NotValidCountry(f"You chose a not valid country: {country!r}")
