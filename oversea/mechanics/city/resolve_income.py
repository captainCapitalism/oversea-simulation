import operator

from oversea.mechanics.factions.schemas.bank import Bank
from oversea.mechanics.factions.schemas.income import Income


def resolve_income(
    bank: Bank,
    income: Income,
) -> Bank:
    return operator.add(
        bank,
        income,
    )
