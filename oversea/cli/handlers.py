import os
import shutil
from pathlib import Path

import typer


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
