# src/data_pipeline/validator.py

import pandas as pd
from src.config import EXPECTED_COLUMNS, DECK_SIZE, MIN_TROPHIES, MAX_TROPHIES
from src.utils.logger import get_logger

logger = get_logger("validator")

def validate_columns(df: pd.DataFrame):
    missing = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    logger.info("Column validation passed.")

def validate_trophies(df: pd.DataFrame):
    if df["player_trophies"].min() < MIN_TROPHIES:
        raise ValueError("Invalid trophy values detected.")
    if df["player_trophies"].max() > MAX_TROPHIES:
        raise ValueError("Trophy values exceed logical maximum.")
    logger.info("Trophy validation passed.")

def validate_decks(df: pd.DataFrame):
    def check_deck(deck):
        cards = deck.split(",")
        return len(cards) == DECK_SIZE

    invalid = df[~df["player_deck"].apply(check_deck)]
    if len(invalid) > 0:
        raise ValueError("Some decks do not contain exactly 8 cards.")

    logger.info("Deck validation passed.")

def validate_dataset(df: pd.DataFrame):
    validate_columns(df)
    validate_trophies(df)
    validate_decks(df)
    logger.info("All validations passed successfully.")