from typing import List

from pydantic import BaseModel

from oversea.mechanics.factions.schemas.value_objects.bank import Bank
from oversea.mechanics.factions.schemas.value_objects.base_resources import (
    BaseResources,
)
from oversea.mechanics.factions.schemas.value_objects.building import Building
from oversea.mechanics.factions.schemas.value_objects.colony_data import ColonyData
from oversea.mechanics.factions.schemas.entities.fleet import Fleet
from oversea.mechanics.factions.schemas.value_objects.income import Income
from oversea.mechanics.factions.schemas.value_objects.ship_data import ShipData, Stats


class Faction(BaseModel):

    name: str
    base_resources: BaseResources
    base_income: BaseResources
    buildings: List[Building]
    ships: List[ShipData]
    stronghold_stats: Stats
    income: Income
    bank: Bank
    fleet: Fleet
    colony_data: ColonyData

    class Config:
        extra = "forbid"
