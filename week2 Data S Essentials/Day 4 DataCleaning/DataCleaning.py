# Ex 1
import  pandas as pd
import  numpy as np

# Create a sample dataset
data = {
    "Name": ["Jack","Bob",np.nan, "Manish"],
    "Age": [20, np.nan, 30, 35],
    "Score": [85, 90, np.nan, 88],
}
df = pd.DataFrame(data)
print("Orignal Dataset: \n", df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()

# print("Dataset: \n", df)

df = df.rename(columns={"Name": "Student_Name","Score": "Exam_score"})
print("Dataset: \n", df)