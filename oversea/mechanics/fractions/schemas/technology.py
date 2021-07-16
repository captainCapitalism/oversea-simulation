from typing import Optional

from pydantic import BaseModel

from oversea.mechanics.fractions.schemas.cost import Cost


class Technology(BaseModel):
    name: str
    effect: str
    cost: Cost
    requirement: Optional["Technology"]


Technology.update_forward_refs()
