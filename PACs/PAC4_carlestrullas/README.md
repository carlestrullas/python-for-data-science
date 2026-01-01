
# PAC4 - Student Performance in Catalonia

This project analyzes the academic performance of university students in Catalonia using official datasets. The code is organized as a Python package with modular structure, documentation, and tests.

## Project Structure

- `src/` : Source code modules
	- `load_data.py` : Functions for loading datasets
	- `transform_data.py` : Data cleaning, harmonization, grouping, merging
	- `eda.py` : Exploratory Data Analysis utilities
	- `visual_analysis.py` : Visualization functions
	- `statistical_analysis.py` : Statistical analysis functions
- `main.py` : Entry point to run all analyses
- `tests/` : Unit tests
- `requirements.txt` : Python dependencies
- `Makefile` : Environment and install commands
- `setup.py` : Package installer (optional, for advanced usage)

## Installation

Create the conda environment environment:
```sh
# Execute the following command from PAC4_carlestrullas/
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
python main.py
```

- Run only up to exercise N (for example, up to exercise 2):
```sh
python main.py -ex 2
```

- Show help:
```sh
python main.py -h
```

**Note:** Execute the previous commands from `PAC4_carlestrullas/`.

## Usage as a package

TODO

## Documentation

All functions and modules are documented with Python docstrings. To generate HTML documentation (if using Sphinx or similar):
```sh
# Example (if Sphinx is set up):
make html
```

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

## Style Checks

To check code style (if flake8 or similar is installed):
```sh
flake8 src/
```

---
For any questions, refer to the code docstrings or contact the author.
