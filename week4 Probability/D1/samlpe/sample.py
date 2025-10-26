# Basic Probability Concepts 

# . Sample Sapce andEvents 
# Sample Space: The set of all possible outcomes of a rendom expriment
# Events : A subset of the sample space 

    # Conditional Probability 
# . The probability of an event A occurring, given that B has occurred is denoted as P(A|B)

  # independent 
  # Two events A and B are independet if 
    # p(A/B) = P(A) and P(B)
    
  # Random Variables
# A random variable is a function that assigns a real number to each outcome in the sample space
# Types of Random Variables 
  # Discrete Random Variables: Take on a countable number of distinct values 
  # Continuous Random Variables: Take on an infinite number of possible values within a given range
  
 # sample 1 
# from itertools import product

# # sample space of a dice roll 
# sample_space =  list(range(1, 7))

# # Probability of rolling an even number 
# even_numbers = [2,4,6]
# P_even = len(even_numbers) / len(sample_space)
# print("P(Even):", P_even)

# sample 2 
import numpy as np

# Random Variable: die roll
outcomes = np.array([1, 2, 3, 4, 5, 6], dtype=float)
probabilities = np.array([1/6] * 6, dtype=float)

# Expected Value
expectation = np.sum(outcomes * probabilities)
print("Expected Value of a fair six-sided die roll:", expectation)

# Variance (weighted): Var(X) = E[X^2] - (E[X])^2
EX2 = np.sum((outcomes**2) * probabilities)
variance = EX2 - expectation**2

std_dev = np.sqrt(variance)

print("Variance:", variance)
print("Standard Deviation:", std_dev)
