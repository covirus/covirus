import git
from .storage_handlers import reset_cache
import logging

logger = logging.getLogger()


def get_repo(path, url):
    logger.info(f"Getting dataset from git: %s, file will be saved at %s", url, path)
    git.Git(path).clone(url)
    logger.info(f"Saved dataset on: %s", path)
