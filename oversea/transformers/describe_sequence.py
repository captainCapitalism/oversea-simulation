from typing import Union, List

from pydantic import BaseModel
import statistics


class Description(BaseModel):
    mean: float
    stdev: float
    median: float


def describe(data: List[Union[int, float]]) -> Description:

    return Description(
        mean=statistics.mean(data),
        stdev=statistics.stdev(data),
        median=statistics.stdev(data),
    )
