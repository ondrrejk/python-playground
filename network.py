import numpy as np

# activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    return x * (1 - x)

# training data (XOR)
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

# initialize weights
np.random.seed(0)
W1 = np.random.randn(2, 2)
W2 = np.random.randn(2, 1)

lr = 0.1

for epoch in range(10000):
    # forward
    z1 = X @ W1
    a1 = sigmoid(z1)
    z2 = a1 @ W2
    y_hat = sigmoid(z2)

    # backprop
    error = y - y_hat
    d2 = error * sigmoid_deriv(y_hat)
    d1 = d2 @ W2.T * sigmoid_deriv(a1)

    # update
    W2 += a1.T @ d2 * lr
    W1 += X.T @ d1 * lr

print("Predictions:")
print(y_hat)
