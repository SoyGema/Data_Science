
import numpy as np

## Replace missing values with mean

mean = np.mean(df.column)
data = df.column.fillna(mean)

## Drop rows with missing values 

df. dropna(axis=0)

##  Drop in function 

def clean_dataset(df):
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)
