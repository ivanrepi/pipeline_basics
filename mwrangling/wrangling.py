import pandas as pd

def wrangling(df, year, col):
    df = df[df[col].isin(year)]
    return df