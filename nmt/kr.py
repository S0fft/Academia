import numpy as np


def activation_function(y):
    return np.maximum(y, 0)


def find_maximum(x, epsilon=0.2, max_iter=100):
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


x = np.array([7, 2, 4], dtype=float)
y_out = find_maximum(x)

max_value = np.max(y_out)
max_index = np.argmax(y_out)


print("Входные сигналы:", x)
print(f"Выходные сигналы нейронов: {y_out}")
print(f"Максимальное значение: {max_value} (индекс: {max_index})")
