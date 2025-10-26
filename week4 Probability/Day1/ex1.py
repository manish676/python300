# EX1 Simulated Dice Rolls and Calculating Probabilities

import numpy as np

# Simulate rolling a six-sided die 1000 times
rolls = np.random.randint(1, 7, size=1000)

# Calculate the probability 
P_even = np.sum(rolls % 2 == 0) / len(rolls)
P_greater_then_4 = np.sum(rolls > 4 / len(rolls))

print("P(Even):" , P_even)
print("probability of rolling a number greater than 4:", P_greater_then_4)
