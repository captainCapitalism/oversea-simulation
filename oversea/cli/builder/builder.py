import typer

from oversea.cli.builder.handlers import load_simulation

DATA_DIRECTORY = "data"
builder = typer.Typer(
    name="builder", help="commands for interacting with simulation inputs."
)


@builder.command(help="Display inputs for given simulation.")
def display(
    name: str = typer.Argument(..., help="Simulation name."),
):
    [
        starting_resources,
        ships,
        income,
        fleet,
        colony,
        buildings,
        actions,
    ] = load_simulation(name, str(DATA_DIRECTORY))

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
    print("Fleet: ")
    for ship in fleet.ships:
        print(ship.dict(exclude_defaults=True))

    print()
    print("Buildings: ")
    for building in buildings:
        print(building.dict(exclude_defaults=True))

    print()
    print("Actions: ")
    for turn in actions:
        for action in turn:
            print(action.dict(exclude_defaults=True))
