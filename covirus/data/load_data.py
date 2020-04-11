from .countries.load_data import get_country_data
from .dataset import Dataset
from abc import abstractmethod


def load_dataset(source=None, country=None) -> Dataset:
    """Function to load one of the lib-provided datasets
    
    Args:
        source (str): Must pass a source name.
            Available Worldwide Sources:
            There are no Worldwide (country=None) sources yet.
        country (str): Define the country of the source.
            Available Countries and Sources:
            "BR":
                "wcota":
                    Casos e óbitos confirmados por dia, utilizando informação oficial pelo Ministério da Saúde, 
                    dados no nível municipal do Brasil.IO e dados mais recentes reportados pela equipe do @CoronavirusBra1.
                    Objects:
                        - cities
                        - cities_time
                        - states
                        - total
                    Source: https://github.com/wcota/covid19br
    
    Raises:
        ValueError: ValueError is raised if source AND country is none, since you must define WHICH dataset you want.   
    
    Returns:
        Dataset: Dataset object, which may contain several pd.Dataframe inside within its objects.
    """
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
