from pydantic import BaseModel

from oversea.mechanics.factions.schemas.ship_data import ShipData


class Ship(BaseModel):
    data: ShipData
    damage: int = 0

    @property
    def current_health(self) -> int:
        return self.data.stats.hit_points - self.damage

    def get_hit(self):
        self.damage += 1
