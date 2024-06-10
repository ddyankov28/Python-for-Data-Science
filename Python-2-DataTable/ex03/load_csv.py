import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''
    Reads .CSV file and
    returns it as a Pandas DataFrame object
    -------
    @param
        - path: str -> the path of the file
    -------
    @rtype
        - Pandas DataFrame
    -------
    @return
        - The data from file as a Pandas DataFrame ojbect
    '''
    try:
        dataFrame = pd.read_csv(path)
    except Exception:
        print("Error: Path is bad or has bad format")
        return None
#    print(f"Loading dataset of dimensions {dataFrame.shape}")
    return dataFrame

# resources
# - https://www.w3schools.com/python/pandas/pandas_dataframes.asp
# - https://www.w3schools.com/python/pandas/pandas_csv.asp
