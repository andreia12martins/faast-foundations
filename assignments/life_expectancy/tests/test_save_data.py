from unittest.mock import patch
import pandas as pd
from life_expectancy.save_data import save_data
from . import FIXTURES_DIR

def test_save_data():
    with patch('pandas.DataFrame.to_csv') as to_csv_mock:
        save_data(pd.DataFrame(), FIXTURES_DIR / "eu_life_expectancy_expected.csv")
        to_csv_mock.assert_called_once()
