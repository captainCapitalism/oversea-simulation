from oversea.mechanics.battle.fight import (
    hit_threshold,
    LOWEST_HIT_THRESHOLD,
    HIGHEST_HIT_THRESHOLD,
)


def test_cannot_be_below_min():
    fire_power = 100
    resilience = 1
    threshold = hit_threshold(
        fire_power=fire_power,
        resilience=resilience,
    )

    assert threshold == LOWEST_HIT_THRESHOLD


def test_cannot_exceed_8():
    fire_power = 1
    resilience = 100

    threshold = hit_threshold(
        fire_power=fire_power,
        resilience=resilience,
    )

    assert threshold == HIGHEST_HIT_THRESHOLD
