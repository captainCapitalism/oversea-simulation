from hypothesis import given, strategies

from oversea.mechanics.battle.fight import (
    hit_threshold,
    HitThresholds,
)
from oversea.utils import inclusive_range


def test_cannot_be_below_min():
    fire_power = 100
    resilience = 1
    threshold = hit_threshold(
        fire_power=fire_power,
        resilience=resilience,
    )

    assert threshold == HitThresholds.LOW


def test_cannot_exceed_8():
    fire_power = 1
    resilience = 100

    threshold = hit_threshold(
        fire_power=fire_power,
        resilience=resilience,
    )

    assert threshold == HitThresholds.HIGH


@given(
    fire_power=strategies.integers(min_value=1, max_value=8),
    resilience=strategies.integers(min_value=1, max_value=8),
)
def test_dice_rolls_are_in_range(
    fire_power: int,
    resilience: int,
):
    threshold = hit_threshold(
        fire_power=fire_power,
        resilience=resilience,
    )
    assert threshold in inclusive_range(HitThresholds.LOW, HitThresholds.HIGH)


@given(
    fire_power=strategies.integers(),
    resilience=strategies.integers(),
)
def test_random_numbers_are_in_range(
    fire_power: int,
    resilience: int,
):
    threshold = hit_threshold(
        fire_power=fire_power,
        resilience=resilience,
    )
    assert threshold in inclusive_range(HitThresholds.LOW, HitThresholds.HIGH)
