import enum
import operator
from typing import Tuple

from oversea.mechanics.casino.games import K8
from oversea.mechanics.casino.roll import roll
from oversea.mechanics.factions.schemas.ship import Ship
from oversea.mechanics.factions.schemas.ship_data import Stats


class HitThresholds(int, enum.Enum):
    BASE = 5
    LOW = 1
    HIGH = 8


def fight(
    ship_a: Ship,
    ship_b: Ship,
) -> Ship:
    aggressor = ship_a
    defender = ship_b
    while ship_a.current_health and ship_b.current_health:
        [defender, aggressor] = fire(
            aggressor=aggressor,
            defender=defender,
        )

    return defender


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


def is_hit(
    roll_result: int,
    threshold: int,
) -> bool:
    return roll_result >= threshold


def shoot(
    aggressor: Stats,
    defender: Stats,
) -> bool:
    return is_hit(
        roll_result=roll(K8.in_range()),
        threshold=hit_threshold(
            fire_power=aggressor.fire_power,
            resilience=defender.resilience,
        ),
    )


def fire(
    aggressor: Ship,
    defender: Ship,
) -> Tuple[Ship, Ship]:
    shoot_result = shoot(
        aggressor=aggressor.data.stats,
        defender=defender.data.stats,
    )
    if shoot_result:
        defender.get_hit()

    return aggressor, defender
