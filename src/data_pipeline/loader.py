# src/data_pipeline/loader.py

import pandas as pd
from src.config import RAW_MATCH_FILE
from src.utils.logger import get_logger

logger = get_logger("loader")

def load_raw_data() -> pd.DataFrame:
    """
    Loads raw Kaggle dataset.
    Fails loudly if file missing.
    """

    if not RAW_MATCH_FILE.exists():
        raise FileNotFoundError(f"Raw data not found at {RAW_MATCH_FILE}")

    logger.info("Loading raw dataset...")
    df = pd.read_csv(RAW_MATCH_FILE)

    logger.info(f"Loaded {len(df)} rows and {len(df.columns)} columns.")
    return df