import json
import logging

from oversea.mechanics.city.sim.safe_get import safe_get
from oversea.mechanics.factions.arhant import buildings
from oversea.mechanics.factions.arhant.faction import arhant
from oversea.mechanics.factions.schemas.action import CreateBuilding, Action
from oversea.mechanics.factions.schemas.bank import Bank
from oversea.mechanics.factions.schemas.income import Income


def sim(
    bank: Bank,
    income: Income,
    actions: list[list[Action]],
    turns: int,
) -> Bank:
    for turn in range(turns):
        this_turn_actions = safe_get(actions, turn)
        for action in this_turn_actions:
            if isinstance(action, CreateBuilding):
                bank -= action.target.cost
                income += action.target.effect

        bank += income
        logging.log(
            logging.DEBUG,
            f"Turn {turn} income {json.dumps(income.dict())}",
        )
        logging.log(
            logging.DEBUG,
            f"Turn {turn} ends with {json.dumps(bank.dict())}",
        )

    return bank


def base_arhant(turns: int) -> Bank:
    turn_0 = arhant.bank + arhant.base_resources

    income = Income(**arhant.base_income.dict())

    return sim(
        bank=turn_0,
        income=income,
        costs=[],
        turns=turns,
    )


def arhant_with_buildings(turns: int) -> Bank:
    turn_0 = arhant.bank + arhant.base_resources

    income = Income(**arhant.base_income.dict())
    actions = [
        [CreateBuilding(target=buildings.eternal_forges)],
        [CreateBuilding(target=buildings.ash_oracle)],
    ]
    return sim(
        bank=turn_0,
        income=income,
        actions=actions,
        turns=turns,
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    arhant_with_buildings(10)
