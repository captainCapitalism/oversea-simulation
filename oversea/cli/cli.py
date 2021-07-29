import logging
import os
import shutil
from pathlib import Path

import typer

from oversea.cli.builder.builder import builder
from oversea.cli.builder.handlers import load_simulation
from oversea.cli.handlers import new_simulation_structure
from oversea.mechanics.city.sim.income import sim
from oversea.mechanics.factions.schemas.bank import Bank

app = typer.Typer()
app.add_typer(builder)
SIM_DIRECTORY = "sim"


@app.command(name="new")
def new(name: str, data_directory: Path = "data"):
    if not os.path.exists(data_directory):
        os.mkdir(data_directory)
    sim_path = os.path.join(data_directory, SIM_DIRECTORY)
    if not os.path.exists(sim_path):
        os.mkdir(sim_path)

    new_simulation_structure(name, Path(sim_path))


@app.command()
def delete(name: str, data_directory: Path = "data"):
    this_sim_directory = os.path.join(data_directory, SIM_DIRECTORY, name)
    shutil.rmtree(this_sim_directory)
    coloured_name = typer.style(name, fg=typer.colors.RED)
    typer.echo(f"Simulation {coloured_name} was removed.")


@app.command(name="list")
def list_simulations(data_directory: Path = "data"):
    sim_path = os.path.join(data_directory, SIM_DIRECTORY)

    simulations = os.listdir(sim_path)
    for simulation in simulations:
        typer.echo(simulation)


@app.command(name="run")
def run_simulation(name: str, data_directory: Path = "data"):
    logging.basicConfig(level=logging.DEBUG)
    [
        starting_resources,
        ships,
        income,
        fleet,
        colony,
        buildings,
    ] = load_simulation(name, str(data_directory))
    result = sim(
        bank=Bank() + starting_resources,
        income=income,
        actions=[],
        fleet=fleet,
        turns=10,
    )

    print(result)
