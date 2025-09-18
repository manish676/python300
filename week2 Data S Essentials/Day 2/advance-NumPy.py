# 1 What is Broadcasting?
 #. Dimensions are aligned from the right
 #. A dimensions is compatible if;
    #. it matches the other array's dimension
    #. One of the dimensions is 1

import numpy as np

# arr = np.array([1,2,3])
# print(arr + 10)

# matrix = np.array([[1,2,3], [4,5,6]])
# vector = np.array([1,0,1])
# print(matrix+vector)

# Aggeregations Funtions
 #. Aggregations Funtions compute summary statistics for arrays

# arr= np.array([[1,2,3], [4,5,6]])
# print("Sum: ", np.sum(arr))
# print("mean:", np.mean(arr))
# print("Max: ", np.max(arr))
# print("Min: ", np.min(arr))
# print("Standrade Deviations", np.std(arr))
# print("Sum along rows: ", np.sum(arr, axis=1))
# print("Sum along columns: ", np.sum(arr, axis=0))

# Booling indexing for filtring

rendom_array = np.random.rand(3, 3)
print("Random Array: \n", rendom_array)

rendom_integers = np.random.randint(0, 10, size=(2,3))
print("Rendom Integers: \n", rendom_integers)