#https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd

# Load Dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Explore the structure
# print("First 5 rows: \n ", df.head())
# print("Lats 5 rows: \n", df.tail())
# print(df.describe())

print(df.columns)
selected_columns = df[["species","sepal_length"]]
# print("My selected colum is: ",selected_columns)

filtered_rows = df[(df["sepal_length"] > 5.0) & (df["species"] == "setosa")]
print("Filtered Rows:\n ",filtered_rows)