import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = 6
b = 27
c = 81
xmin = -6
xmax = 14
ymin = 8
ymax = 28


def elliptic_cone(xyz):
    x, y, z = xyz
    return (x**2/a**2) + (y**2/b**2) - (z**2/c**2)


def elliptic_cone_with_constraints(xyz, sign=1.0):
    x, y, z = xyz
    return sign * ((x**2/a**2) + (y**2/b**2) - (z**2/c**2))


N = 11
x0 = 0.1 * N
y0 = 0.3 * N
z0 = 0

res = minimize(elliptic_cone, (x0, y0, z0))
print("Безусловный минимум: ", res.fun, " в точке ", res.x)

bounds = ((xmin, xmax), (ymin, ymax), (None, None))
res = minimize(elliptic_cone, (x0, y0, z0), bounds=bounds)
print("Максимальное значение: ", -res.fun, " в точке ", res.x)
res = minimize(elliptic_cone_with_constraints, (x0, y0, z0), bounds=bounds, args=(-1,))
print("Минимальное значение: ", res.fun, " в точке ", res.x)

x = np.linspace(xmin, xmax, 100)
y = np.linspace(ymin, ymax, 100)
X, Y = np.meshgrid(x, y)
Z = np.sqrt((X**2/a**2) + (Y**2/b**2))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

fig, ax = plt.subplots()
ax.set_aspect('equal')
c = ax.contour(X, Y, Z, levels=np.arange(0, 1.5, 0.1))
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()
