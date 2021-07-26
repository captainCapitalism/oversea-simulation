import enum

from oversea.utils import inclusive_range


class K8(int, enum.Enum):
    MIN: int = 1
    MAX: int = 8

    @classmethod
    def in_range(cls):
        return inclusive_range(cls.MIN, cls.MAX)
