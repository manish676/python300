import numpy as np

def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)  # number of training examples
    for _ in range(iterations):
        predictions = np.dot(X, theta)
        error = predictions - y
        gradients = (1/m) * np.dot(X.T, error)
        theta -= learning_rate * gradients
    return theta

# Sample Data
X = np.array([[1,1], [1,2], [1,3]])   # includes bias term
y = np.array([2, 2.5, 3.5])
theta = np.array([0.1, 0.1])
learning_rate = 0.1
iterations = 1000

# Perform gradient descent
optimized_theta = gradient_descent(X, y, theta, learning_rate, iterations)
print("Optimized Parameters: ", optimized_theta)
