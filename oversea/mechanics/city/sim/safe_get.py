from typing import TypeVar

T = TypeVar("T")


def safe_get(costs: list[list[T]], turn: int):
    try:
        return costs[turn]
    except IndexError:
        return []
