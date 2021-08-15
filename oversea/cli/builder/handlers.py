import enum
import json
import os.path
from typing import TypeVar

from oversea.mechanics.factions.schemas.action import (
    Action,
    CreateBuilding,
    CreateShip,
    CreateColony,
)
from oversea.mechanics.factions.schemas.value_objects.base_resources import (
    BaseResources,
)
from oversea.mechanics.factions.schemas.value_objects.building import Building
from oversea.mechanics.factions.schemas.value_objects.colony_data import ColonyData
from oversea.mechanics.factions.schemas.entities.fleet import Fleet
from oversea.mechanics.factions.schemas.value_objects.income import Income
from oversea.mechanics.factions.schemas.entities.ship import Ship
from oversea.mechanics.factions.schemas.value_objects.ship_data import ShipData

SIM_DIRECTORY = "sim"


class Inputs(str, enum.Enum):
    base_income = "base_income.json"
    buildings = "buildings.json"
    colony = "colony.json"
    ships = "ships.json"
    starting_resources = "starting_resources.json"
    starting_fleet = "starting_fleet.json"
    actions = "actions.json"


def load_ships(sim_path: str) -> list[ShipData]:
    with open(os.path.join(sim_path, Inputs.ships), "r") as f:
        obj: dict = json.load(f)

    ships = []
    for name, data in obj.items():
        some_ship = ShipData(name=name, **data)
        ships.append(some_ship)
    return ships


def load_buildings(sim_path: str) -> list[Building]:
    with open(os.path.join(sim_path, Inputs.buildings), "r") as f:
        obj: dict = json.load(f)

    buildings = []
    for name, data in obj.items():
        some_building = Building(name=name, **data)
        buildings.append(some_building)
    return buildings


def load_income(sim_path: str) -> BaseResources:
    with open(os.path.join(sim_path, Inputs.base_income), "r") as f:
        obj: dict = json.load(f)

    return Income(**obj)


def load_starting_resources(sim_path: str) -> BaseResources:
    with open(os.path.join(sim_path, Inputs.starting_resources), "r") as f:
        obj: dict = json.load(f)

    return BaseResources(**obj)


def load_fleet(sim_path: str, ship_data: list[ShipData]) -> Fleet:
    with open(os.path.join(sim_path, Inputs.starting_fleet), "r") as f:
        obj: list = json.load(f)

    ships = []
    for ship in obj:
        ships.append(spawn_ship(ship, ship_data))
    return Fleet(ships=ships)


def spawn_ship(name: str, ship_data: list[ShipData]) -> Ship:
    for ship in ship_data:
        if name == ship.name:
            return Ship(data=ship)

    raise ValueError(f"Ship {name} does not exist.")


def load_colony(sim_path: str) -> ColonyData:
    with open(os.path.join(sim_path, Inputs.colony), "r") as f:
        obj: dict = json.load(f)

    return ColonyData(**obj)


def load_actions(
    sim_path: str,
    ships: list[ShipData],
    buildings: list[Building],
    colony: ColonyData,
) -> list[list[Action]]:
    with open(os.path.join(sim_path, Inputs.actions), "r") as f:
        obj: dict = json.load(f)

    actions = []
    for day in obj:
        today_actions = []
        for action in day:
            if action["type"] == "building":
                target_building = find_in_config(action["name"], buildings)
                today_actions.append(CreateBuilding(target=target_building))
            if action["type"] == "ship":
                target_ship = find_in_config(action["name"], ships)
                today_actions.append(CreateShip(target=target_ship))
            if action["type"] == "colony":
                today_actions.append(CreateColony(target=colony))
        actions.append(today_actions)

    return actions


T = TypeVar("T")


def find_in_config(name: str, some_sequence: list[T]) -> T:
    for el in some_sequence:
        if name.lower() == el.name.lower():
            return el

    raise ValueError(f"{name} not found in {some_sequence}")


def load_simulation(name: str, dir: str):
    sim_path = os.path.join(dir, SIM_DIRECTORY, name, "inputs")

    starting_resources = load_starting_resources(sim_path)
    ships = load_ships(sim_path)
    income = load_income(sim_path)
    colony = load_colony(sim_path)
    buildings = load_buildings(sim_path)
    fleet = load_fleet(sim_path, ships)
    actions = load_actions(sim_path, ships, buildings, colony)

    return starting_resources, ships, income, fleet, colony, buildings, actions
