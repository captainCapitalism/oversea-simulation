from os import path

import pandas


def get_data_directory() -> str:
    return path.join(path.dirname(path.dirname(__file__)), "data")


def read_expeditions(data_dir: str) -> pandas.DataFrame:
    PL_ENCODING = "UTF-16"
    return pandas.read_csv(
        path.join(data_dir, "Karty Ekspedycji.csv"),
        encoding=PL_ENCODING,
    )
