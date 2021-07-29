import logging
import os
import shutil
from pathlib import Path

import typer

from oversea.cli.handlers import new_simulation_structure
from oversea.mechanics.city.sim.income import arhant_with_buildings

app = typer.Typer()

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


@app.command(name="run")
def run_simulation():
    logging.basicConfig(level=logging.DEBUG)

    res = arhant_with_buildings(10)
