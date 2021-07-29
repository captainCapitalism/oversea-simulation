import json
import logging
from typing import Tuple

from oversea.mechanics.city.sim.safe_get import safe_get
from oversea.mechanics.factions.arhant import buildings, colony_data
from oversea.mechanics.factions.arhant.faction import arhant
from oversea.mechanics.factions.schemas.action import (
    CreateBuilding,
    Action,
    CreateColony,
    IncreaseIncome,
)
from oversea.mechanics.factions.schemas.bank import Bank
from oversea.mechanics.factions.schemas.income import Income, Reward


def handle_colony(
    action: CreateColony,
    bank: Bank,
) -> Tuple[Bank, IncreaseIncome]:
    bank -= action.target.cost

    new_event = IncreaseIncome(income=action.target.effect)

    return bank, new_event


def handle_building(
    action: CreateBuilding,
    bank: Bank,
    income: Income,
) -> Tuple[Bank, Income]:
    bank -= action.target.cost
    for effect in action.target.effects:
        if isinstance(effect, Income):
            income += effect
    for reward in action.target.rewards:
        if isinstance(reward, Reward):
            bank += reward

    return bank, income


def add_action(
    action: Action,
    actions: list[list[Action]],
    turn: int,
) -> list[list[Action]]:
    new_actions = safe_get(actions, turn) + [action]
    try:
        actions[turn] = new_actions
    except IndexError:
        actions.append(new_actions)

    return actions


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
                bank, income = handle_building(action, bank, income)
            elif isinstance(action, CreateColony):
                bank, new_action = handle_colony(action, bank)
                add_action(new_action, actions, turn=turn + 1)
            elif isinstance(action, IncreaseIncome):
                income += action.income

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


def arhant_with_buildings(turns: int) -> Bank:
    turn_0 = arhant.bank + arhant.base_resources

    income = Income(**arhant.base_income.dict())
    actions = [
        [CreateBuilding(target=buildings.eternal_forges)],
        [CreateBuilding(target=buildings.ash_oracle)],
        [CreateBuilding(target=buildings.silent_council)],
        [CreateBuilding(target=buildings.brotherhood_of_dream)],
        [CreateColony(target=colony_data.colony_data)],
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
