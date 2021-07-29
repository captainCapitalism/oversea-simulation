import json
import logging
from typing import Tuple

from pydantic import BaseModel

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
    spent: Bank,
) -> Tuple[Bank, IncreaseIncome, Bank]:
    colony_cost = Cost(
        **action.target.cost.dict(exclude={"cash"}),
        cash=action.target.cost.cash + colony_count,
    )
    bank -= colony_cost
    spent += colony_cost
    new_event = IncreaseIncome(income=action.target.effect)

    return bank, new_event, spent


def handle_building(
    action: CreateBuilding,
    bank: Bank,
    income: Income,
    spent: Bank,
) -> Tuple[Bank, Income, Bank]:
    bank -= action.target.cost
    spent += action.target.cost

    for effect in action.target.effects:
        if isinstance(effect, Income):
            income += effect
    for reward in action.target.rewards:
        if isinstance(reward, Reward):
            bank += reward
    return bank, income, spent


def handle_ship(
    action: CreateShip,
    bank: Bank,
    spent: Bank,
) -> Tuple[Bank, DispatchShip, Bank]:
    bank -= action.target.cost
    spent += action.target.cost
    new_action = DispatchShip(ship=Ship(data=action.target))
    return bank, new_action, spent


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


class Report(BaseModel):
    banks: list[Bank] = []
    incomes: list[Income] = []
    fleets: list[Fleet] = []
    costs: list[Bank] = []


def sim(
    bank: Bank,
    income: Income,
    actions: list[list[Action]],
    fleet: Fleet,
    turns: int,
) -> Report:
    colony_count = 0
    report = Report()

    for turn in range(turns):
        spent = Bank()
        this_turn_actions = safe_get(actions, turn)
        for action in this_turn_actions:
            if isinstance(action, CreateBuilding):
                bank, income, spent = handle_building(action, bank, income, spent)
            elif isinstance(action, CreateColony):
                bank, new_action, spent = handle_colony(
                    action, bank, colony_count, spent
                )
                colony_count += 1
                add_action(new_action, actions, turn=turn + 1)
            elif isinstance(action, CreateShip):
                bank, new_action, spent = handle_ship(action, bank, spent)
                add_action(new_action, actions, turn=turn + 1)

            elif isinstance(action, IncreaseIncome):
                income += action.income

            elif isinstance(action, DispatchShip):
                fleet += action.ship

        bank += income
        report.incomes.append(income)
        report.banks.append(bank)
        report.fleets.append(fleet)
        report.costs.append(spent)

        logging.log(
            logging.DEBUG,
            f"Turn {turn} income {json.dumps(income.dict())}",
        )
        logging.log(
            logging.DEBUG,
            f"Turn {turn} ends with {json.dumps(bank.dict())}",
        )

    return report


def arhant_with_buildings(
    turns: int,
) -> Report:
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
    simulation_report = arhant_with_buildings(10)

    print(simulation_report.banks)
    print(simulation_report.incomes)
    print(simulation_report.fleets)
    print(simulation_report.costs)
