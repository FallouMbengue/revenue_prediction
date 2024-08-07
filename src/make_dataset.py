"""Module for loading data from OpenData."""

import pandas as pd
from typing import Optional
from loguru import logger


def load_data(dataset_path:str, columns_to_lower: Optional[bool] = False) -> pd.DataFrame:
    """Fetch dataset by path.
     Args:
        dataset_path (str): dataset_path to load data

    Returns:
        pd.DataFrame: feature and target data
    """
    data = pd.DataFrame()
    logger.info(f"Dataset lo load from : {dataset_path}")

    if not dataset_path:
        raise ValueError("Dataset path, like ``dataset_path``, must be defined!")
    else:
        data = pd.read_csv(dataset_path)
        logger.info(f"Data shape: {data.shape}")
        logger.info(f"Data description: {data.describe()}")

    if columns_to_lower:
        logger.info("Columns will be transformed to lower!")
        data.columns = data.columns.str.lower()
    
    return data

def date_formatage(df:pd.DataFrame):
    data = df
    data["open date"] = pd.to_datetime(data["open date"])
    data["day"] = data["open date"].dt.day
    data["day_name"] = data["open date"].dt.day_name()
    data["month"] = data["open date"].dt.month
    data["years"] = data["open date"].dt.year
    data.drop("open date",axis=1,inplace=True)
    return data