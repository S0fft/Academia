m = 37
n = 36
c = 39
a = -942
b = 1086    
epsilon = 0.4


def f(x):
    return m * x ** 2 + n * x + c


def bolzano(a, b, epsilon):
    while abs(b-a) > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * (c) < 0:
            b = c
        else:
            a = c
    return (a+b)/2


min_x = bolzano(a, b, epsilon)
min_y = f(min_x)

print("Minimum coordinates: ({:.2f}, {:.2f})".format(min_x, min_y))
