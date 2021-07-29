from oversea.mechanics.factions.arhant import ships
from oversea.mechanics.factions.schemas.fleet import Fleet
from oversea.mechanics.factions.schemas.ship import Ship

starting_fleet = Fleet(
    ships=[
        Ship(data=ships.galley),
        Ship(data=ships.black_boat),
    ],
)