import pandas as pd
<<<<<<< HEAD
df = pd.read_csv('/Users/pamelaguzman/git_kata/data/titanic.csv')
print(df.columns)
print(df["sex"].unique())
female_df = df[df["sex"]=="female"]
print(female_df)
=======
def load_titanic_female():
    df = pd.read_csv('data/titanic.csv')
    print(df.columns)
    print(df["sex"].unique())
    female_df = df[df["sex"]=="male"]
    return female_df
>>>>>>> utils
