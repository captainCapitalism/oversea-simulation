from oversea.mechanics.factions.schemas.building import Building
from oversea.mechanics.factions.schemas.cost import Cost
from oversea.mechanics.factions.schemas.income import Income, Reward

eternal_forges = Building(
    name="Eternal Forges",
    cost=Cost(cash=4),
    effects=[Income(cash=2)],
)
underground_mines = Building(
    name="Underground Mines",
    cost=Cost(cash=6),
    effects=[Income(cash=3)],
    requirement=eternal_forges,
)

ash_oracle = Building(
    name="Ash Oracle",
    cost=Cost(cash=3),
    effects=[Income(geist=1)],
)

silent_council = Building(
    name="Silent Council",
    cost=Cost(cash=4),
    effects=[Income(intrigue_cards=1)],
)

brotherhood_of_dream = Building(
    name="Brotherhood of Dream",
    cost=Cost(cash=3),
    effects=[
        "Access to Magic Arcanas.",
        Income(magic_cards=1),
    ],
    rewards=[Reward(magic_cards=1)],
)

brotherhood_of_idea = Building(
    name="Brotherhood of Idea",
    cost=Cost(cash=3),
    effects=["Gain access to technologies."],
)
war_shipyard = Building(
    name="War Shipyard",
    cost=Cost(cash=4),
    effects=["Access to all faction ships."],
)
colony_war_shipyards = Building(
    name="Colony War Shipyards",
    cost=Cost(cash=5),
    effects=["Colonies can build all faction ships."],
    requirement=war_shipyard,
)
toothed_stronghold = Building(
    name="Toothed Stronghold",
    cost=Cost(cash=4),
    effects=["Capitol gains defenses"],
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
