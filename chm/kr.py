def f1(x1, x2):
    return x1 - 0.2 * x1**2 + 0.1 * x1 * x2 - 1


def f2(x1, x2):
    return 0.4 * x1**2 + x2 - 0.2 * x1 * x2 - 2


def phi1(x1, x2, h1):
    return x1 + h1 * f1(x1, x2)


def phi2(x1, x2, h2):
    return x2 + h2 * f2(x1, x2)


def simple_iteration_method(x1, x2, h1, h2, e=0.2, max_iterations=1000000):
    for i in range(max_iterations):
        x1_new = phi1(x1, x2, h1)
        x2_new = phi2(x1_new, x2, h2)

        if max(abs(x1_new - x1), abs(x2_new - x2)) < e:
            print("Кількість ітерацій:", i + 1)
            return x1_new, x2_new

        x1, x2 = x1_new, x2_new

    raise ValueError("Метод простої ітерації не сходиться")


initial_point = (1, 1)
h1 = -0.3
h2 = -0.3

solution = simple_iteration_method(initial_point[0], initial_point[1], h1, h2)

print("Розв'язання системи рівнянь:", solution)
