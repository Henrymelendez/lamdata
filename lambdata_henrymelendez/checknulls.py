import pandas as pd 

def check_for_nulls(df):
    print(df.isnull().sum())

