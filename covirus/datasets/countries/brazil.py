import logging
from ..utils import create_data_dir, reset_cache_folder, get_repo, cache_exists

logger = logging.getLogger()
GIT_DIR_NAME = "covid19br"
GIT_PATH = f"https://github.com/wcota/{GIT_DIR_NAME}.git"


def load_br(path="/tmp/data", use_cache=False):
    create_data_dir(path)
    load_dataset(path, use_cache)


def load_dataset(path, use_cache):
    logger.info("Loading Brazillian Dataset")
    if use_cache and cache_exists(path + GIT_DIR_NAME):
        logger.info("Using Cache for Brazil's Dataset")
    else:
        reset_cache_folder(path + GIT_DIR_NAME)
        get_repo(path, GIT_PATH)
