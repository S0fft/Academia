m = 7
n = 39
X0 = 49
tol = 0.004


def f(x, m, n):
    return n * x ** 2 + m / x


def f_deriv(x, m, n):
    return 2 * n * x - m / x ** 2


def f_second_deriv(x, m, n):
    return 2 * n + 2 * m / x ** 3


def newton_raphson(x0, m, n, tol):
    x = x0
    while True:
        fx = f(x, m, n)
        fprime_x = f_deriv(x, m, n)
        fprimeprime_x = f_second_deriv(x, m, n)
        delta_x = -fprime_x / fprimeprime_x
        x += delta_x
        if abs(delta_x) < tol:
            break
    return x


x_min = newton_raphson(X0, m, n, tol)
print("Minimum coordinates: {:.4f}".format(x_min))
