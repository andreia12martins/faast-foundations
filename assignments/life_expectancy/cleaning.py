"""
Module with cleaning functions
"""

import argparse
from pathlib import Path
import pandas as pd
from life_expectancy.load_data import load_data
from life_expectancy.save_data import save_data


def clean_data(data, country="PT") -> pd.DataFrame:
    """
    This function performs several cleaning operations on the input data:
    1. Splits the 'unit,sex,age,geo\\time' column into separate columns.
    2. Melts the data to a long format with 'unit', 'sex', 'age', 'geo\\time' as identifiers.
    3. Renames the 'geo\\time' column to 'region'.
    4. Converts the 'year' column to integer type.
    5. Extracts numerical values from the 'value' column.
    6. Removes rows with missing or invalid values (indicated by ':').
    7. Filters the data to include only rows corresponding to the specified country.

    Args:
    - data (pandas.DataFrame): Input data to be cleaned and filtered.
    - country (str, optional): Country code to filter the data. Default is "PT" for Portugal.

    Returns:
    - cleaned_data (pandas.DataFrame): Cleaned and filtered data for the specified country.
    """
    data['unit'] = data['unit,sex,age,geo\\time'].apply(lambda x: x.split(",")[0])
    data['sex'] = data['unit,sex,age,geo\\time'].apply(lambda x: x.split(",")[1])
    data['age'] = data['unit,sex,age,geo\\time'].apply(lambda x: x.split(",")[2])
    data['geo\\time'] = data['unit,sex,age,geo\\time'].apply(lambda x: x.split(",")[3])
    data.drop('unit,sex,age,geo\\time', axis=1, inplace=True)
    data = data.melt(
        id_vars=['unit', 'sex', 'age', 'geo\\time'],
        var_name='year',
        value_name='value')
    data = data.rename(columns={'geo\\time': 'region'})
    data['year'] = data['year'].astype(int)
    data['value'] = data['value'].apply(lambda x: x.split(" ")[0])
    data = data.drop(data[data['value'] == ':'].index)
    data['value'] = data['value'].astype(float)
    cleaned_data = data[data["region"] == country]

    return cleaned_data


def main(load_path, save_path, country="PT") -> pd.DataFrame:
    """
    Main function to load, clean, and save data.

    Args:
    - file_path (str): Path to the data file.
    - country (str): Country code to filter the data.
    """
    data_raw = load_data(load_path)
    cleaned_data = clean_data(data_raw, country)
    save_data(cleaned_data, save_path)

    return cleaned_data


if __name__ == "__main__": # pragma: no cover
    path_data_load = Path(__file__).parents[0] / "data/eu_life_expectancy_raw.tsv"
    path_data_save = Path(__file__).parents[0] / "data/pt_life_expectancy.csv"

    parser = argparse.ArgumentParser(
        description="Clean life expectancy data for a specific country.")
    parser.add_argument("--file_path",
                        default="assignments/life_expectancy/data/eu_life_expectancy_raw.tsv",
                        help="Path to the data file")
    parser.add_argument("--country", default="PT",
                        help="Country code to filter the data")
    args = parser.parse_args()

    main(path_data_load, path_data_save, args.country)
