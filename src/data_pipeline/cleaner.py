# src/data_pipeline/cleaner.py

import pandas as pd
from src.utils.logger import get_logger

logger = get_logger("cleaner")

def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting cleaning process...")

    # Remove duplicates
    df = df.drop_duplicates()

    # Drop null match IDs
    df = df.dropna(subset=["match_id"])

    # Normalize battle_time
    df["battle_time"] = pd.to_datetime(df["battle_time"], errors="coerce")

    # Drop invalid timestamps
    df = df.dropna(subset=["battle_time"])

    # Standardize winner column
    df["winner"] = df["winner"].astype(str).str.lower()

    logger.info(f"Cleaning complete. Remaining rows: {len(df)}")

    return df