import json
import logging

from oversea.mechanics.factions.arhant.faction import arhant
from oversea.mechanics.factions.schemas.bank import Bank
from oversea.mechanics.factions.schemas.cost import Cost
from oversea.mechanics.factions.schemas.income import Income


def sim(
    bank: Bank,
    income: Income,
    costs: list[list[Cost]],
    turns: int,
) -> Bank:
    for turn in range(turns):
        bank += income
        logging.log(
            logging.DEBUG,
            f"Turn {turn} ends with {json.dumps(bank.dict())}",
        )

    return bank


def get_costs(costs: list[list[Cost]], turn: int):
    try:
        return costs[turn]
    except IndexError:
        return []


def base_arhant(turns: int) -> Bank:
    turn_0 = arhant.bank + arhant.base_resources

    income = Income(**arhant.base_income.dict())

    return sim(
        bank=turn_0,
        income=income,
        costs=[],
        turns=turns,
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    base_arhant(10)
