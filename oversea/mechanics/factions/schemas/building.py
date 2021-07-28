from typing import Optional, Union

from pydantic import BaseModel

from oversea.mechanics.factions.schemas.cost import Cost
from oversea.mechanics.factions.schemas.income import Income, Reward


class Building(BaseModel):
    name: str
    effects: list[Union[str, Income]] = []
    rewards: list[Reward] = []
    cost: Cost
    requirement: Optional["Building"]

    class Config:
        frozen = True


Building.update_forward_refs()
