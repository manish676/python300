# EX1 Plot and Explore Various Distributions

import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson, uniform
import seaborn as sns

# Gaussian Distribution
x = np.linspace(-10, 10, 1000)
plt.plot(x, norm.pdf(x, 0, 1), label='Gaussian Distribution')
# Binomial Distribution
n, p = 10, 0.5 
x = np.arange(0, n+1)
plt.plot(x, binom.pmf(x, n, p), 'o', label='Binomial Distribution')

# Poisson Distribution
lam  = 3 
x = np.arange(0, 15)
plt.bar(x, poisson.pmf(x, lam), label='Poisson (l = 3)')

# uniform Distribution
x = np.random.uniform(low=0.0, high=10.0, size=1000)
sns.histplot(x, kde=True, label='Uniform Distribution', color="red")

plt.title("probability distributions")
plt.legend()
plt.show()
