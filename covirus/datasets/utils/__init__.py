import os
import git
import stat
import logging

logger = logging.getLogger()


def create_data_dir(path):
    logger.info(f"Data will be stored at {path!r}")
    os.makedirs(path, exist_ok=True)


def get_repo(path, url):
    logger.info(f"Getting dataset from git: {url!r}")
    git.Git(path).clone(url)
    logger.info(f"Saved dataset on: {path!r}")


def cache_exists(path):
    return os.path.exists(path)


def reset_cache_folder(path):
    logger.info(f"Resetting cache folder: {path!r}")
    if os.path.exists(path):
        rmdir(path)


def rmdir(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(top)
