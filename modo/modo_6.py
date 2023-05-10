from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt


def elliptic_cone(point, a, b, c):
    x, y, z = point
    return (x**2 / a**2) + (y**2 / b**2) + (z**2 / abs(c)**2)


a = 6
b = 27
c = -5
xmin = -6
xmax = 14
ymin = 8
ymax = 28

x0 = 0.1 * (11)
y0 = 0.3 * (11)

bounds = [(xmin, xmax), (ymin, ymax), (-np.inf, 0)]

res = minimize(elliptic_cone, (x0, y0, c/2), args=(a, b, c), bounds=bounds)

print("Безумовний мінімум:", res.fun)
print("Точка мінімуму:", res.x)

x_range = np.linspace(xmin, xmax, 100)
y_range = np.linspace(ymin, ymax, 100)
x, y = np.meshgrid(x_range, y_range)
z = elliptic_cone((x, y, c/2), a, b, c)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title('Поверхня відгуку')
plt.show()

fig, ax = plt.subplots()
levels = np.linspace(res.fun, 1, 10)
cp = ax.contour(x, y, z, levels=levels)
ax.plot(res.x[0], res.x[1], 'r*', markersize=10)
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.title('Лінії рівня')
plt.show()
