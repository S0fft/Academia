import matplotlib.pyplot as plt


x0 = 1
y0 = 1
a = 2
epsilon = 0.01


def f(x, y):
    return (2 * x * y) / (3 * x**2 - y**2)


def find_next_step(x, y, h, epsilon):
    while True:
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        delta = abs(k2 - k1) / 15.0

        if delta < epsilon / 2:
            return h
        else:
            h = h / 2


x_values = [x0]
y_values = [y0]

x = x0
y = y0
h = 0.1

while x < a:
    h = find_next_step(x, y, h, epsilon)
    k1 = h * f(x, y)
    k2 = h * f(x + h / 2, y + k1 / 2)
    y_new = y + k2
    x_new = x + h

    x_values.append(x_new)
    y_values.append(y_new)

    x = x_new
    y = y_new


plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Рішення методу Ейлера з автоматичним вибором кроку')
plt.grid(True)
plt.show()
