# PAC4 - Student Performance in Catalonia

This project analyzes the academic performance of university students in Catalonia using official datasets. The code is organized as a Python package with modular structure, documentation, and tests.


## Project Structure

- `LICENSE` : Project license (MIT)
- `src/` : Main source code package
    - `main.py` : Main script to run all analyses
    - `img/` : Generated or example images for reports/visualizations
    - `modules/` : All analysis modules
        - `eda.py` : Exploratory Data Analysis utilities
        - `load_data.py` : Functions for loading datasets
        - `statistical_analysis.py` : Statistical analysis functions
        - `transform_data.py` : Data cleaning, harmonization, grouping, merging
        - `visual_analysis.py` : Visualization functions
    - `report/` : Output reports (e.g., JSON analysis)
- `data/` : Input datasets (Excel, CSV, etc.)
- `tests/` : Unit tests
- `requirements.txt` : Python dependencies
- `Makefile` : Environment and install commands
- `setup.py` : Package installer (optional, for advanced usage)
- `doc/` : Sphinx documentation source and build outputs
- `screenshots/` : Required screenshots for reports or documentation
- `PAC4_enunciat.ipynb` : Project statement and instructions (Jupyter Notebook)
- `README.md` : Project overview and instructions

## Installation



Create the conda environment (requires both Make and Conda to be installed):

> **Note:** Make sure you have `Make` and `Miniconda` installed on your system before running the following command.

```sh
# Ejecuta el siguiente comando desde PAC4_carlestrullas/
make install
```

## Usage

First, activate the previously created environment:
```sh
conda activate python-for-data-science
```

Now, you can run all exercises or only up to a specific one using the `-ex` option:

- Run all exercises (default):
```sh
python -m src.main
```

- Run only up to exercise N (for example, up to exercise 2):
```sh
python -m src.main -ex 2
```

- Show help:
```sh
python -m src.main -h
```

**Note:** Execute the previous commands from `PAC4_carlestrullas/`.

## Usage as a package

TODO



## Documentation

All functions and modules in this project are documented with Google‑style docstrings. HTML documentation is generated with Sphinx under the `doc/` folder.

> **Note:** The generated documentation now includes all modules inside the `src/` folder, including `main.py`.

### Generate the documentation (step by step)

1. **Install dependencies and activate the environment** (first time only):
	```sh
	# Ejecuta el siguiente comando desde PAC4_carlestrullas/
	make install
	```
2. **Build HTML documentation** from the `PAC4_carlestrullas/`:
	```sh
	make docs
	```
3. **Open the documentation homepage** in your browser:
	- Path: `PAC4_carlestrullas/doc/_build/html/index.html`

## Testing

Run all unit tests with pytest:
```sh
pytest tests/
```

## Coverage

To check test coverage (if coverage is installed):
```sh
coverage run -m pytest
coverage report
```

## Linting and Code Style

All code follows the Python style guide (PEP8), except in cases where strict adherence would reduce code readability. The linter `pylint` is used to check code quality. Any justified exceptions to the style guide are configured in the `.pylintrc` file, aiming for scores above 9 in all scripts.

> **Note:** The warning `too-many-locals` has been disabled in `.pylintrc` to allow more local variables in some functions (e.g., in `statistical_analysis.py`), as this improves clarity for complex analysis steps.

To check code style, run:
```sh
pylint src/
```
