import matplotlib.pyplot as plt
import  seaborn as sns
import  pandas as pd
import  numpy as np

data = np.random.rand(5, 5)
sns.heatmap(data, annot=True, cmap="coolwarm", annot_kws={"size": 10, "color": "black"})

plt.title("HeatMap")
plt.show()



# matplotlib


# Basic Plot
# x = [1,2,3,4]
# y = [10,20,25,30]
# plt.plot(x,y)
# plt.show()

# Line Plot
# plt.plot([1,2,3], [10,20,30], label="Trend")
# plt.title("Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend()
# plt.show()

# Bar Chat
# categories = ["A","B","C"]
# values = [10,15,7]
# plt.bar(categories,values, color="red")
# plt.title("Bar Chat")
# plt.show()

#Histogram
# dataa = [1,2,2,3,3,3,4,4,4,4]
# plt.hist(dataa, bins=4, color="red", edgecolor="black")
# plt.title("Histogram")
# plt.show()

# Scatter Plot
# x = [1,2,3,4,5]
# y = [10,15,60,50,70]
# plt.scatter(x, y, color="red")
# plt.title("Scatter Plot")
# plt.xlabel("X-axis Label")
# plt.ylabel("Y-axis Lable")
# plt.legend(["Dataset 1"])
# plt.show()

