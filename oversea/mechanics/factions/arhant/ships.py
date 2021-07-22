from oversea.mechanics.factions.schemas.cost import Cost
from oversea.mechanics.factions.schemas.ship import Ship, Stats, Traits

galley = Ship(
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
)
black_boat = Ship(
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
)
silent_arc = Ship(
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
)

arhant_ships = [
    galley,
    black_boat,
    silent_arc,
]
