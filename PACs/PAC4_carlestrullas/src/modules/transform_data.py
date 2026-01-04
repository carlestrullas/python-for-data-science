"""Data transformation and cleaning utilities.

Helpers to harmonize column names between datasets, drop unused fields, compute
grouped aggregates by branch and related dimensions, and merge the datasets.
"""

import pandas as pd


def harmonize_abandonment_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Harmonize abandonment dataset columns.

    Renames specific columns in the dropout dataset so they match the naming
    used by the performance dataset and downstream processing.

    Args:
        df: Abandonment dataset.

    Returns:
        A DataFrame with harmonized column names.
    """
    rename_dict = {
        "Naturalesa universitat responsable": "Tipus universitat",
        "Universitat responsable": "Universitat",
        "Sexe Alumne": "Sexe",
        "Tipus de centre": "Integrat S/N",
    }
    return df.rename(columns=rename_dict)


def drop_unnecessary_columns(df: pd.DataFrame, dataset: str) -> pd.DataFrame:
    """Drop unneeded columns for the specified dataset type.

    Args:
        df: Input DataFrame.
        dataset: Dataset type, e.g. ``"performance"`` to also drop credit
            columns.

    Returns:
        A DataFrame with unnecessary columns removed.
    """
    cols_to_drop = ["Universitat", "Unitat"]
    if dataset == "performance":
        cols_to_drop += ["Crèdits ordinaris superats", "Crèdits ordinaris matriculats"]
    return df.drop(
        columns=[c for c in cols_to_drop if c in df.columns], errors="ignore"
    )


def group_by_branch(df: pd.DataFrame, value_col: str, new_col: str) -> pd.DataFrame:
    """Compute per-branch averages over common grouping dimensions.

    Groups by academic year, university type, sigles, study type, branch,
    gender, integration flag, and averages ``value_col``.

    Args:
        df: Input DataFrame.
        value_col: Name of the column to average.
        new_col: Name of the averaged column in the result.

    Returns:
        A grouped DataFrame with averaged values and normalized column name.
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
    """Merge performance and abandonment datasets on shared dimensions.

    Args:
        df_perf: Performance dataset.
        df_aband: Abandonment dataset.

    Returns:
        A merged DataFrame containing only matching rows across datasets.
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
