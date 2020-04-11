import os
import stat
import logging

logger = logging.getLogger()


def create_data_dir(path):
    logger.info(f"Creating folder at %s", path)
    os.makedirs(path, exist_ok=True)


def reset_cache(path):
    if cache_exists(path):
        logger.info(f"Resetting cache folder: %s", path)
        rmdir(path)
    create_data_dir(path)


def cache_exists(path):
    return os.path.exists(path)


def rmdir(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(top)
