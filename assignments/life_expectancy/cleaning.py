"""
Module with cleaning functions
"""

import argparse

import pandas as pd


def clean_data(country="PT") -> None:
    """
    Reads raw life expectancy data, cleans it, and filters it for Portugal (PT) region.

    Raises:
    FileNotFoundError: If the specified file path is incorrect or the file is not found.
    """
    file_path = 'assignments/life_expectancy/data/eu_life_expectancy_raw.tsv'
    data = pd.read_csv(file_path, delimiter='\t')
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
    data = data[data["region"] == country]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Clean life expectancy data for a specific country.")
    parser.add_argument("--country", default="PT")
    args = parser.parse_args()
    clean_data(country=args.country)
