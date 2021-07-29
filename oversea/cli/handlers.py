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
    if os.path.exists(target_path):
        typer.echo(f"Simulation {name} already exists.")
    else:
        os.mkdir(target_path)
        os.mkdir(os.path.join(target_path, input_dir))
        os.mkdir(os.path.join(target_path, output_dir))
        typer.echo(f"Simulation {name} created at {path}")
