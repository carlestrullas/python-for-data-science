"""Unit tests validating the statistical analysis reporting module."""

import json
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd
from src.modules import statistical_analysis


class StatisticalAnalysisTests(unittest.TestCase):
    """Cover the JSON reporting workflow for statistical analysis."""

    def setUp(self):
        self.report_path = (
            Path(statistical_analysis.__file__).resolve().parents[1]
            / "report"
            / "analisi_estadistic.json"
        )
        self.original_bytes = (
            self.report_path.read_bytes() if self.report_path.exists() else None
        )

    def tearDown(self):
        if self.original_bytes is not None:
            self.report_path.write_bytes(self.original_bytes)
        elif self.report_path.exists():
            self.report_path.unlink()

    def test_analyze_dataset_generates_report(self):
        """Running the analysis should persist a structured JSON payload."""
        df = pd.DataFrame(
            {
                "Curs Acadèmic": ["2018-19", "2019-20", "2018-19", "2019-20"],
                "Branca": ["Arts", "Arts", "STEM", "STEM"],
                "Abandonament mitjà (%)": [5.0, 4.0, 7.0, 6.0],
                "Rendiment mitjà (%)": [85.0, 86.0, 82.0, 83.0],
            }
        )

        with patch("src.modules.statistical_analysis.print"):
            statistical_analysis.analyze_dataset(df)

        self.assertTrue(self.report_path.exists())
        payload = json.loads(self.report_path.read_text(encoding="utf-8"))
        self.assertEqual(set(payload["analisis_por_rama"].keys()), {"Arts", "STEM"})
        self.assertEqual(payload["analysis_metadata"]["num_registros"], 4)
        self.assertIn(payload["rankings"]["mejor_rendimiento"], {"Arts", "STEM"})


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
