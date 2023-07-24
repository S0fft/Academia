import numpy as np

a = 8
b = 9
c = 5
x0 = 13
y0 = 2.71
gamma0 = 0.09
gamma_min = 2


def ell_cone(x, y, z):
    return (x*x / a*a) + (y*y / b*b) - (z*z / c*c)


def ell_cone_grad(x, y, z):
    grad_x = 2*x / (a*a)
    grad_y = 2*y / (b*b)
    grad_z = -2*z / (c*c)
    return np.array([grad_x, grad_y, grad_z])


def gradient_descent_var_step(x0, y0, z0, gamma0, gamma_min, max_iter):
    x = np.array([x0, y0, z0])
    gamma = gamma0
    for i in range(max_iter):
        gradient = ell_cone_grad(*x)
        x_next = x - gamma * gradient
        while ell_cone(*x_next) > ell_cone(*x):
            gamma = gamma / 2
            x_next = x - gamma * gradient
            if gamma < gamma_min:
                return x
        x = x_next
        gamma = gamma * 1.01
    return x


x_min = gradient_descent_var_step(x0, y0, 0, gamma0, gamma_min, max_iter=10)
print("Координати мінімуму функції:", x_min)
