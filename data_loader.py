import pandas as pd
import os
def load_csv(path:str):
    if not os.path.exists(path):
        raise ValueError("The provided file does not exist.")
    if not path.endswith('.csv'):
        raise ValueError("The provided file is not a CSV file.")
    df =  pd.read_csv(path)
    if df.empty:
        raise ValueError("The provided CSV file is empty.")
    return df
