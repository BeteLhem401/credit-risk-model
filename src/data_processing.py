import pandas as pd
from sklearn.preprocessing import StandardScaler


def scale_features(df):
    scaler = StandardScaler()

    numeric_cols = df.select_dtypes(include="number").columns

    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df