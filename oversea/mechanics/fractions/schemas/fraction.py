from typing import Tuple, List

from pydantic import BaseModel

from oversea.mechanics.fractions.schemas.base_resources import BaseResources
from oversea.mechanics.fractions.schemas.building import Building
from oversea.mechanics.fractions.schemas.cost import Cost
from oversea.mechanics.fractions.schemas.ship import Ship, Stats
from oversea.mechanics.fractions.schemas.technology import Technology


class Fraction(BaseModel):

    name: str
    combat_factor: int
    base_resources: BaseResources
    base_income: Cost
    main_goal: str
    perks: Tuple[str, str]
    buildings: List[Building]
    technologies: List[Technology]
    magic_technologies: List[Technology]
    ships: List[Ship]
    stronghold_stats: Stats
    colony_cost: Cost
    colony_income: Cost