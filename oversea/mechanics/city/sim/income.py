import json
import logging

from oversea.mechanics.factions.arhant.faction import arhant
from oversea.mechanics.factions.schemas.bank import Bank
from oversea.mechanics.factions.schemas.income import Income


def sim(
    bank: Bank,
    income: Income,
    turns: int,
) -> Bank:
    for turn in range(turns):
        bank += income
        logging.log(
            logging.DEBUG,
            f"Turn {turn} ends with {json.dumps(bank.dict())}",
        )

    return bank


def base_arhant(turns: int) -> Bank:
    turn_0 = arhant.bank + arhant.base_resources

    income = Income(**arhant.base_income.dict())

    return sim(turn_0, income, turns)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    base_arhant(10)
