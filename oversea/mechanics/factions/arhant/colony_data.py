from oversea.mechanics.factions.schemas.colony_data import ColonyData
from oversea.mechanics.factions.schemas.cost import Cost
from oversea.mechanics.factions.schemas.income import Income

colony_data = ColonyData(
    cost=Cost(cash=4),
    effects=[Income(cash=2)],
    rewards=[],
)
