import enum
import operator

from oversea.mechanics.factions.schemas.ship import Ship


class HitThresholds(int, enum.Enum):
    BASE = 5
    LOW = 1
    HIGH = 8


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
        HitThresholds.BASE,
        operator.sub(resilience, fire_power),
    )

    if calculated_threshold < HitThresholds.LOW:
        return HitThresholds.LOW
    if calculated_threshold > HitThresholds.HIGH:
        return HitThresholds.HIGH
    return calculated_threshold
