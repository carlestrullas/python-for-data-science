"""
Data loading utilities for PAC4 - Student Performance in Catalonia
"""

import os
from typing import Optional

import pandas as pd


def load_dataset(filepath: Optional[str] = None) -> pd.DataFrame:
    """
    Load a dataset from the given file path or prompt the user to select one.
    Args:
        filepath (str, optional): Path to the dataset file. If None, prompt user.
    Returns:
        pd.DataFrame: Loaded dataset.
    """
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
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
