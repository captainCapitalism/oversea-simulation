from oversea.mechanics.fractions.schemas.cost import Cost
from oversea.mechanics.fractions.schemas.technology import Technology

lower_magic_aranas = Technology(
    name="Lower Magic Arcanas",
    cost=Cost(geist=1),
    effect="Once a turn selected unit gets until the end of the turn: a) +2 speed or b) +1 "
    "fire power and resilience",
)
higher_magic_arcanas = Technology(
    name="Higher Magic Arcanas",
    cost=Cost(geist=2),
    effect="Once a you can draw a Goal Card. If you have one already, discard it before "
    "drawing.",
    requirement=lower_magic_aranas,
)
superior_magic_arcanas = (
    Technology(
        name="Superior Magic Arcanas",
        cost=Cost(geist=3),
        effect="You gain extra turn after current one. You may use this power once a round, "
        "each time paying its initial cost.",
        requirement=higher_magic_arcanas,
    ),
)
arhant_magic_technologies = [
    lower_magic_aranas,
    higher_magic_arcanas,
    superior_magic_arcanas,
]
