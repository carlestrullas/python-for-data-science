"""Unit tests covering dataset loading workflows."""

import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd
from src.modules import load_data


class LoadDataTests(unittest.TestCase):
    """Exercise the interactive and path-based dataset loader."""

    def test_load_dataset_with_relative_path(self):
        """Ensure relative paths are resolved under the project data folder."""
        expected_df = pd.DataFrame({"value": [1, 2]})

        with patch("src.modules.load_data.print"), patch.object(
            load_data.pd, "read_excel", return_value=expected_df
        ) as mock_read:
            result = load_data.load_dataset("custom.xlsx")

        data_dir = (
            Path(load_data.__file__).resolve().parents[2] / "data" / "custom.xlsx"
        )
        self.assertEqual(Path(mock_read.call_args[0][0]), data_dir)
        self.assertIs(result, expected_df)

    def test_load_dataset_prompt_selection(self):
        """Interactive prompt keeps looping until a valid option is selected."""
        selected_df = pd.DataFrame({"value": [42]})

        with patch("src.modules.load_data.print"), patch(
            "builtins.input", side_effect=["9", "2"]
        ):
            with patch.object(
                load_data.pd, "read_excel", return_value=selected_df
            ) as mock_read:
                result = load_data.load_dataset()

        expected_path = (
            Path(load_data.__file__).resolve().parents[2]
            / "data"
            / "taxa_abandonament.xlsx"
        )
        self.assertEqual(Path(mock_read.call_args[0][0]), expected_path)
        self.assertIs(result, selected_df)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
