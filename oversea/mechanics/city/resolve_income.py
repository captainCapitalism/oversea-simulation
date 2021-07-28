import operator

from oversea.mechanics.factions.schemas.bank import Bank
from oversea.mechanics.factions.schemas.base_resources import BaseResources


def resolve_income(
    bank: Bank,
    income: BaseResources,
) -> Bank:
    return operator.add(
        bank,
        income,
    )
