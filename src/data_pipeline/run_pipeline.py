# src/data_pipeline/run_pipeline.py

from src.data_pipeline.loader import load_raw_data
from src.data_pipeline.validator import validate_dataset
from src.data_pipeline.cleaner import clean_dataset
from src.config import CLEAN_MATCH_FILE
from src.utils.logger import get_logger

logger = get_logger("pipeline")

def run():
    df = load_raw_data()
    validate_dataset(df)
    df_clean = clean_dataset(df)

    CLEAN_MATCH_FILE.parent.mkdir(parents=True, exist_ok=True)
    df_clean.to_parquet(CLEAN_MATCH_FILE)

    logger.info(f"Saved cleaned dataset to {CLEAN_MATCH_FILE}")

if __name__ == "__main__":
    run()