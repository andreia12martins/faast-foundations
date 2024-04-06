"Module for generate a data sample"
import random
from pathlib import Path
from life_expectancy.cleaning import clean_data
import pandas as pd
from . import OUTPUT_DIR, FIXTURES_DIR

def generate_data_sample(
        input_path: Path,
        region: str,
        number_of_rows: int,
        output_path: Path
    ) -> None:
    """
    Generate a data sample based on the given input file, region, and number of rows,
    and save it to the specified output file.
    """

    with open(input_path, 'r', encoding='utf-8') as file:
        file = file.readlines()

    header = file[0]
    data_rows = file[1:]

    found_region = False
    while not found_region:
        subset_sample = random.sample(data_rows, number_of_rows)
        found_region = any(region in row for row in subset_sample)

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(header)
        for row in subset_sample:
            file.write(row)


def main():
    """Main function to generate a data sample, clean it, and save the cleaned data."""
    input_path = OUTPUT_DIR / "eu_life_expectancy_raw.tsv"
    output_path = FIXTURES_DIR / "eu_life_expectancy_raw.tsv"

    generate_data_sample(
        input_path=input_path,
        region='PT',
        number_of_rows=40,
        output_path=output_path
    )

    # generate the corresponding cleaned data for the raw subset
    data_raw_subset = pd.read_csv(output_path, delimiter='\t')
    expected_cleaned_data = clean_data(data_raw_subset)
    expected_cleaned_data.to_csv("life_expectancy/tests/fixtures/eu_life_expectancy_expected.csv",
                                 sep="\t",
                                 index=False,
                                 header=True)

if __name__ == "__main__":
    main()
