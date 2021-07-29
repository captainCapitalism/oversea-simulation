import os
from pathlib import Path

import typer


def new_simulation_structure(
    name: str,
    path: Path,
):
    input_dir = "inputs"
    output_dir = "outputs"
    target_path = os.path.join(path, name)

    coloured_name = typer.style(name, fg=typer.colors.RED)
    coloured_path = typer.style(str(path), fg=typer.colors.BLUE)
    if os.path.exists(target_path):
        typer.echo(f"Simulation {coloured_name} already exists.")
    else:
        os.mkdir(target_path)
        os.mkdir(os.path.join(target_path, input_dir))
        os.mkdir(os.path.join(target_path, output_dir))
        typer.echo(f"Simulation {coloured_name} created at {coloured_path}")
