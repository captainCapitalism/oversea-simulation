from pydantic import BaseModel

from oversea.mechanics.factions.schemas.cost import Cost
from oversea.mechanics.factions.schemas.income import Income


class ColonyData(BaseModel):
    cost: Cost
    income: Income
