"""
Module for test load_data()
"""

from unittest.mock import patch
import pandas as pd
from life_expectancy.load_data import load_data
from . import FIXTURES_DIR

# pylint: disable=C0116
def test_load_data(eu_life_expectancy_expected_subset):
    """Run the `load_data` function and compare the output to the expected output"""
    with patch('pandas.read_csv') as read_csv_mock:
        read_csv_mock.side_effect = [
            eu_life_expectancy_expected_subset
        ]
        data_actual = load_data(FIXTURES_DIR / "eu_life_expectancy_expected.csv", "[\t,]")

        pd.testing.assert_frame_equal(data_actual, eu_life_expectancy_expected_subset)
        read_csv_mock.assert_called_once()
