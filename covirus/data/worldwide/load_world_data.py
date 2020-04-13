from .sources import johns_hopkins, cbc_news


def load_world_dataset(source):
    if source.lower() in johns_hopkins.NAMES:
        return johns_hopkins.JohnsHopkinsDataset()
    elif source in cbc_news.NAMES:
        return cbc_news.load()

    raise ValueError(f"Source not Valid {source!r}")
