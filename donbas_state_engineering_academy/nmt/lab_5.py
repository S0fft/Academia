import matplotlib.pyplot as plt
import numpy as np
from scipy.special import expit
from sklearn.preprocessing import Binarizer


def activation_function(y):
    return np.maximum(y, 0)


def find_maximum(x, epsilon=0.1, max_iter=100):
    n = len(x)
    W = np.full((n, n), -epsilon)
    np.fill_diagonal(W, 1)

    y = np.array(x, dtype=float)

    for _ in range(max_iter):
        y_new = activation_function(y - epsilon * (np.sum(y) - y))

        if np.allclose(y, y_new, atol=1e-6):
            break
        y = y_new

    return y


x = np.random.randint(1, 10, size=5)
y_out = find_maximum(x)

max_value = np.max(y_out)
max_index = np.argmax(y_out)


print("Вхідні сигнали:", x)
print(f"Вихідні сигнали нейронів: {y_out}")
print(f"Максимальне значення: {max_value} (індекс: {max_index})")

X_scaled = np.random.rand(5, 5)

binarizer = Binarizer(threshold=0.5)
X_binary = binarizer.fit_transform(X_scaled)

patterns = X_binary[:5, :5]


class HopfieldNN:
    def __init__(self, size):
        self.size = size
        self.weights = np.zeros((size, size))

    def train(self, patterns):
        for p in patterns:
            self.weights += np.outer(p, p)
        np.fill_diagonal(self.weights, 0)
        self.weights /= len(patterns)

    def recall(self, pattern, steps=10):
        for _ in range(steps):
            pattern = np.sign(np.dot(self.weights, pattern))
        return pattern


hopfield = HopfieldNN(size=5)
hopfield.train(patterns)

input_pattern = patterns[0]
output_pattern = hopfield.recall(input_pattern)

print("Вхідний образ:", input_pattern)
print("Відновлений образ:", output_pattern)
