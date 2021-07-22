from oversea.mechanics.factions.schemas.ship import Ship


def fight(ship_a: Ship, ship_b: Ship) -> Ship:
    ship_b.damage = ship_b.data.stats.hit_points
    return ship_a
