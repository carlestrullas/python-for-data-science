"""Data loading utilities for PAC4 - Student Performance in Catalonia.

This module provides helpers to load the official PAC4 datasets either by
passing an explicit path or by interactively selecting one of the known files
bundled under the project `data/` folder.
"""

import os
from typing import Optional

import pandas as pd


def load_dataset(filepath: Optional[str] = None) -> pd.DataFrame:
    """Load a dataset from Excel.

    Loads one of the PAC4 datasets from an Excel file. If ``filepath`` is not
    provided, an interactive prompt lets you choose between the performance and
    dropout datasets located under the project `data/` directory.

    Args:
        filepath: Absolute or relative path to the Excel dataset. If ``None``,
            the user is prompted to select a known dataset.

    Returns:
        A pandas DataFrame with the loaded dataset.

    Raises:
        FileNotFoundError: If the resolved path does not exist.
        ValueError: If an invalid selection is made during the prompt.
        xlrd.XLRDError, openpyxl.utils.exceptions.InvalidFileException: If the
            Excel file is invalid or cannot be parsed by the engine.
    """
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    data_dir = os.path.join(project_root, "data")
    datasets = {
        "1": ("rendiment_estudiants.xlsx", "Performance rate dataset"),
        "2": ("taxa_abandonament.xlsx", "Dropout rate dataset"),
    }
    if filepath is None:
        print("Select a dataset to load:")
        for k, v in datasets.items():
            print(f"  {k}: {v[1]} ({v[0]})")
        choice = input("Enter 1 or 2: ").strip()
        while choice not in datasets:
            choice = input("Invalid option. Enter 1 or 2: ").strip()
        filepath = os.path.join(data_dir, datasets[choice][0])
    else:
        if not os.path.isabs(filepath):
            filepath = os.path.join(data_dir, filepath)
    print(f"Loading file: {filepath}")
    df = pd.read_excel(filepath)
    return df
