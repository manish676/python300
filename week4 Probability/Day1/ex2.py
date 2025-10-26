# EX2 Create and Analyze Random Variables

import matplotlib.pyplot as plt
from scipy.stats import uniform  
import numpy as np
import random

# Dsicreate random varibale: Dice roll 
# outcomes = [1, 2, 3, 4, 5, 6]
# probabilities = [1/6] * 6 
# plt.bar(outcomes, probabilities, color="blue", alpha=0.7)
# plt.title("PMF of a Dice Roll")
# plt.xlabel("Outcomes")
# plt.ylabel("Probabilities")
# plt.show()

# continuous random variable: Uniform distribution between 0 and 1
x = np.linspace(0, 1, 100)
pdf = uniform.pdf(x, loc=0, scale=1)
plt.plot(x, pdf, color="red")
plt.title("PDF of Unifrom(0.1)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
