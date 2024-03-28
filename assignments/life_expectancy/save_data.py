"""
Module for saving data.
"""

from pathlib import Path
import pandas as pd

def save_data(data: pd.DataFrame, file_path: Path) -> None:
    """
    Save a pandas DataFrame to a CSV file.
    """
    data.to_csv(file_path, index=False, header=True)
