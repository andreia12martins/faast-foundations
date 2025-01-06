"""
Module with cleaning functions
"""
# pylint: disable=too-few-public-methods

from abc import ABC, abstractmethod
from life_expectancy.region import Region
import pandas as pd


class DataCleaningStrategy(ABC):
    """Abstract base class for data cleaning strategies."""
    @abstractmethod
    def clean_data(self, data: pd.DataFrame, region: str) -> pd.DataFrame:
        """Abstract method to clean data.
        
        Args:
            data: Input DataFrame to clean
            region: Region to filter data for
            
        Returns:
            Cleaned DataFrame
        """


class CSVDataCleaningStrategy(DataCleaningStrategy):
    """Concrete strategy class for cleaning CSV format data."""
    def clean_data(self, data: pd.DataFrame, region: str) -> pd.DataFrame:
        """Clean CSV format data.
        
        Args:
            data: Input DataFrame to clean
            region: Region to filter data for
            
        Returns:
            Cleaned DataFrame containing only specified region
        """
        cleaning_data = data.copy()
        cleaning_data[['unit', 'sex', 'age', 'geo\\time']] = (
            cleaning_data['unit,sex,age,geo\\time'].str.split(',', expand=True)
        )
        cleaning_data.drop('unit,sex,age,geo\\time', axis=1, inplace=True)
        cleaning_data = cleaning_data.melt(
            id_vars=['unit', 'sex', 'age', 'geo\\time'],
            var_name='year',
            value_name='value'
        )
        cleaning_data = cleaning_data.rename(columns={'geo\\time': 'region'})
        cleaning_data['year'] = cleaning_data['year'].astype(int)
        cleaning_data['value'] = cleaning_data['value'].apply(lambda x: x.split(" ")[0])
        cleaning_data = cleaning_data.drop(cleaning_data[cleaning_data['value'] == ':'].index)
        cleaning_data['value'] = cleaning_data['value'].astype(float)
        cleaned_data = cleaning_data[cleaning_data["region"] == region]

        return cleaned_data


class JSONDataCleaningStrategy(DataCleaningStrategy):
    """Concrete strategy class for cleaning JSON format data."""
    def clean_data(self, data: pd.DataFrame, region: str) -> pd.DataFrame:
        """Clean JSON format data.
        
        Args:
            data: Input DataFrame to clean
            region: Region to filter data for
            
        Returns:
            Cleaned DataFrame containing only specified region
        """
        cleaning_data = data.copy()
        cleaning_data = cleaning_data.drop(["flag", "flag_detail"], axis=1)
        cleaning_data = cleaning_data.rename(
                columns={'country': 'region', 'life_expectancy': 'value'}
        )
        cleaned_data = cleaning_data[cleaning_data["region"] == region]

        return cleaned_data


class DataCleaner:
    """Context class that uses a data cleaning strategy."""
    def __init__(self, strategy: DataCleaningStrategy):
        """Initialize with cleaning strategy.
        
        Args:
            strategy: Strategy object implementing DataCleaningStrategy
        """
        self.strategy = strategy

    def clean_data(self, data: pd.DataFrame, region: Region) -> pd.DataFrame:
        """Clean data using the configured strategy.
        
        Args:
            data: Input DataFrame to clean
            region: Region enum value to filter data for
            
        Returns:
            Cleaned DataFrame containing only specified region
        """
        return self.strategy.clean_data(data, region.value)
