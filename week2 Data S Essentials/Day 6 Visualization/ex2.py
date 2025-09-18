# Create a Heatmap with Seaborn
#https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Select only numeric columns
numeric_df = df.select_dtypes(include=["float64", "int64"])

# Calculate correlation matrix
correlation_matrix = numeric_df.corr()

# Plot heatmap
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", annot_kws={"size": 10, "color": "black"})

plt.title("Correlation Heatmap")
plt.show()
