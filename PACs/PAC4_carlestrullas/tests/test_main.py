"""Unit tests ensuring the PAC4 CLI orchestrator behaves as expected."""

import sys
import unittest
from contextlib import ExitStack
from unittest.mock import patch

from src import main as pac4_main


class MainModuleTests(unittest.TestCase):
    """Verify that CLI argument parsing triggers the right exercises."""

    def test_main_runs_only_requested_exercises(self):
        """Passing -ex 2 should execute only exercises 1 and 2."""
        with ExitStack() as stack:
            ex1 = stack.enter_context(
                patch.object(
                    pac4_main, "run_exercise_1", return_value=("perf", "aband")
                )
            )
            ex2 = stack.enter_context(
                patch.object(pac4_main, "run_exercise_2", return_value="merged")
            )
            ex3 = stack.enter_context(patch.object(pac4_main, "run_exercise_3"))
            ex4 = stack.enter_context(patch.object(pac4_main, "run_exercise_4"))
            stack.enter_context(patch.object(sys, "argv", ["pac4", "-ex", "2"]))

            pac4_main.main()

        self.assertEqual(ex1.call_count, 1)
        self.assertEqual(ex2.call_count, 1)
        ex2.assert_called_once_with("perf", "aband")
        ex3.assert_not_called()
        ex4.assert_not_called()

    def test_main_runs_all_exercises_by_default(self):
        """Without arguments, the CLI should run exercises 1 through 4."""
        with ExitStack() as stack:
            ex1 = stack.enter_context(
                patch.object(
                    pac4_main, "run_exercise_1", return_value=("perf", "aband")
                )
            )
            ex2 = stack.enter_context(
                patch.object(pac4_main, "run_exercise_2", return_value="merged")
            )
            ex3 = stack.enter_context(patch.object(pac4_main, "run_exercise_3"))
            ex4 = stack.enter_context(patch.object(pac4_main, "run_exercise_4"))
            stack.enter_context(patch.object(sys, "argv", ["pac4"]))

            pac4_main.main()

        self.assertEqual(ex1.call_count, 1)
        ex2.assert_called_once_with("perf", "aband")
        ex3.assert_called_once_with("merged")
        ex4.assert_called_once_with("merged")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
