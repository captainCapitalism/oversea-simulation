import json
import logging
from typing import Tuple

from oversea.mechanics.city.sim.safe_get import safe_get
from oversea.mechanics.factions.arhant import buildings, colony_data, ships
from oversea.mechanics.factions.arhant.faction import arhant
from oversea.mechanics.factions.schemas.action import (
    CreateBuilding,
    Action,
    CreateColony,
    IncreaseIncome,
    CreateShip,
    DispatchShip,
)
from oversea.mechanics.factions.schemas.bank import Bank
from oversea.mechanics.factions.schemas.cost import Cost
from oversea.mechanics.factions.schemas.fleet import Fleet
from oversea.mechanics.factions.schemas.income import Income, Reward
from oversea.mechanics.factions.schemas.ship import Ship


def handle_colony(
    action: CreateColony,
    bank: Bank,
    colony_count: int,
) -> Tuple[Bank, IncreaseIncome]:
    bank -= Cost(
        **action.target.cost.dict(exclude={"cash"}),
        cash=action.target.cost.cash + colony_count,
    )
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


def handle_ship(
    action: CreateShip,
    bank: Bank,
) -> Tuple[Bank, DispatchShip]:
    bank -= action.target.cost
    new_action = DispatchShip(ship=Ship(data=action.target))
    return bank, new_action


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
    fleet: Fleet,
    turns: int,
) -> Bank:
    colony_count = 0

    for turn in range(turns):
        this_turn_actions = safe_get(actions, turn)
        for action in this_turn_actions:
            if isinstance(action, CreateBuilding):
                bank, income = handle_building(action, bank, income)
            elif isinstance(action, CreateColony):
                bank, new_action = handle_colony(action, bank, colony_count)
                colony_count += 1
                add_action(new_action, actions, turn=turn + 1)
            elif isinstance(action, CreateShip):
                bank, new_action = handle_ship(action, bank)
                add_action(new_action, actions, turn=turn + 1)

            elif isinstance(action, IncreaseIncome):
                income += action.income

            elif isinstance(action, DispatchShip):
                fleet += action.ship

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
    fleet = arhant.fleet

    actions = [
        [CreateBuilding(target=buildings.eternal_forges)],
        [CreateBuilding(target=buildings.ash_oracle)],
        [CreateBuilding(target=buildings.silent_council)],
        [CreateBuilding(target=buildings.brotherhood_of_dream)],
        [CreateColony(target=colony_data.colony_data)],
        [CreateColony(target=colony_data.colony_data)],
        [CreateShip(target=ships.galley)],
    ]
    return sim(
        bank=turn_0,
        income=income,
        actions=actions,
        fleet=fleet,
        turns=turns,
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    arhant_with_buildings(10)
