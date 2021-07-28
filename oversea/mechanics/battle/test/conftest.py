import pytest

from oversea.mechanics.factions.schemas.ship import Ship
from oversea.mechanics.factions.arhant.ships import galley, silent_arc, black_boat


@pytest.fixture()
def ship_a() -> Ship:
    return Ship(data=galley)


@pytest.fixture()
def ship_b() -> Ship:
    return Ship(data=black_boat)
