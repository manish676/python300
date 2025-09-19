# Calculate Determinant and inverse of matrix
import numpy as np

A = np.array([[1, 2, 3],
              [0, 4, 5],
              [1, 0, 6]])   # determinant ≠ 0

determinant = np.linalg.det(A)
inverse = np.linalg.inv(A)

print("Determinant: ", determinant)
print("Inverse:\n", inverse)
