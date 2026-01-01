"""
Exploratory Data Analysis utilities for PAC4
"""

import pandas as pd


def show_eda(df: pd.DataFrame):
    """
    Display basic EDA: head, columns, info.
    Args:
        df (pd.DataFrame): DataFrame to analyze.
    """
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nInfo:")
    df.info()
