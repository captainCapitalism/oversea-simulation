from typing import TypeVar

T = TypeVar("T")


def safe_get(objects: list[list[T]], turn: int):
    try:
        return objects[turn]
    except IndexError:
        return []
