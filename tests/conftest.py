import pytest

from oversea.read import get_data_directory


@pytest.fixture()
def data_dir() -> str:
    return get_data_directory()
