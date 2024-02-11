import pytest
import pandas as pd
from src.main import find_most_accurate_name_and_calculate_similarity

def test_fuction_return_dataframe():
    names = [ "Абдурашвидова Диана",
        "Абдурашвидова Диана Магомедовна",
        "Абдурашвідова Діана Магомедівна",]
    res = find_most_accurate_name_and_calculate_similarity(names)

    assert isinstance(res, pd.DataFrame)
