import json
import logging

from oversea.mechanics.city.sim.safe_get import safe_get
from oversea.mechanics.factions.arhant import buildings
from oversea.mechanics.factions.arhant.faction import arhant
from oversea.mechanics.factions.schemas.bank import Bank
from oversea.mechanics.factions.schemas.cost import Cost
from oversea.mechanics.factions.schemas.income import Income


def sim(
    bank: Bank,
    income: Income,
    costs: list[list[Cost]],
    effects: list[list[Income]],
    turns: int,
) -> Bank:
    for turn in range(turns):
        this_turn_costs = safe_get(costs, turn)
        for cost in this_turn_costs:
            bank -= cost
        this_turn_effects = safe_get(effects, turn)
        for effect in this_turn_effects:
            income = income + effect
        bank += income
        logging.log(logging.DEBUG, f"Turn {turn} income {json.dumps(income.dict())}")
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
    costs = [
        [buildings.eternal_forges.cost],
        [buildings.ash_oracle.cost],
    ]
    effects = [[Income(cash=2), Income(geist=1)]]
    return sim(
        bank=turn_0,
        income=income,
        costs=costs,
        effects=effects,
        turns=turns,
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    arhant_with_buildings(10)
