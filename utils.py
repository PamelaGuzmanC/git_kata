

import pandas as pd

def load_titanic_male():
    df = pd.read_csv('data/titanic.csv')
    male_df = df[df["sex"] == "male"]
    return male_df
