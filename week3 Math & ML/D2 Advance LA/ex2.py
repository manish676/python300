#2 Compute Eigenvalues and Eigenvectors

import  numpy as np

A = np.array([[4, -2],[1, 1]])
eigvals, egivec = np.linalg.eig(A)

print("EigentValues",eigvals)
print("EignetVectors:\n",egivec)