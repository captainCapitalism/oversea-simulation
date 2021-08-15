import operator

from oversea.mechanics.factions.schemas.value_objects.bank import Bank
from oversea.mechanics.factions.schemas.value_objects.base_resources import (
    BaseResources,
)


def resolve_income(
    bank: Bank,
    income: BaseResources,
) -> Bank:
    return operator.add(
        bank,
        income,
    )
