"""
Module for loading data.
"""
from pathlib import Path
import pandas as pd

def load_data(file_path: Path, separator='\t') -> pd.DataFrame:
    """
    Load data from a CSV file into a pandas DataFrame.
    """
    return pd.read_csv(file_path, delimiter=separator)
