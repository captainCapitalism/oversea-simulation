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
from oversea.mechanics.factions.schemas.value_objects.bank import Bank

app = typer.Typer()
app.add_typer(builder)
SIM_DIRECTORY = "sim"
DATA_DIRECTORY = "data"


@app.command(
    name="new",
    help="Create new simulation. Use --base to copy inputs from existing one",
)
def new(
    name: str = typer.Argument(..., help="Simulation name."),
    base: str = typer.Option(None, help="Simulation name to copy data from."),
):
    if not os.path.exists(DATA_DIRECTORY):
        os.mkdir(DATA_DIRECTORY)
    sim_path = os.path.join(DATA_DIRECTORY, SIM_DIRECTORY)

    if not os.path.exists(sim_path):
        os.mkdir(sim_path)
    if base is None:
        new_simulation_structure(name, Path(sim_path))
    else:
        copy_simulation(name, base, Path(sim_path))


@app.command(help="Generate example simulation data.")
def example():
    example_name = "example"
    path_to_example = os.path.join(os.path.dirname(__file__), example_name)
    target_path = os.path.join(DATA_DIRECTORY, "sim", example_name)
    shutil.copytree(path_to_example, target_path)

    outputs_path = os.path.join(target_path, "outputs")
    if not os.path.exists(outputs_path):
        os.mkdir(outputs_path)

    typer.echo(
        f"{typer.style(example_name, fg=typer.colors.BLUE)} created at "
        f"{typer.style(target_path, fg=typer.colors.RED)}"
    )


@app.command(help="Delete given simulation.")
def delete(
    name: str = typer.Argument(..., help="Simulation name."),
):
    this_sim_directory = os.path.join(DATA_DIRECTORY, SIM_DIRECTORY, name)
    shutil.rmtree(this_sim_directory)
    coloured_name = typer.style(name, fg=typer.colors.RED)
    typer.echo(f"Simulation {coloured_name} was removed.")


@app.command(name="list", help="Show available simulations.")
def list_simulations():
    sim_path = os.path.join(DATA_DIRECTORY, SIM_DIRECTORY)

    simulations = os.listdir(sim_path)
    for simulation in simulations:
        typer.echo(simulation)


@app.command(name="run", help="Run given simulation.")
def run_simulation(
    name: str = typer.Argument(..., help="Simulation name."),
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
    ] = load_simulation(name, str(DATA_DIRECTORY))

    report = sim(
        bank=Bank() + starting_resources,
        income=income,
        actions=actions,
        fleet=fleet,
        turns=10,
    )

    dump_simulation(name, DATA_DIRECTORY, report)
