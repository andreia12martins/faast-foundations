"""
Module for test load_data()
"""

from unittest.mock import patch
import pandas as pd
from life_expectancy.load_data import load_csv, load_json
from . import FIXTURES_DIR

# pylint: disable=C0116
def test_load_data(eu_life_expectancy_expected_subset):
    """Run the `load_data` function and compare the output to the expected output"""
    with patch('pandas.read_csv') as read_csv_mock:
        read_csv_mock.side_effect = [
            eu_life_expectancy_expected_subset
        ]
        data_actual = load_csv(FIXTURES_DIR / "eu_life_expectancy_expected.csv", "[\t,]")

        pd.testing.assert_frame_equal(data_actual, eu_life_expectancy_expected_subset)
        read_csv_mock.assert_called_once()

def test_load_json(eu_life_expectancy_expected_subset):
    """Test the load_json function with mocked pandas read_json"""
    with patch('pandas.read_json') as read_json_mock:
        read_json_mock.side_effect = [
            eu_life_expectancy_expected_subset
        ]
        data_actual = load_json(FIXTURES_DIR / "eu_life_expectancy_expected.json")

        pd.testing.assert_frame_equal(data_actual, eu_life_expectancy_expected_subset)
        read_json_mock.assert_called_once()
