import pandas as pd
from src.data_pipeline.validator import validate_columns

def test_missing_columns():
    df = pd.DataFrame({"random": [1, 2, 3]})
    try:
        validate_columns(df)
        assert False
    except ValueError:
        assert True