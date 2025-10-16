def simple_iteration_method(x0, y0, epsilon):
    x = x0
    y = y0
    iteration = 0

    while True:
        x_new = x / (x**2 + y**2) + 0.4
        y_new = (1 - y) / (x**2 + y**2) + 1

        if abs(x_new - x) < epsilon and abs(y_new - y) < epsilon:
            break

        x = x_new
        y = y_new
        iteration += 1

    return x, y, iteration


x0 = 1
y0 = 1
epsilon = 1e-4

result_x, result_y, iterations = simple_iteration_method(x0, y0, epsilon)
print(f"Рішення: x = {result_x:.1f}, y = {result_y:.1f}")
print(f"Кількість ітерацій: {iterations}")
