import pandas as pd
import numpy as np

def analysis(df, groupby_col, agg_col):
    df = df.groupby([groupby_col])[agg_col].agg(np.sum)
    df.to_csv('./data/vehicles_output.csv')
    message = '/---------PIPELINE SUCCESSFULY EXECUTED--------/'
    return message