"""Statistical analysis utilities.

Functions to compute descriptive statistics, correlations, and simple trends by
branch, and to persist the analysis as a JSON report under `src/report/`.
"""

import json
import os
from datetime import datetime

import pandas as pd
from scipy.stats import linregress, pearsonr


def analyze_dataset(merged_df: pd.DataFrame) -> None:
    """Perform statistical analysis and save a JSON report.

    Computes global means, Pearson correlation, per-branch statistics, and
    simple trend detection of dropout rates. The resulting analysis is saved as
    a JSON file at `src/report/analisi_estadistic.json`.

    Args:
        merged_df: Merged dataset containing performance and dropout metrics.

    Returns:
        None. Writes a JSON report to disk and prints its path.
    """
    abandon_col = "Abandonament mitjà (%)"
    perf_col = "Rendiment mitjà (%)"

    # Metadata section
    metadata = {
        "fecha_analisis": datetime.now().strftime("%Y-%m-%d"),
        "num_registros": len(merged_df),
        "periodo_temporal": sorted(merged_df["Curs Acadèmic"].unique()),
    }

    # Global statistics section
    abandono_medio = merged_df[abandon_col].mean()
    rendimiento_medio = merged_df[perf_col].mean()
    corr = pearsonr(merged_df[abandon_col].dropna(), merged_df[perf_col].dropna())[0]
    global_stats = {
        "abandono_medio": abandono_medio,
        "rendimiento_medio": rendimiento_medio,
        "correlacion_abandono_rendimiento": corr,
    }

    # Analysis by branch section
    branch_stats = {}
    for branch in merged_df["Branca"].unique():
        branch_data = merged_df[merged_df["Branca"] == branch]
        abandon_mean = branch_data[abandon_col].mean()
        abandon_std = branch_data[abandon_col].std()
        perf_mean = branch_data[perf_col].mean()
        perf_std = branch_data[perf_col].std()
        branch_by_year = (
            branch_data.groupby("Curs Acadèmic")
            .agg({abandon_col: "mean"})
            .reset_index()
        )
        years = branch_by_year["Curs Acadèmic"].tolist()
        valores_abandono = branch_by_year[abandon_col].tolist()
        slope = linregress(range(len(years)), valores_abandono).slope
        if slope > 0.01:
            tendencia = "increasing"
        elif slope < -0.01:
            tendencia = "decreasing"
        else:
            tendencia = "stable"
        branch_stats[branch] = {
            "abandono": {"mean": abandon_mean, "std": abandon_std},
            "rendimiento": {"mean": perf_mean, "std": perf_std},
            "tendencia_abandono": tendencia,
        }

    # Rankings section
    branch_means = merged_df.groupby("Branca").agg(
        {perf_col: "mean", abandon_col: "mean"}
    )
    best_perf = branch_means[perf_col].idxmax()
    worst_perf = branch_means[perf_col].idxmin()
    most_abandon = branch_means[abandon_col].idxmax()
    least_abandon = branch_means[abandon_col].idxmin()
    rankings = {
        "mejor_rendimiento": best_perf,
        "peor_rendimiento": worst_perf,
        "mayor_abandono": most_abandon,
        "menor_abandono": least_abandon,
    }

    # Create final JSON report
    report = {
        "analysis_metadata": metadata,
        "estadisticas_globales": global_stats,
        "analisis_por_rama": branch_stats,
        "rankings": rankings,
    }

    # Save report in src/report/
    src_dir = os.path.dirname(os.path.dirname(__file__))
    output_path = os.path.join(src_dir, "report", "analisi_estadistic.json")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
    print(f"Statistical analysis report saved to {output_path}")
