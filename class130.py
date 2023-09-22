import pandas as pd
import csv

df = pd.read_csv("merged_stars.csv")
print(df)

df.columns
df.drop(['Unnamed: 0', "Unnamed: 5", "Name.1", "Distance.1", "Mass.1", "Radius.1"], axis=1, inplace = True)
print(df)