import  numpy as np

A = np.array([[2,3], [1,4]])
determinant = np.linalg.det(A)
# print("Determinat: ",determinant)

inverse = np.linalg.inv(A)
# print("Inverse of A: \n",inverse)


eigenValues, eigneVectors = np.linalg.eig(A)
print("Eigenval\n", eigenValues)
print("EigenVectors\n", eigneVectors)

B = np.array([[4,2], [1,1]])
eigval, eigvec = np.linalg.eig(B)
print("Eigval: ",eigval)
print("EigVect:\n", eigvec)


