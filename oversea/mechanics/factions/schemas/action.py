from pydantic import BaseModel

from oversea.mechanics.factions.schemas.building import Building
from oversea.mechanics.factions.schemas.colony_data import ColonyData
from oversea.mechanics.factions.schemas.income import Income
from oversea.mechanics.factions.schemas.ship_data import ShipData


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
