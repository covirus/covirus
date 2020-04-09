import logging
from .sources import (WCotaDataset)

logger = logging.getLogger()


def load_brazillian_dataset(source):
    logger.info("Loading %s data", source)
    if source == "wcota":
        dataset = WCotaDataset()
    else:
        raise ValueError(f"Dataset Could not be Retrived: {source!r}, is it available?")
    return dataset
