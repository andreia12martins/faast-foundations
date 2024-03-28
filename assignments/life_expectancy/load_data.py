"""
Module for loading data.
"""
import pandas as pd
from pathlib import Path

def load_data(file_path: Path, separator='\t') -> pd.DataFrame:
    """
    Load data from a CSV file into a pandas DataFrame.
    """
    return pd.read_csv(file_path, delimiter=separator)