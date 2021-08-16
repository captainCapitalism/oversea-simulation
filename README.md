# Getting started

### Creating environment
Required python: python3.9

### Linux:
```bash
python39 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Windows:
```bash
python39 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Using
Installation steps should create executable command `sim`, but only with released version, here 
it is required to run app with `python -m oversea`

```bash
python -m oversea
```
Should invoke help:
```bash
Usage: sim [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.

  --help                          Show this message and exit.

Commands:
  builder  commands for interacting with simulation inputs.
  delete   Delete given simulation.
  example  Generate example simulation data.
  list     Show available simulations.
  new      Create new simulation.
```

For generating test data:

`python -m oversea example`

Running an example:

`python -m oversea run example`

