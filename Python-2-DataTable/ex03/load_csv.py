import pandas as pandas


def load(path: str) -> pandas.DataFrame | None:
    """Read CSV file, check error, print dimensions and return dataframe"""

    try:
        dataframe = pandas.read_csv(path)
    except Exception as e:
        print("Error loading CSV file :", e)
        return None
    print("Loading dataset of dimensions", dataframe.shape)
    return dataframe
