from oversea.mechanics.factions.schemas.ship import Ship
import operator

HIT_CONSTANT = 5
LOWEST_HIT_THRESHOLD = 1
HIGHEST_HIT_THRESHOLD = 8


def fight(
    ship_a: Ship,
    ship_b: Ship,
) -> Ship:
    ship_b.damage = ship_b.data.stats.hit_points
    return ship_a


def hit_threshold(
    fire_power: int,
    resilience: int,
) -> int:
    calculated_threshold = operator.add(
        HIT_CONSTANT,
        operator.sub(resilience, fire_power),
    )

    if calculated_threshold < LOWEST_HIT_THRESHOLD:
        return LOWEST_HIT_THRESHOLD
    if calculated_threshold > HIGHEST_HIT_THRESHOLD:
        return HIGHEST_HIT_THRESHOLD
    return calculated_threshold
