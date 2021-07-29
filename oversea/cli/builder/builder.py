from pathlib import Path

import typer

from oversea.cli.builder.handlers import load_simulation

builder = typer.Typer()


@builder.command()
def display(name: str, data_directory: Path = "data"):
    [
        starting_resources,
        ships,
        income,
        colony,
        buildings,
    ] = load_simulation(name, str(data_directory))

    print()
    print("Starting Resources: ")
    print(starting_resources.dict(exclude_defaults=True))

    print()
    print("Income: ")
    print(income.dict(exclude_defaults=True))

    print()
    print("Colony: ")
    print(colony.dict(exclude_defaults=True))

    print()
    print("Ships: ")
    for ship in ships:
        print(ship.dict(exclude_defaults=True))

    print()
    print("Buildings: ")
    for building in buildings:
        print(building.dict(exclude_defaults=True))
