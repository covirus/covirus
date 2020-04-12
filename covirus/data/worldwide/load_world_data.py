from .sources import johns_hopkins


def load_world_dataset(source):
    if source.lower() in johns_hopkins.NAMES:
        return johns_hopkins.JohnsHopkinsDataset()

    raise ValueError(f"Source not Valid {source!r}")
