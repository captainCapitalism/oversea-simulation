import os
import shutil
from pathlib import Path

import pandas
import typer
from pydantic import BaseModel

from oversea.mechanics.city.sim.income import Report
from oversea.mechanics.factions.schemas.entities.fleet import Fleet

SIM_DIRECTORY = "sim"


def new_simulation_structure(
    name: str,
    path: Path,
):
    input_dir = "inputs"
    output_dir = "outputs"
    target_path = os.path.join(path, name)

    coloured_name = typer.style(name, fg=typer.colors.BLUE)
    coloured_path = typer.style(str(path), fg=typer.colors.RED)
    if os.path.exists(target_path):
        typer.echo(f"Simulation {coloured_name} already exists.")
    else:
        os.mkdir(target_path)
        os.mkdir(os.path.join(target_path, input_dir))
        os.mkdir(os.path.join(target_path, output_dir))
        typer.echo(f"Simulation {coloured_name} created at {coloured_path}")


def copy_simulation(
    name: str,
    base: str,
    path: Path,
):
    base_path = os.path.join(path, base)
    target_path = os.path.join(path, name)
    coloured_name = typer.style(name, fg=typer.colors.BLUE)
    coloured_base = typer.style(base, fg=typer.colors.RED)
    coloured_path = typer.style(target_path, fg=typer.colors.RED)
    try:
        shutil.copytree(base_path, target_path)
        typer.echo(f"Created {coloured_name} from {coloured_base} at {coloured_path}")
    except FileNotFoundError:
        typer.echo(
            f"{coloured_base} simulation does not exist. Could not create {coloured_name}"
        )


report_paths = {
    "banks": "banks.csv",
    "incomes": "incomes.csv",
    "fleets": "fleets.csv",
    "costs": "costs.csv",
}


class FleetDescription(BaseModel):
    value: int = 0
    number_of_ships: int = 0
    tier_1: int = 0
    tier_2: int = 0
    tier_3: int = 0


def serialize_fleet(fleet: Fleet) -> FleetDescription:
    description = FleetDescription()
    for ship in fleet.ships:
        description.value += ship.data.cost.cash
        description.number_of_ships += 1
        tier = ship.data.tier
        if tier == 1:
            description.tier_1 += 1
        if tier == 2:
            description.tier_2 += 1
        if tier == 3:
            description.tier_3 += 1

    return description


def dump_simulation(
    name: str,
    path: Path,
    report: Report,
):
    for key, target_file in report_paths.items():
        output_path = os.path.join(path, SIM_DIRECTORY, name, "outputs", target_file)

        if key == "fleets":
            objects = pandas.DataFrame(
                serialize_fleet(fleet).dict() for fleet in getattr(report, key)
            )
        else:
            objects = pandas.DataFrame(obj.dict() for obj in getattr(report, key))
        with open(output_path, "w") as f:
            objects.to_csv(
                f,
                sep=",",
                index=False,
            )
