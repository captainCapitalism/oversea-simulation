import pytest

from oversea.mechanics.factions.arhant.ships import Galley


@pytest.fixture()
def ship_a():
    return Galley()


@pytest.fixture()
def ship_b():
    return Galley()
