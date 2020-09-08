import pandas as pd
import numpy as np

def completeWithMean(column):
    return (column.shift() + column.shift(-1)) / 2

def getCumulativeColumn(df):
    duplicated = df.duplicated('Total')
    df.loc[duplicated, ['Total']] = np.NaN
    
    df.Total = np.where(df['Total'].isnull(),
                               completeWithMean(df['Total']),
                               df['Total'])

    df.fillna(method='pad', inplace=True)
    df.Total = df.Total.round().astype(int)
    
    return df

def addNewCasesColumn(df):
    df['New'] = (df.Total - df.Total.shift(1)).fillna(0).astype(int)
    return df

def mergeConfirmedDeath(confirmed, deaths):
    return pd.merge(confirmed, deaths,
                    left_index=True, right_index=True,
                    suffixes=('ConfirmedCases', 'DeathCases'))

def addNumericIndex(df):
    df['num_id'] = np.arange(len(df) + 1)[1:]
    return df