"""Tests for the cleaning module"""
import pytest
import pandas as pd
from life_expectancy.cleaning import (
    DataCleaner,
    CSVDataCleaningStrategy,
    JSONDataCleaningStrategy
)
from life_expectancy.region import Region


def test_clean_data_csv(eu_life_expectancy_raw_subset, eu_life_expectancy_expected_subset):
    """Test CSV data cleaning strategy"""
    strategy = DataCleaner(strategy=CSVDataCleaningStrategy())
    actual_cleaned_data = strategy.clean_data(eu_life_expectancy_raw_subset, Region.PT)
    actual_cleaned_data = actual_cleaned_data.reset_index(drop=True)
    pd.testing.assert_frame_equal(
        actual_cleaned_data, eu_life_expectancy_expected_subset
    )


def test_clean_data_json():
    """Test JSON data cleaning strategy"""
    # Create sample JSON-like DataFrame
    input_data = pd.DataFrame({
        'country': ['PT', 'ES', 'PT'],
        'year': [2020, 2020, 2021],
        'life_expectancy': [80.1, 82.3, 80.5],
        'flag': ['', '', ''],
        'flag_detail': ['', '', '']
    })
    
    expected_output = pd.DataFrame({
        'region': ['PT', 'PT'],
        'year': [2020, 2021],
        'value': [80.1, 80.5]
    })
    
    strategy = DataCleaner(strategy=JSONDataCleaningStrategy())
    actual_cleaned_data = strategy.clean_data(input_data, Region.PT)
    actual_cleaned_data = actual_cleaned_data.reset_index(drop=True)
    pd.testing.assert_frame_equal(actual_cleaned_data, expected_output)


def test_abstract_strategy():
    """Test that abstract class cannot be instantiated"""
    from life_expectancy.cleaning import DataCleaningStrategy
    
    with pytest.raises(TypeError):
        DataCleaningStrategy()
