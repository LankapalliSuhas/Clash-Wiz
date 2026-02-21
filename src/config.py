# src/config.py

from pathlib import Path

# Root Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data Paths
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
META_FILTERED_DIR = DATA_DIR / "meta_filtered"

# Files
RAW_MATCH_FILE = RAW_DATA_DIR / "matches.csv"
CLEAN_MATCH_FILE = INTERIM_DATA_DIR / "clean_matches.parquet"
FINAL_DATA_FILE = PROCESSED_DATA_DIR / "model_ready.parquet"

# Columns expected in Kaggle dataset
EXPECTED_COLUMNS = [
    "match_id",
    "player_tag",
    "opponent_tag",
    "player_deck",
    "opponent_deck",
    "player_trophies",
    "opponent_trophies",
    "winner",
    "battle_time",
    "arena"
]

# Validation thresholds
MIN_TROPHIES = 0
MAX_TROPHIES = 9000
DECK_SIZE = 8