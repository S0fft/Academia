import numpy as np

lambda_rate = 4.75
mu_rate = 2.79
n = 5
m = 4

states = n + m + 1


def calculate_p0(rho, n, m):
    sum1 = sum(rho**k / np.math.factorial(k) for k in range(n + 1))
    sum2 = (rho**n / np.math.factorial(n)) * sum(rho**(k - n) / n**(k - n) for k in range(n + 1, n + m + 1))
    return 1 / (sum1 + sum2)


rho = lambda_rate / mu_rate
p0 = calculate_p0(rho, n, m)
stationary_probs = []

for k in range(states):
    if k <= n:
        pk = (rho**k / np.math.factorial(k)) * p0
    else:
        pk = (rho**k / (np.math.factorial(n) * n**(k - n))) * p0
    stationary_probs.append(pk)

print("Стаціонарні ймовірності p_k:")

for k, pk in enumerate(stationary_probs):
    print(f"p_{k} = {pk:.6f}")

print(f"Сума ймовірностей: {sum(stationary_probs):.6f}")
