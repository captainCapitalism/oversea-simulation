from oversea.mechanics.factions.schemas.value_objects.colony_data import ColonyData
from oversea.mechanics.factions.schemas.value_objects.cost import Cost
from oversea.mechanics.factions.schemas.value_objects.income import Income

colony_data = ColonyData(
    cost=Cost(cash=4),
    effect=Income(cash=2),
)
