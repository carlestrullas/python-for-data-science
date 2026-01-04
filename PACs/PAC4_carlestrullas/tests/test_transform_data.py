"""Unit tests for the data transformation helpers."""

import unittest

import pandas as pd
from src.modules import transform_data


class TransformDataTests(unittest.TestCase):
    """Validate the cleaning, grouping, and merging helpers."""

    def test_harmonize_abandonment_columns_renames_expected_fields(self):
        """Legacy abandonment columns are renamed to the normalized schema."""
        df = pd.DataFrame(
            {
                "Naturalesa universitat responsable": ["P"],
                "Universitat responsable": ["UPC"],
                "Sexe Alumne": ["D"],
                "Tipus de centre": ["S"],
            }
        )

        result = transform_data.harmonize_abandonment_columns(df)

        self.assertIn("Tipus universitat", result.columns)
        self.assertIn("Universitat", result.columns)
        self.assertIn("Sexe", result.columns)
        self.assertIn("Integrat S/N", result.columns)
        self.assertNotIn("Naturalesa universitat responsable", result.columns)

    def test_drop_unnecessary_columns_removes_performance_fields(self):
        """Performance dataset columns flagged as redundant are dropped."""
        df = pd.DataFrame(
            {
                "Universitat": ["UPC"],
                "Unitat": ["A"],
                "Crèdits ordinaris superats": [60],
                "Crèdits ordinaris matriculats": [60],
            }
        )

        cleaned = transform_data.drop_unnecessary_columns(df, dataset="performance")

        for column in [
            "Universitat",
            "Unitat",
            "Crèdits ordinaris superats",
            "Crèdits ordinaris matriculats",
        ]:
            self.assertNotIn(column, cleaned.columns)

    def test_group_by_branch_computes_mean_and_renames_column(self):
        """Branch aggregation computes the mean and renames the measure."""
        df = pd.DataFrame(
            {
                "Curs Acadèmic": ["2019-20", "2019-20"],
                "Tipus universitat": ["P", "P"],
                "Sigles": ["UPC", "UPC"],
                "Tipus Estudi": ["Graus", "Graus"],
                "Branca": ["STEM", "STEM"],
                "Sexe": ["D", "D"],
                "Integrat S/N": ["S", "S"],
                "Valor": [80.0, 90.0],
            }
        )

        grouped = transform_data.group_by_branch(df, "Valor", "Mitjana")

        self.assertEqual(grouped.shape[0], 1)
        self.assertAlmostEqual(grouped.loc[0, "Mitjana"], 85.0, places=3)
        self.assertEqual(list(grouped.columns)[-1], "Mitjana")

    def test_merge_datasets_inner_join_only_matches_rows(self):
        """Merge keeps only the intersection of shared grouping keys."""
        shared = {
            "Curs Acadèmic": ["2019-20", "2020-21"],
            "Tipus universitat": ["P", "P"],
            "Sigles": ["UPC", "UPC"],
            "Tipus Estudi": ["G", "G"],
            "Branca": ["STEM", "Arts"],
            "Sexe": ["D", "H"],
            "Integrat S/N": ["S", "S"],
        }
        perf = pd.DataFrame({**shared, "Rendiment mitjà (%)": [85.0, 70.0]})
        aband = pd.DataFrame({**shared, "Abandonament mitjà (%)": [5.0, 8.0]})

        merged = transform_data.merge_datasets(perf, aband)

        self.assertEqual(set(merged["Branca"]), {"STEM", "Arts"})
        self.assertIn("Rendiment mitjà (%)", merged.columns)
        self.assertIn("Abandonament mitjà (%)", merged.columns)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
