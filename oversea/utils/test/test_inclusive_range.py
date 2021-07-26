from hypothesis import given, strategies

from oversea.utils import inclusive_range


@given(
    min=strategies.integers(),
    max=strategies.integers(),
)
def test_inclusive_range(
    min: int,
    max: int,
):
    assert inclusive_range(min, max) == range(min, max + 1)
