# src/data_pipeline/time_split.py

import pandas as pd

def time_based_split(df: pd.DataFrame, split_date: str):
    """
    Splits dataset chronologically.
    """

    split_date = pd.to_datetime(split_date)

    train = df[df["battle_time"] < split_date]
    test = df[df["battle_time"] >= split_date]

    return train, test