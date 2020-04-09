import git
from .storage_handlers import reset_cache_folder_if_exists
import logging

logger = logging.getLogger()


def get_repo(path, url):
    reset_cache_folder_if_exists(path)
    logger.info(f"Getting dataset from git: %s, file will be saved at %s", url, path)
    git.Git(path).clone(url)
    logger.info(f"Saved dataset on: %s", path)
