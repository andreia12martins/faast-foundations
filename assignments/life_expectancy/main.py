import pandas as pd
import argparse
from pathlib import Path
from life_expectancy.region import Region, string_2_enum
from life_expectancy.cleaning import DataCleaner, CSVDataCleaningStrategy, JSONDataCleaningStrategy
from life_expectancy.load_data import load_csv, load_json
from life_expectancy.save_data import save_data

def main(file_path: str, output_path: str, region: str) -> pd.DataFrame:
    # path strs to Path object
    file_path = Path(file_path)
    output_path = Path(output_path)

    # load data and create strategy based on input
    format = str(file_path).split(".")[1]
    if format == "csv" or format == "tsv":
        data_raw = load_csv(file_path)
        strategy = CSVDataCleaningStrategy()
    elif format == "json":
        data_raw = load_json(file_path)
        strategy = JSONDataCleaningStrategy()
    else:
        raise ValueError(
            f"Unsupported data format: {format}. Please provide a file with 'tsv', 'csv', or 'json' format."
        )
    cleaner = DataCleaner(strategy)

    # create Region enum based on input
    region = string_2_enum(region)
    if not region:
        raise ValueError(
            f"Unsupported region. Must be one of {Region.get_countries()}."
        )
    
    cleaned_data = cleaner.clean_data(data_raw, region)
    save_data(cleaned_data, output_path)
    return cleaned_data


if __name__ == "__main__": # pragma: no cover
    default_file_path = Path(__file__).parents[0] / "data/eu_life_expectancy_raw.tsv"
    default_output_path = Path(__file__).parents[0] / "data/pt_life_expectancy.csv"

    parser = argparse.ArgumentParser(
        description="Clean life expectancy data for a specific region.")
    parser.add_argument("--file-path",
                        default=default_file_path,
                        help="Path to the data file")
    parser.add_argument("--output-path",
                        default=default_output_path,
                        help="Path to save the cleaned data")
    parser.add_argument("--region", default="PT",
                        help="Region code to filter the data")
    args = parser.parse_args()

    main(args.file_path, args.output_path, args.region)