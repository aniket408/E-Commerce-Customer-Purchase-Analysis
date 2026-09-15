import pandas as pd
from src.config import RAW_DATA_PATH

def load_data():
    df = pd.read_excel(
    RAW_DATA_PATH
    )
    
    # calen
    return df