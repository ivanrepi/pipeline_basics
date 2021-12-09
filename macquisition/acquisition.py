import pandas as pd

# Acquisition methods

def acquisition(path_file):
    dataframe = pd.read_csv(path_file)
    return dataframe