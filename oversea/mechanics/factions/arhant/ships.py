from oversea.mechanics.factions.schemas.cost import Cost
from oversea.mechanics.factions.schemas.ship_data import ShipData, Stats, Traits

galley = ShipData(
    name="Galley",
    traits={Traits.rowing},
    stats=Stats(
        speed=4,
        range=3,
        fire_power=2,
        resilience=2,
        hit_points=2,
    ),
    cost=Cost(cash=2),
    advanced=False,
    tier=1,
)
black_boat = ShipData(
    name="Black Boat",
    traits={Traits.agile, Traits.artillery},
    stats=Stats(
        speed=5,
        range=4,
        fire_power=2,
        resilience=2,
        hit_points=3,
    ),
    cost=Cost(cash=4),
    advanced=False,
    tier=2,
)
silent_arc = ShipData(
    name="Silent Arc",
    traits={Traits.stronghold, Traits.artillery, Traits.deep},
    stats=Stats(
        speed=4,
        range=4,
        fire_power=3,
        resilience=3,
        hit_points=4,
    ),
    cost=Cost(cash=7),
    advanced=True,
    tier=3,
)

arhant_ships = [
    galley,
    black_boat,
    silent_arc,
]
