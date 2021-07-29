import logging
import os
import shutil
from pathlib import Path

import typer

from oversea.cli.builder.builder import builder
from oversea.cli.builder.handlers import load_simulation
from oversea.cli.handlers import (
    new_simulation_structure,
    copy_simulation,
    dump_simulation,
)
from oversea.mechanics.city.sim.income import sim
from oversea.mechanics.factions.schemas.bank import Bank

app = typer.Typer()
app.add_typer(builder)
SIM_DIRECTORY = "sim"


@app.command(name="new")
def new(
    name: str = typer.Argument(..., help="Simulation name."),
    base: str = typer.Option(None, help="Simulation name to copy data from."),
    data_directory: Path = typer.Option(
        "data", help="Directory in which data is stored."
    ),
):
    if not os.path.exists(data_directory):
        os.mkdir(data_directory)
    sim_path = os.path.join(data_directory, SIM_DIRECTORY)

    if not os.path.exists(sim_path):
        os.mkdir(sim_path)
    if base is None:
        new_simulation_structure(name, Path(sim_path))
    else:
        copy_simulation(name, base, Path(sim_path))


@app.command()
def example(
    data_directory: Path = typer.Option(
        "data", help="Directory in which data is stored."
    ),
):
    example_name = "sim_example"
    path_to_example = os.path.join(os.path.dirname(__file__), example_name)
    target_path = os.path.join(data_directory, "sim", example_name)
    shutil.copytree(path_to_example, target_path)

    outputs_path = os.path.join(target_path, "outputs")
    if not os.path.exists(outputs_path):
        os.mkdir(outputs_path)

    typer.echo(
        f"{typer.style(example_name, fg=typer.colors.BLUE)} created at "
        f"{typer.style(target_path, fg=typer.colors.RED)}"
    )


@app.command()
def delete(
    name: str = typer.Argument(..., help="Simulation name."),
    data_directory: Path = typer.Option(
        "data", help="Directory in which data is stored."
    ),
):
    this_sim_directory = os.path.join(data_directory, SIM_DIRECTORY, name)
    shutil.rmtree(this_sim_directory)
    coloured_name = typer.style(name, fg=typer.colors.RED)
    typer.echo(f"Simulation {coloured_name} was removed.")


@app.command(name="list")
def list_simulations(
    data_directory: Path = typer.Option(
        "data", help="Directory in which data is stored."
    ),
):
    sim_path = os.path.join(data_directory, SIM_DIRECTORY)

    simulations = os.listdir(sim_path)
    for simulation in simulations:
        typer.echo(simulation)


@app.command(name="run")
def run_simulation(
    name: str = typer.Argument(..., help="Simulation name."),
    data_directory: Path = typer.Option(
        "data", help="Directory in which data is stored."
    ),
):
    logging.basicConfig(level=logging.DEBUG)
    [
        starting_resources,
        ships,
        income,
        fleet,
        colony,
        buildings,
        actions,
    ] = load_simulation(name, str(data_directory))

    report = sim(
        bank=Bank() + starting_resources,
        income=income,
        actions=actions,
        fleet=fleet,
        turns=10,
    )

    dump_simulation(name, data_directory, report)
