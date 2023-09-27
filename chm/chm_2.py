def simple_iteration_solver(B, c, accuracy=0.001, max_iterations=500):
    n = len(c)
    x = [0.0] * n
    for i in range(max_iterations):
        x_new = [0.0] * n
        for j in range(n):
            sum_ = sum(B[j][k] * x[k] for k in range(n) if k != j)
            x_new[j] = (c[j] - sum_) / B[j][j]
        if all(abs(x_new[j] - x[j]) < accuracy for j in range(n)):
            return x_new
        x = x_new
    return x


B = [
    [3.5, -2.3, 3.7],
    [-2.8, 3.4, 5.8],
    [-1.2, -7.3, 2.3]
]
c = [4.5, -3.2, 5.6]

solution = simple_iteration_solver(B, c, accuracy=0.001)
print("Рішення:", solution)
