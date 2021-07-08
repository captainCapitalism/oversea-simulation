import pandas

from overseen.read import read_expeditions


def test_read_expeditions(data_dir) -> None:
    expeditions = read_expeditions(data_dir)

    assert isinstance(expeditions, pandas.DataFrame)
