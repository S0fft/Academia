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

    raise Exception('Не вдалося знайти коріння у вказаній межі ітерацій')


root_combined = combined_method(x0_combined, x1_combined, epsilon)

try:
    root_iterative = iterative_method(x0_iterative, epsilon)
except Exception as e:
    root_iterative = None

# Результаты
print('Корінь з використанням комбінованого методу:', root_combined)

if root_iterative is not None:
    print('Корінь із використанням методу ітерацій:', root_iterative)
else:
    print('Метод ітерацій не зійшовся до кореня')


if abs(func(root_combined)) < epsilon and (root_iterative is None or abs(func(root_iterative)) < epsilon):
    print('\n' 'Порівняння результатів:' '\n' 'Обидва методи зійшлися до кореня')
    print('Значення кореня (комбінований метод):', root_combined)

    if root_iterative is not None:
        print('Значення кореня (метод ітерацій):', root_iterative)
else:
    print('Не вдалося досягти заданої точності в обох методах')
