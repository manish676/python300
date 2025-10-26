#url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"


import pandas as pd
import numpy as np
from scipy.stats import norm

# Load the Iris dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# sampling 
sample = df["sepal_length"].sample(30, random_state=42)

# Sample statistics
mean = np.mean(sample)
std = sample.std()
n = len(sample)

# confidence interval 
z_value = norm.ppf(0.975)
margin_of_error = z_value * (std / np.sqrt(n))
ci = (mean - margin_of_error, mean + margin_of_error)

print("Sample Mean:", mean)
print("95% Confidence Interval:", ci)