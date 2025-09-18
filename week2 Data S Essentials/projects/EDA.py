import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Titanic Data Set
url = "https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv"
df = pd.read_csv(url)

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Remove duplicates
df = df.drop_duplicates()

# Filter Data: Passengers in first class
first_class = df[df["Pclass"] == 1]
print("First Class Passengers: \n", first_class.head())  # print only first 5

# Task 2 Generate Visualizations to Illustrate Key insights

# Bar Chart: Survival rate by class
# survival_by_class = df.groupby("Pclass")["Survived"].mean()
# survival_by_class.plot(kind="bar", color="skyblue")
# plt.title("Survival Rate by Class")
# plt.ylabel("Survival rate")
# plt.show()

# Histogram
# sns.histplot(df["Age"], kde=True, bins=20, color="purple")
# plt.title("Age Distrubution")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()

# Scatter Plot: Age vs Fare
# plt.scatter(df["Age"], df["Fare"], alpha=0.5, color="green")
# plt.ylabel("Age")
# plt.xlabel("Fare")
# plt.title("Age vs Fare")
# plt.show()

# Task 3 identify and interpret Patterns or Anomalies
# Task 4 Summarize Findings in a Report

