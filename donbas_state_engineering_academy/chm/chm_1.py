def f(x):
    return x**3 + 4*x - 6


def combined_method(epsilon):
    root = 0
    prev_root = root - 2 * epsilon
    while abs(f(root)) >= epsilon and abs(root - prev_root) >= epsilon:
        prev_root = root
        root = prev_root - f(prev_root) * (2 * epsilon)
    return root


def iterative_method(epsilon):
    x = 0
    while abs(f(x)) >= epsilon:
        x = x - f(x) * epsilon
    return x


epsilon = 0.01
root_combined = combined_method(epsilon)
root_iterative = iterative_method(epsilon)

print("Корінь (комбінований метод):", round(root_combined, 3))
print("Корінь (ітераційний метод):", round(root_iterative, 3))
