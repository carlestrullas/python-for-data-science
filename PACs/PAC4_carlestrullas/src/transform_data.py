"""
Data transformation and cleaning utilities.
"""

import pandas as pd


def harmonize_abandonment_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename columns in the abandonment dataset to match the performance dataset.

    Args:
        df (pd.DataFrame): Abandonment dataset.

    Returns:
        pd.DataFrame: DataFrame with harmonized column names.
    """
    rename_dict = {
        "Naturalesa universitat responsable": "Tipus universitat",
        "Universitat responsable": "Universitat",
        "Sexe Alumne": "Sexe",
        "Tipus de centre": "Integrat S/N",
    }
    return df.rename(columns=rename_dict)


def drop_unnecessary_columns(df: pd.DataFrame, dataset: str) -> pd.DataFrame:
    """
    Drop columns not needed for analysis.

    Args:
        df (pd.DataFrame): Input DataFrame.
        dataset (str): Dataset type ('performance' or other).

    Returns:
        pd.DataFrame: DataFrame with unnecessary columns dropped.
    """
    cols_to_drop = ["Universitat", "Unitat"]
    if dataset == "performance":
        cols_to_drop += ["Crèdits ordinaris superats", "Crèdits ordinaris matriculats"]
    return df.drop(
        columns=[c for c in cols_to_drop if c in df.columns], errors="ignore"
    )


def group_by_branch(df: pd.DataFrame, value_col: str, new_col: str) -> pd.DataFrame:
    """
    Group by academic year, university type, sigles, study type, branch, gender,
    integrated, and average the value_col.

    Args:
        df (pd.DataFrame): Input DataFrame.
        value_col (str): Name of the column to average.
        new_col (str): Name for the averaged column in the result.

    Returns:
        pd.DataFrame: Grouped DataFrame with averaged values.
    """
    group_cols = [
        "Curs Acadèmic",
        "Tipus universitat",
        "Sigles",
        "Tipus Estudi",
        "Branca",
        "Sexe",
        "Integrat S/N",
    ]
    grouped = df.groupby(group_cols, dropna=False)[value_col].mean().reset_index()
    grouped = grouped.rename(columns={value_col: new_col})
    return grouped


def merge_datasets(df_perf: pd.DataFrame, df_aband: pd.DataFrame) -> pd.DataFrame:
    """
    Merge the two datasets on the common columns, keeping only matching rows.

    Args:
        df_perf (pd.DataFrame): Performance dataset.
        df_aband (pd.DataFrame): Abandonment dataset.

    Returns:
        pd.DataFrame: Merged DataFrame containing only matching rows.
    """
    merge_cols = [
        "Curs Acadèmic",
        "Tipus universitat",
        "Sigles",
        "Tipus Estudi",
        "Branca",
        "Sexe",
        "Integrat S/N",
    ]
    merged = pd.merge(df_perf, df_aband, on=merge_cols, how="inner")
    return merged
