"""Tests for the cleaning module"""
from unittest.mock import patch
import pandas as pd
from life_expectancy.cleaning import clean_data, main, Regions
from . import FIXTURES_DIR

def test_clean_data(eu_life_expectancy_raw_subset, eu_life_expectancy_expected_subset):
    """Run the `clean_data` function and compare the output to the expected output"""
    actual_cleaned_data = clean_data(eu_life_expectancy_raw_subset)
    actual_cleaned_data = actual_cleaned_data.reset_index(drop=True)
    pd.testing.assert_frame_equal(
        actual_cleaned_data, eu_life_expectancy_expected_subset
    )


def test_main(eu_life_expectancy_raw_subset, eu_life_expectancy_expected_subset):
    """Tests the main function by mocking the read_csv and to_csv methods, 
    and then asserts that the obtained data matches the expected cleaned data.
    """
    with patch('pandas.read_csv') as read_csv_mock:
        read_csv_mock.side_effect = [eu_life_expectancy_raw_subset]
        with patch('pandas.DataFrame.to_csv') as to_csv_mock:
            to_csv_mock.side_effect = print("The clean data was saved!")
            data_obtained = main(FIXTURES_DIR / "eu_life_expectancy_raw.tsv",
                                 FIXTURES_DIR / "eu_life_expectancy_expected.csv",
                                 country=Regions.PT)
            data_obtained = data_obtained.reset_index(drop=True)

    pd.testing.assert_frame_equal(
        data_obtained, eu_life_expectancy_expected_subset
    )
