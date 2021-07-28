from oversea.mechanics.battle.fight import shoot
from oversea.mechanics.factions.schemas.ship import Ship


def test_shoot(
    ship_a: Ship,
    ship_b: Ship,
):
    hit = shoot(ship_a.data.stats, ship_b.data.stats)

    assert hit
