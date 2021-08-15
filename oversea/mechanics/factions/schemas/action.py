from pydantic import BaseModel

from oversea.mechanics.factions.schemas.value_objects.building import Building
from oversea.mechanics.factions.schemas.value_objects.colony_data import ColonyData
from oversea.mechanics.factions.schemas.value_objects.income import Income
from oversea.mechanics.factions.schemas.entities.ship import Ship
from oversea.mechanics.factions.schemas.value_objects.ship_data import ShipData


class Action(BaseModel):
    pass


class CreateBuilding(Action):
    target: Building


class CreateShip(Action):
    target: ShipData


class CreateColony(Action):
    target: ColonyData


class IncreaseIncome(Action):
    income: Income


class DispatchShip(Action):
    ship: Ship
