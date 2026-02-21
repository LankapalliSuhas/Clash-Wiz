from pathlib import Path
from src.reference.load_cards import load_card_metadata

def build_card_index():
    metadata_path = Path("data/raw/card_metadata.json")

    card_info = load_card_metadata(metadata_path)

    # Sort IDs for stable index mapping
    sorted_ids = sorted(card_info.keys())

    card_to_index = {
        card_id: idx
        for idx, card_id in enumerate(sorted_ids)
    }

    return card_info, card_to_index