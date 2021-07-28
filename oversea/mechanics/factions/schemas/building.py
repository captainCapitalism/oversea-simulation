from typing import Optional

from pydantic import BaseModel

from oversea.mechanics.factions.schemas.cost import Cost


class Building(BaseModel):
    name: str
    effect: str
    cost: Cost
    requirement: Optional["Building"]


Building.update_forward_refs()
