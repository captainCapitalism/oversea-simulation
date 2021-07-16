from oversea.mechanics.fractions.schemas.cost import Cost
from oversea.mechanics.fractions.schemas.technology import Technology


innovative_boatbuilding = Technology(
    name="Innovating Boatbuilding",
    cost=Cost(cash=5, geist=1),
    effect="Ships gain +1 hit point",
)
armor = Technology(
    name="Armor",
    cost=Cost(cash=4, geist=1),
    effect="Ships gain +1 hit point",
)
new_projectiles = Technology(
    name="New Projectiles",
    cost=Cost(cash=4, geist=1),
    effect="All units gain +1 range and fire power",
)
defensive_architecture = Technology(
    name="Defensive Architecture",
    cost=Cost(cash=2, geist=1),
    effect="Fortifications gain +1 resilience and hit points",
)
new_sails = Technology(
    name="New Sails",
    cost=Cost(cash=3, geist=1),
    effect="Ships gain +1 speed",
)
sailwings = Technology(
    name="Sailwings",
    cost=Cost(cash=4, geist=2),
    effect="Agile ships can move above the land. Movement must end on the sea. Agile ships cannot be boarded. Silence negates the effects",
    requirement=new_sails,
)
army_reformation = Technology(
    name="Army Reformation",
    cost=Cost(cash=2, geist=1),
    effect="All ships gain +1 action",
)
storm_troopers = Technology(
    name="Storm Troopers",
    cost=Cost(cash=2, geist=1),
    effect="Gain +1 combat factor",
    requirement=army_reformation,
)
powder_artillery = Technology(
    name="Powder Artillery",
    cost=Cost(cash=5, geist=1),
    effect="Artillery ships shoot twice when at least half distance to target is perpendicular.",
)
long_cannons = Technology(
    name="Long Cannons",
    cost=Cost(cash=2, geist=1),
    effect="Artillery ships gain +1 range",
    requirement=powder_artillery,
)
war_engineering = Technology(
    name="War Engineering",
    cost=Cost(cash=1, geist=1),
    effect="Shipyards can build two ships at once.",
)
scientific_research = Technology(
    name="Scientific Research",
    cost=Cost(cash=3, geist=1),
    effect="+1 geist a turn.",
)
effective_economy = Technology(
    name="Effective Economy",
    cost=Cost(cash=3, geist=1),
    effect="+3 cash a turn.",
)


arhant_technologies = [
    innovative_boatbuilding,
    armor,
    new_projectiles,
    defensive_architecture,
    new_sails,
    sailwings,
    army_reformation,
    storm_troopers,
    powder_artillery,
    long_cannons,
    war_engineering,
    scientific_research,
    effective_economy,
]
