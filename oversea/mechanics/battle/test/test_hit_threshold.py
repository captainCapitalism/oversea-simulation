from oversea.mechanics.battle.fight import (
    hit_threshold,
    HitThresholds,
)


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
