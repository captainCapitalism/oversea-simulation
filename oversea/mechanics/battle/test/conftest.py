import pytest

from oversea.mechanics.factions.schemas.ship import Ship
from oversea.mechanics.factions.arhant.ships import galley


@pytest.fixture()
def ship_a():
    return Ship(data=galley)


@pytest.fixture()
def ship_b():
    return Ship(data=galley)
