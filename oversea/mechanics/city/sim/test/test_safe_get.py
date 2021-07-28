from oversea.mechanics.city.sim.safe_get import safe_get


def test_gets_index_element():
    costs = [[1, 7], [9, 4]]
    index = 1
    el = safe_get(costs, index)

    assert el == costs[index]


def test_no_index_returns_empty():
    costs = [[1], [21], [442]]

    index = 33
    el = safe_get(costs, index)

    assert el == []
