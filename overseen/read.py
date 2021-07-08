from os import path
from typing import Callable

import pandas

from tests.filenames import Filenames, PL_ENCODING


def get_data_directory() -> str:
    return path.join(path.dirname(path.dirname(__file__)), "data")


def read_csv(
    data_dir: str,
    file_name: str,
    encoding: str = PL_ENCODING,
) -> pandas.DataFrame:
    return pandas.read_csv(
        path.join(data_dir, file_name),
        encoding=encoding,
    )


def lazy_reader(
    file_name: str,
    encoding: str = PL_ENCODING,
) -> Callable[[], pandas.DataFrame]:
    data_dir = get_data_directory()

    def wrapper() -> pandas.DataFrame:
        return read_csv(
            data_dir=data_dir,
            file_name=file_name,
            encoding=encoding,
        )

    return wrapper


read_expeditions = lazy_reader(Filenames.expeditions)
read_intrigues = lazy_reader(Filenames.intrigues)
