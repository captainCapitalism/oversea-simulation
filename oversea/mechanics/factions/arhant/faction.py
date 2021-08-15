from oversea.mechanics.factions.arhant.buildings import arhant_buildings
from oversea.mechanics.factions.arhant.colony_data import colony_data
from oversea.mechanics.factions.arhant.ships import arhant_ships
from oversea.mechanics.factions.arhant.starting_fleet import starting_fleet
from oversea.mechanics.factions.schemas.value_objects.bank import Bank
from oversea.mechanics.factions.schemas.value_objects.base_resources import (
    BaseResources,
)
from oversea.mechanics.factions.schemas.faction import Faction
from oversea.mechanics.factions.schemas.value_objects.income import Income
from oversea.mechanics.factions.schemas.value_objects.ship_data import Stats

arhant = Faction(
    name="Arhant",
    base_resources=BaseResources(
        cash=4,
        geist=3,
        intrigue_cards=2,
    ),
    base_income=BaseResources(
        cash=2,
        geist=0,
    ),
    buildings=arhant_buildings,
    ships=arhant_ships,
    stronghold_stats=Stats(
        range=5,
        fire_power=3,
        resilience=4,
        hit_points=1,
        speed=0,
    ),
    colony_data=colony_data,
    income=Income(),
    bank=Bank(),
    fleet=starting_fleet,
)
