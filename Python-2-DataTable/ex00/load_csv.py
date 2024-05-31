import pandas as pd


def load(path: str) -> pd.DataFrame:
    try:
        dataFrame = pd.read_csv(path)
    except Exception:
        return None
    print(f"Loading dataset of dimensions {dataFrame.shape}")
    return dataFrame

# resources
# - https://www.w3schools.com/python/pandas/pandas_dataframes.asp
