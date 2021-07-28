from typing import Optional, Union

from pydantic import BaseModel

from oversea.mechanics.factions.schemas.cost import Cost
from oversea.mechanics.factions.schemas.income import Income


class Building(BaseModel):
    name: str
    effect: Union[str, Income]
    cost: Cost
    requirement: Optional["Building"]


Building.update_forward_refs()
