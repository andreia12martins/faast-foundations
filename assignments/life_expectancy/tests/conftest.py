"""Pytest configuration file"""
import pandas as pd
import pytest

from . import FIXTURES_DIR


@pytest.fixture(scope="function")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv", delimiter="\t")


@pytest.fixture(scope="function")
def eu_life_expectancy_raw_subset() -> pd.DataFrame:
    """Fixture to load a raw subset of eu data"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_raw.tsv", delimiter="\t")


@pytest.fixture(scope="function")
def eu_life_expectancy_expected_subset() -> pd.DataFrame:
    """Fixture to load the expected subset of cleaned eu data"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_expected.csv", delimiter="\t")
