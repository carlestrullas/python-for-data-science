"""Exploratory Data Analysis utilities for PAC4.

Simple helpers to quickly inspect a dataset by printing a preview, columns, and
info to standard output.
"""

import pandas as pd


def show_eda(df: pd.DataFrame) -> None:
    """Display a basic EDA for the given DataFrame.

    Prints the head, the list of columns, and the result of ``DataFrame.info``
    to standard output.

    Args:
        df: DataFrame to analyze.

    Returns:
        None. Information is printed to stdout.
    """
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nInfo:")
    df.info()
