from oversea.mechanics.fractions.schemas.cost import Cost
from oversea.mechanics.fractions.schemas.technology import Technology

arhant_magic_technologies = [
    Technology(
        name="Lower Magic Arcanas",
        cost=Cost(geist=1),
        effect="Once a turn selected unit gets until the end of the turn: a) +2 speed or b) +1 "
        "fire power and resilience",
    ),
    Technology(
        name="Higher Magic Arcanas",
        cost=Cost(geist=2),
        effect="Once a you can draw a Goal Card. If you have one already, discard it before "
        "drawing.",
    ),
    Technology(
        name="Superior Magic Arcanas",
        cost=Cost(geist=3),
        effect="You gain extra turn after current one. You may use this power once a round, "
        "each time paying its initial cost.",
    ),
]
