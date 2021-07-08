import pandas

from oversea.read import read_csv, read_expeditions


def test_read_expeditions(data_dir) -> None:
    expeditions = read_csv(
        data_dir=data_dir,
        file_name="Karty Ekspedycji.csv",
    )

    assert isinstance(expeditions, pandas.DataFrame)


def test_lazy_reader():
    expeditions = read_expeditions()

    assert isinstance(expeditions, pandas.DataFrame)
