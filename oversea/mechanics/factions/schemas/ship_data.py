import enum
from typing import List, Set

from pydantic import BaseModel, Field

from oversea.mechanics.factions.schemas.cost import Cost


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
    traits: Set[Traits]
    stats: Stats
    cost: Cost
    advanced: bool
