"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy.cleaning import DataCleaner, CSVDataCleaningStrategy
from life_expectancy.region import Region

def test_clean_data(eu_life_expectancy_raw_subset, eu_life_expectancy_expected_subset):
    """Run the `clean_data` function and compare the output to the expected output"""
    strategy = DataCleaner(strategy=CSVDataCleaningStrategy())
    actual_cleaned_data = strategy.clean_data(eu_life_expectancy_raw_subset, Region.PT)
    actual_cleaned_data = actual_cleaned_data.reset_index(drop=True)
    pd.testing.assert_frame_equal(
        actual_cleaned_data, eu_life_expectancy_expected_subset
    )
