"""
Module for loading data.
"""
from pathlib import Path
import pandas as pd

def load_csv(file_path: Path, separator='\t') -> pd.DataFrame:
    """
    Load data from a CSV file into a pandas Dataframe.
    """
    return pd.read_csv(file_path, delimiter=separator)


def load_json(file_path: Path) -> pd.DataFrame:
    """
    Load data from a JSON file into a pandas Dataframe.
    """
    return pd.read_json(file_path)
