"""Unit tests asserting the visualization module emits expected files."""

import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd
from src.modules import visual_analysis


class VisualAnalysisTests(unittest.TestCase):
    """Ensure plotting helpers emit the expected PNG artifact."""

    def test_plot_time_series_by_branch_creates_png(self):
        """Plotting time series should save a deterministic PNG file."""
        df = pd.DataFrame(
            {
                "Branca": ["Arts", "Arts", "STEM", "STEM"],
                "Curs Acadèmic": ["2018-19", "2019-20", "2018-19", "2019-20"],
                "Abandonament mitjà (%)": [5.0, 4.5, 7.0, 6.5],
                "Rendiment mitjà (%)": [85.0, 86.0, 82.0, 83.0],
            }
        )

        output_path = (
            Path(visual_analysis.__file__).resolve().parents[1]
            / "img"
            / "evolucio_unittest.png"
        )
        if output_path.exists():
            output_path.unlink()

        with patch("src.modules.visual_analysis.print"):
            visual_analysis.plot_time_series_by_branch(df, student_name="unittest")

        self.assertTrue(output_path.exists(), "Expected PNG output was not created")
        output_path.unlink()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
