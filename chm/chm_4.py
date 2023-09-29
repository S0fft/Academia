import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import minimize_scalar


def func(x):
    return 3 * np.sin(np.exp(x))


a = -2
b = 2
maximum_result = minimize_scalar(lambda x: -func(x), bounds=(a, b))
maximum_x = maximum_result.x
maximum_y = func(maximum_x)

minimum_result = minimize_scalar(func, bounds=(a, b))
minimum_x = minimum_result.x
minimum_y = func(minimum_x)

inflection_x = (minimum_x + maximum_x) / 2
inflection_y = func(inflection_x)

x_nodes = np.array([a, minimum_x, inflection_x, maximum_x, b])
y_nodes = func(x_nodes)

global_interpolation = interp1d(x_nodes, y_nodes, kind='cubic')
x_global = np.linspace(a, b, 1000)

plt.figure(figsize=(8, 4))
plt.plot(x_global, global_interpolation(x_global), label='Глобальна інтерполяція')
plt.plot(x_nodes, y_nodes, 'ro', label='Вузли інтерполяції')
plt.plot(maximum_x, maximum_y, 'go', label='Максимум')
plt.plot(minimum_x, minimum_y, 'bo', label='Мінімум')
plt.plot(inflection_x, inflection_y, 'yo', label='Перегиб')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

x0 = 0.5
y_exact = func(x0)

y_interpolated = global_interpolation(x0)
error_global = abs(y_exact - y_interpolated) / y_exact * 100

print(f'Відносна похибка для глобальної інтерполяції у точці x0={x0}: {error_global:.2f}%')
