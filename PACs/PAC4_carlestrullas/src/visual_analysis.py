"""
Visualization utilities for PAC4
"""

import os

import matplotlib.pyplot as plt
import pandas as pd


def plot_time_series_by_branch(
    merged_df: pd.DataFrame, student_name: str = "carlestrullas"
):
    """
    Generate and save time series plots for abandonment and performance rates by branch.
    Args:
        merged_df (pd.DataFrame): Merged dataset with columns for academic year,
            branch, performance, and abandonment.
        student_name (str): Name to use in the output filename.
    """
    plt.figure(figsize=(14, 10))
    branches = merged_df["Branca"].unique()
    colors = plt.get_cmap("tab10").colors
    # Subplot 1: Abandonment
    ax1 = plt.subplot(2, 1, 1)
    for i, branch in enumerate(branches):
        data = merged_df[merged_df["Branca"] == branch]
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
        data = merged_df[merged_df["Branca"] == branch]
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

    img_dir = os.path.join(os.path.dirname(__file__), "img")
    os.makedirs(img_dir, exist_ok=True)
    out_path = os.path.join(img_dir, f"evolucio_{student_name}.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"Figure saved to {out_path}")
    print(f"Figure saved to {out_path}")
    print(f"Figure saved to {out_path}")
    print(f"Figure saved to {out_path}")
    print(f"Figure saved to {out_path}")
    print(f"Figure saved to {out_path}")
    print(f"Figure saved to {out_path}")
    print(f"Figure saved to {out_path}")
    print(f"Figure saved to {out_path}")
