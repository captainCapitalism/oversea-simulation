from oversea.mechanics.factions.schemas.bank import Bank
from oversea.mechanics.factions.schemas.income import Income


def test_adding_income_increases_bank_values():
    expected_resources = {
        "cash": 5,
        "geist": 8,
        "intrigue_cards": 2,
        "magic_cards": 2,
        "goal_cards": 3,
    }

    bank = Bank(
        cash=3,
        geist=7,
        intrigue_cards=1,
        magic_cards=1,
        goal_cards=2,
    )
    income = Income(
        cash=2,
        geist=1,
        intrigue_cards=1,
        magic_cards=1,
        goal_cards=1,
    )

    bank = bank + income

    assert bank.dict() == expected_resources
