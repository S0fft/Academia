a = 17
b = 26
c = 11
xo = -1
yo = 3
gamma = 0.05
eps = 0.0001


def elliptic_cone(x, y, z, a, b, c):
    return x**2/a**2 + y**2/b**2 - z**2/c**2


def coordinate_descent(x0, y0, z0, a, b, c, gamma, eps):
    x, y, z = x0, y0, z0
    fx = elliptic_cone(x, y, z, a, b, c)

    while True:
        x_new = x - gamma * (2*x/a**2)
        y_new = y - gamma * (2*y/b**2)
        z_new = z + gamma * (2*z/c**2)
        fx_new = elliptic_cone(x_new, y_new, z_new, a, b, c)
        if abs(fx_new - fx) < eps:
            break
        x, y, z = x_new, y_new, z_new
        fx = fx_new

    return x, y, z, fx


x_min, y_min, z_min, f_min = coordinate_descent(xo, yo, 0, a, b, c, gamma, eps)

# print(f"Minimum value is {f_min} at coordinates ({x_min}, {y_min}, {z_min})")
print("Minimum value is {:.4f} at coordinates ({}, {}, {})".format(f_min, x_min, y_min, z_min))
