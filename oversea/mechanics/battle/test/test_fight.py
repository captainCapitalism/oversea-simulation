import pytest

from oversea.mechanics.battle.fight import fight


@pytest.mark.parametrize("execution_number", range(1_0_000))
def test_winner_is_returned(
    ship_a,
    ship_b,
    execution_number,
):
    winner = fight(ship_a, ship_b)
    assert winner == ship_a
    if winner == ship_a:
        assert ship_b.current_health == 0
        assert ship_a.current_health > 0
    if winner == ship_b:
        assert ship_a.current_health == 0
        assert ship_b.current_health > 0
