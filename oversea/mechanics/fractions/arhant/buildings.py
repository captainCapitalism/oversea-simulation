from oversea.mechanics.fractions.schemas.building import Building
from oversea.mechanics.fractions.schemas.cost import Cost

eternal_forges = Building(
    name="Eternal Forges",
    cost=Cost(cash=4),
    effect="+2 cash a turn.",
)
underground_mines = Building(
    name="Underground Mines",
    cost=Cost(cash=6),
    effect="+3 cash a turn.",
    requirement=eternal_forges,
)

ash_oracle = Building(
    name="Ash Oracle",
    cost=Cost(cash=3),
    effect="+1 geist a turn.",
)

silent_council = Building(
    name="Silent Council",
    cost=Cost(cash=4),
    effect="+1 intrigue card a turn.",
)

brotherhood_of_dream = Building(
    name="Brotherhood of Dream",
    cost=Cost(cash=3),
    effect="Access to Magic Arcanas. Draw magic card. +1 magic card a turn.",
)

brotherhood_of_idea = Building(
    name="Brotherhood of Idea",
    cost=Cost(cash=3),
    effect="Gain access to technologies.",
)
war_shipyard = Building(
    name="War Shipyard",
    cost=Cost(cash=4),
    effect="Access to all fraction ships.",
)
colony_war_shipyards = Building(
    name="Colony War Shipyards",
    cost=Cost(cash=5),
    effect="Colonies can build all fraction ships.",
    requirement=war_shipyard,
)
toothed_stronghold = Building(
    name="Toothed Stronghold",
    cost=Cost(cash=4),
    effect="Capitol gains defenses",
)

arhant_buildings = [
    eternal_forges,
    underground_mines,
    ash_oracle,
    silent_council,
    brotherhood_of_dream,
    brotherhood_of_idea,
    war_shipyard,
    colony_war_shipyards,
    toothed_stronghold,
]
