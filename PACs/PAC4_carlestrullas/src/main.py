"""
Main script for PAC4 - Student Performance in Catalonia. This script runs all
the required analyses and functionalities for the assignment.
"""

import argparse

from src.modules import (
    eda,
    load_data,
    statistical_analysis,
    transform_data,
    visual_analysis,
)


def run_exercise_1():
    """
    Load both datasets and perform exploratory data analysis (EDA).

    Returns
    -------
    df_perf : pd.DataFrame
        Performance dataset.
    df_aband : pd.DataFrame
        Abandonment dataset.
    """
    print("Exercise 1: Load dataset and EDA")
    df_perf = load_data.load_dataset("rendiment_estudiants.xlsx")
    df_aband = load_data.load_dataset("taxa_abandonament.xlsx")
    print("\nPerformance dataset:")
    eda.show_eda(df_perf)
    print("\nAbandonment dataset:")
    eda.show_eda(df_aband)
    return df_perf, df_aband


def run_exercise_2(df_perf, df_aband):
    """
    Clean, harmonize, group, and merge the datasets for further analysis.
    Args:
        df_perf (pd.DataFrame): Performance dataset.
        df_aband (pd.DataFrame): Abandonment dataset.
    Returns:
        merged (pd.DataFrame): Merged dataset ready for analysis.
    """
    print("\nExercise 2: Data cleaning, harmonization, grouping, and merging")
    df_aband_h = transform_data.harmonize_abandonment_columns(df_aband)
    df_perf_c = transform_data.drop_unnecessary_columns(df_perf, "performance")
    df_aband_c = transform_data.drop_unnecessary_columns(df_aband_h, "abandonment")
    df_perf_g = transform_data.group_by_branch(
        df_perf_c, "Taxa rendiment", "Rendiment mitjà (%)"
    )
    df_aband_g = transform_data.group_by_branch(
        df_aband_c, "% Abandonament a primer curs", "Abandonament mitjà (%)"
    )
    merged = transform_data.merge_datasets(df_perf_g, df_aband_g)
    print("\nMerged dataset (first 5 rows):")
    print(merged.head())
    return merged


def run_exercise_3(merged):
    """
    Generate and save time series visualizations for abandonment and performance
    rates by branch.
    Args:
        merged (pd.DataFrame): Merged dataset.
    """
    print("\nExercise 3: Time series visualization")
    visual_analysis.plot_time_series_by_branch(merged, student_name="carlestrullas")


def run_exercise_4(merged):
    """
    Perform statistical analysis and save results as a JSON report.
    Args:
        merged (pd.DataFrame): Merged dataset.
    """
    print("\nExercise 4: Statistical analysis and JSON report")
    statistical_analysis.analyze_dataset(merged)


def main():
    """
    Main entry point for PAC4. Parses command-line arguments and runs the
    requested exercises.
    """
    parser = argparse.ArgumentParser(
        description="PAC4 - Student Performance in Catalonia",
        epilog=(
            "\nExamples:\n"
            "  python main.py         # Run all exercises (1-4)\n"
            "  python main.py -ex 2  # Run exercises 1 and 2 only\n"
            "  python main.py --help # Show this help message\n"
            "\nExercises:\n"
            "  1: Load datasets and show EDA\n"
            "  2: Clean, harmonize, group, and merge datasets\n"
            "  3: Visualize time series by branch\n"
            "  4: Statistical analysis and JSON report\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-ex",
        type=int,
        default=4,
        help=(
            "Run exercises 1 to N (default: all). "
            "For example, -ex 2 runs only exercises 1 and 2."
        ),
    )
    args = parser.parse_args()

    # Always run progressively from 1 to N
    df_perf, df_aband, merged = None, None, None
    if args.ex >= 1:
        df_perf, df_aband = run_exercise_1()
    if args.ex >= 2:
        merged = run_exercise_2(df_perf, df_aband)
    if args.ex >= 3:
        run_exercise_3(merged)
    if args.ex >= 4:
        run_exercise_4(merged)


if __name__ == "__main__":
    main()
