# What is numpy?
# NumPy is a powerful library for numerical computing in Python. It provides support for arrays, matrices, and a wide range of mathematical functions to operate on these data structures efficiently.

# What use NumPpy in AI?
# NumPy is widely used in AI and machine learning for several reasons:
# 1. Efficient Data Handling: NumPy arrays are more efficient than Python lists for numerical data, allowing for faster computations.
# 2. Mathematical Operations: NumPy provides a wide range of mathematical functions that are essential
#    for machine learning algorithms, such as linear algebra operations, statistical functions, and random number generation.
# 3. Integration with Other Libraries: Many popular AI and machine learning libraries, such as TensorFlow, PyTorch, and scikit-learn, are built on top of NumPy, making it a fundamental tool for AI development.

# importing NumPy
import numpy as np

arr = np.array([1,2,3,4])

zeroes =np.zeros((3,3,))

ones = np.ones((2,4))
#print(ones)

range_array = np.arange(1, 20, 3)
# print(range_array)

linspace_array = np.linspace(0, 1, 5)
# print(linspace_array)


# Manipulating Arrays

# arr = np.array([1,2,3,4,5,6])
# reshape = arr.reshape(2,3)
# print(reshape)

# arr = np.array([1,2,3])
# expanded = arr[:, np.newaxis]
# print(expanded)

# Element-wise Operations
a = np.array([1,2,3])
b = np.array([4,5,6])
# print(a+b)

# Mathematical Operations
# arr = np.array([4,16,25])
# print(np.sum(arr))
# print((np.mean(arr)))

