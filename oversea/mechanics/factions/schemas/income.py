from oversea.mechanics.factions.schemas.base_resources import BaseResources


class Income(BaseResources):
    def __add__(
        self,
        other: "Income",
    ) -> "Income":
        this_dict = self.dict()
        other_dict = other.dict()

        increased_values = {
            key: value + other_dict[key] for key, value in this_dict.items()
        }

        return Income(**increased_values)
