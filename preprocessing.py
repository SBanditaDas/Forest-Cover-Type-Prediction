import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    """
    Scales numeric features and returns the processed DataFrame.
    """
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.drop("Cover_Type")
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df