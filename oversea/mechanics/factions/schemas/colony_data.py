from pydantic import BaseModel

from oversea.mechanics.factions.schemas.cost import Cost
from oversea.mechanics.factions.schemas.income import Income, Reward


class ColonyData(BaseModel):
    cost: Cost
    effects: list[Income]
    rewards: list[Reward]
