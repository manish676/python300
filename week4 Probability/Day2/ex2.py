# EX2 Analyze a Dataset's Distribution

# url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# Load Dataset
local_path = "iris.csv"
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

try:
    df = pd.read_csv(local_path)  # fixed: read_csv
except FileNotFoundError:
    df = pd.read_csv(url)
# Analyse sepal_length 
feature = df["sepal_length"]
print("Skewness:", skew(feature))
print("Kurtosis:", kurtosis(feature)) 

# Visualize Distribution
sns.histplot(feature, kde=True)
plt.title("Sepal Length Distribution")
plt.show()