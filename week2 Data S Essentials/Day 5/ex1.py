# Group Data by a categorical column

import  pandas as pd

data = {
    "Class": ["A","B","A","B","C","C"],
    "Score": [98,99,78,86,76,88],
    "Age": [23,34,24,25,27,21]
}

df = pd.DataFrame(data)

print("Original Dataset \n", df)

grouped = df.groupby("Class").mean()
print(grouped)