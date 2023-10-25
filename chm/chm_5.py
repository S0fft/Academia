import math


def f(x):
    return math.log(abs(math.sqrt(x**2 + 1) + x))


def right_triangle_method(a, b, n):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        x_i = a + i * h
        x_i1 = a + (i + 1) * h
        integral += f(x_i1)
    integral *= h
    return integral


def simpson_method(a, b, n):
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x_i)
        else:
            integral += 4 * f(x_i)
    integral *= h / 3
    return integral


desired_order = 0.01
desired_error_estimate = 0.0001

n = 1

while True:
    n *= 2
    integral_right_triangle = right_triangle_method(0.6, 1.5, n)

    integral_simpson = simpson_method(0.6, 1.5, n)
    integral_simpson_double_count = simpson_method(0.6, 1.5, 2 * n)

    error_right_triangle = abs(integral_right_triangle - integral_simpson) / 15
    error_simpson = abs(integral_simpson - integral_simpson_double_count) / 15

    if error_right_triangle < desired_order and error_simpson < desired_order:
        break

print("Інтеграл методом правих прямих трикутників:", integral_right_triangle)
print("Похибка методу Сімпсона з подвійним перерахунком:", error_simpson)
print("Кількість розбиття:", n)
print("Похибка методу правих прямих трикутників:", error_right_triangle)
