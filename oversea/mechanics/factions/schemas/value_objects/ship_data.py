import enum
from typing import Set, Optional

from pydantic import BaseModel, Field

from oversea.mechanics.factions.schemas.value_objects.cost import Cost


class Traits(str, enum.Enum):
    rowing = "wiosłowy"
    stronghold = "twierdza"
    artillery = "artyleryjski"
    agile = "zwrotny"
    deep = "głębokie-zanurzenie"


class Stats(BaseModel):
    speed: int = Field(..., ge=0)
    range: int = Field(..., ge=0)
    fire_power: int = Field(..., ge=0)
    resilience: int = Field(..., ge=0)
    hit_points: int = Field(..., ge=0)


class ShipData(BaseModel):
    name: str
    stats: Optional[Stats]
    cost: Cost
    traits: Set[Traits] = set()
    advanced: bool = False
    tier: int = Field(..., ge=0, le=3)
