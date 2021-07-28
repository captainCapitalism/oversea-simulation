from oversea.mechanics.factions.schemas.base_resources import BaseResources
from oversea.mechanics.factions.schemas.income import Income


class Bank(BaseResources):
    pass

    def __add__(
        self,
        income: Income,
    ) -> "Bank":
        self.cash += income.cash
        self.geist += income.geist
        self.intrigue_cards += income.intrigue_cards
        self.magic_cards += income.magic_cards
        self.goal_cards += income.goal_cards
        return self
