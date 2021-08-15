from pydantic import BaseModel

from oversea.mechanics.factions.schemas.value_objects.cost import Cost
from oversea.mechanics.factions.schemas.value_objects.income import Income


class ColonyData(BaseModel):
    cost: Cost
    effect: Income
