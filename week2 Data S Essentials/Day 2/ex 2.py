# Generated and Filter a Rendom Dataset

import numpy as np

dataset = np.random.randint(1, 51 , size=(5,5))
print("Original: \n",dataset)

# Filter values > 25 and replace woth 0
dataset[dataset > 25 ] = 0
print("Modified Dataset: \n", dataset)

# Caluculate summery state
print("Sum: ", np.sum(dataset))
print("Mean:", dataset )
print("Stander Deviation: ", np.std(dataset))