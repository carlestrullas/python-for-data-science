"""Visualization utilities.

Functions to generate time series plots of dropout and performance rates by
branch and save them as PNG files under `src/img/`.
"""

import os

import matplotlib.pyplot as plt
import pandas as pd


def plot_time_series_by_branch(
    merged_df: pd.DataFrame, student_name: str = "carlestrullas"
) -> None:
    """Plot and save time series by branch for dropout and performance.

    Args:
        merged_df: Merged dataset created in exercise 2.
        student_name: Identifier used in the output filename.

    Returns:
        None. Saves a PNG figure and prints its path.
    """
    plt.figure(figsize=(14, 10))
    grouped = merged_df.groupby(["Branca", "Curs Acadèmic"], as_index=False).mean(
        numeric_only=True
    )
    branches = grouped["Branca"].unique()
    colors = plt.get_cmap("tab10").colors

    # Subplot 1: Abandonment
    ax1 = plt.subplot(2, 1, 1)
    for i, branch in enumerate(branches):
        data = grouped[grouped["Branca"] == branch]
        ax1.plot(
            data["Curs Acadèmic"],
            data["Abandonament mitjà (%)"],
            label=branch,
            color=colors[i % len(colors)],
        )
    ax1.set_title("Evolution of Dropout Rate by Branch")
    ax1.set_xlabel("Academic Year")
    ax1.set_ylabel("Dropout Rate (%)")
    ax1.legend()
    ax1.grid(True)
    plt.setp(ax1.get_xticklabels(), rotation=45)

    # Subplot 2: Performance
    ax2 = plt.subplot(2, 1, 2)
    for i, branch in enumerate(branches):
        data = grouped[grouped["Branca"] == branch]
        ax2.plot(
            data["Curs Acadèmic"],
            data["Rendiment mitjà (%)"],
            label=branch,
            color=colors[i % len(colors)],
        )
    ax2.set_title("Evolution of Performance Rate by Branch")
    ax2.set_xlabel("Academic Year")
    ax2.set_ylabel("Performance Rate (%)")
    ax2.legend()
    ax2.grid(True)
    plt.setp(ax2.get_xticklabels(), rotation=45)
    plt.tight_layout()

    # Save figure
    src_dir = os.path.dirname(os.path.dirname(__file__))
    img_dir = os.path.join(src_dir, "img")
    os.makedirs(img_dir, exist_ok=True)
    out_path = os.path.join(img_dir, f"evolucio_{student_name}.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"Figure saved to {out_path}")
