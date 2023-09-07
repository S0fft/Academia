def func(x):
    return x ** 3 + 4 * x - 6


x0_combined = 1.0
x1_combined = 2.0

x0_iterative = 1.0

epsilon = 0.01


def combined_method(x0, x1, epsilon):
    while True:
        x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        if abs(func(x2)) < epsilon or abs(x2 - x1) < epsilon:
            return x2
        x0 = x1
        x1 = x2


def iterative_method(x0, epsilon):
    max_iterations = 1000
    iteration = 0

    while iteration < max_iterations:
        x1 = x0 - func(x0) / func(x0)
        if abs(func(x1)) < epsilon or abs(x1 - x0) < epsilon:
            return x1
        x0 = x1
        iteration += 1

    raise Exception('Не удалось найти корень в указанном пределе итераций')


root_combined = combined_method(x0_combined, x1_combined, epsilon)

try:
    root_iterative = iterative_method(x0_iterative, epsilon)
except Exception as e:
    root_iterative = None

# Результаты
print('Корень с использованием комбинированного метода:', root_combined)

if root_iterative is not None:
    print('Корень с использованием метода итераций:', root_iterative)
else:
    print('Метод итераций не сошелся к корню')


if abs(func(root_combined)) < epsilon and (root_iterative is None or abs(func(root_iterative)) < epsilon):
    print('\n' 'Сравнение результатов:' '\n' 'Оба метода сошлись к корню')
    print('Значение корня (комбинированный метод):', root_combined)

    if root_iterative is not None:
        print('Значение корня (метод итераций):', root_iterative)
else:
    print('Не удалось достичь заданной точности в обоих методах')
