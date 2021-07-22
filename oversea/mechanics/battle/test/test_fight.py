from oversea.mechanics.battle.fight import fight


def test_winner_is_returned(ship_a, ship_b):
    winner = fight(ship_a, ship_b)

    if winner == ship_a:
        assert ship_b.current_health == 0
        assert ship_a.current_health > 0
    if winner == ship_b:
        assert ship_a.current_health == 0
        assert ship_b.current_health > 0