from pydantic import BaseModel

from oversea.mechanics.factions.schemas.ship import Ship


class Fleet(BaseModel):
    ships: list[Ship]

    def __add__(self, new_ship: Ship):
        new_fleet = self.ships + [new_ship]

        return Fleet(ships=new_fleet)
