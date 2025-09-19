import  numpy as np

A = np.array([[2,3], [1,4]])
determinant = np.linalg.det(A)
print("Determinat: ",determinant)

# Determinants and inverse of a Matrix

inverse = np.linalg.inv(A)
print("Inverse of A: \n",inverse)

