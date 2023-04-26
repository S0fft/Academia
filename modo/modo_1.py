m = int(input("m: "))
n = int(input("n: "))
c = float(input("c: "))
epsilon = float(input("epsilon: "))
a = int(input("a: "))
b = int(input("b: "))
alpha = float(input("alpha: "))

f1p = alpha * a + (1 - alpha) * b
f1 = (m * pow(f1p, 2)) + n * f1p + c
f2 = a * (m * (pow(a, 2)) + n * a + c)
f3 = (a - alpha) * (m * (pow(b, 2)) + n * b + c)

if f1 <= (round(f2 + f3, -3)):
    print("Функція опукла")
else:
    print("Функція не опукла")

mx = 1
x1 = 0.618 * a + 0.382 * b
x2 = 0.382 * a + 0.618

fx1 = m * (pow(x1, 2)) + n * x1 + c
fx2 = m * (pow(x2, 2)) + n * x2 + c

while b-a > epsilon:
    if fx1 <= fx2:
        b = x2
        x2 = x1
        x1 = 0.618 * a + 0.382 * b
        fx2 = fx1
        fx1 = m * (pow(x1, 2)) + n * x1 + c
        mx = mx + 1
        print(a, b, a-b, x1, x2, fx1, fx2)
    else:
        a = x1
        x1 = x2
        x2 = 0.382 * a + 0.618 * b
        fx1 = fx2
        fx2 = m * (pow(x2, 2)) + n * x2 + c
        mx = mx + 1
        print(a, b, a - b, x1, x2, fx1, fx2)

x = (a + b) / 2
fx = m * (pow(x, 2)) + n * x + c
print(fx, x)
