from oversea.mechanics.factions.schemas.value_objects.base_resources import (
    BaseResources,
)


class Bank(BaseResources):
    def __add__(
        self,
        income: BaseResources,
    ) -> "Bank":
        return Bank(
            cash=self.cash + income.cash,
            geist=self.geist + income.geist,
            intrigue_cards=self.intrigue_cards + income.intrigue_cards,
            magic_cards=self.magic_cards + income.magic_cards,
            goal_cards=self.goal_cards + income.goal_cards,
        )

    def __sub__(self, cost: BaseResources):
        return Bank(
            cash=self.cash - cost.cash,
            geist=self.geist - cost.geist,
            intrigue_cards=self.intrigue_cards - cost.intrigue_cards,
            magic_cards=self.magic_cards - cost.magic_cards,
            goal_cards=self.goal_cards - cost.goal_cards,
        )
