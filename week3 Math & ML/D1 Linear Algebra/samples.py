import numpy as np

A = np.array([[1,2], [3,4]])
B = np.array([[5,6],[7,8]])

# print("Addition: \n", A +B)
# print("Subtraction: \n", A - B)

C = 2 * A
# print("Scalar Multiplication \n", C)

result = np.dot(A, C)
# print("Matrix Multiplication \n",result)

# Spcial Matrices
I = np.eye(3)
# print("Identity Matrix \n", I)

Z = np.zeros((2,3))
print("Zero Matrix \n", Z)

D = np.diag([1,2,3])
print("Diagonal Matrix",D)
