from oversea.mechanics.factions.schemas.ship_data import ShipData


def fight(ship_a: ShipData, ship_b: ShipData) -> ShipData:
    ship_b.damage = ship_b.stats.hit_points
    return ship_a
