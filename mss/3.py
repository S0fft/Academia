import math

lambda_ = 4.75
mu = 2.79
n = 4
max_k = 10


def calculate_probabilities():

    p = [0.0] * (max_k + 1)

    p[0] = 1.0
    for k in range(1, max_k + 1):
        p[k] = (lambda_ / (k * mu)) * p[k - 1]

    normalization_factor = sum(p)
    p = [prob / normalization_factor for prob in p]

    return p


probabilities = calculate_probabilities()

s_10 = sum(probabilities[:11])

p_n = probabilities[n]
m_s = 1.0 - p_n

# Output results
print("Probabilities p_k (k = 0, ..., 10):")
for k in range(max_k + 1):
    print(f"p[{k}] = {probabilities[k]:.6f}")

print(f"\nSum of probabilities s_10: {s_10:.6f}")
print(f"\np_n (n = 4): {p_n:.6f}")
print(f"Relative throughput m_s: {m_s:.6f}")


def factorial(num):
    """Calculate the factorial of a number."""
    result = 1.0
    for i in range(1, num + 1):
        result *= i
    return result


def main():
    lambda_ = 4.75
    mu = 2.79
    v = 4.75
    n = 4

    p = [0.0] * (int(v) + 1)

    sum_ = 0.0
    for k in range(n + 1):
        sum_ += (lambda_ / mu) ** k / factorial(k)
    for k in range(n + 1, int(v) + 1):
        sum_ += (lambda_ / mu) ** k / (factorial(n) * (n ** (k - n)))
    p[0] = 1.0 / sum_

    for k in range(1, int(v) + 1):
        if k <= n:
            p[k] = p[0] * (lambda_ / mu) ** k / factorial(k)
        else:
            p[k] = p[0] * (lambda_ / mu) ** k / (factorial(n) * (n ** (k - n)))

    print("Probabilities p_k:")
    for k in range(int(v) + 1):
        print(f"p[{k}] = {p[k]:.6f}")

    s_v = sum(p)
    print(f"\nSum of probabilities (s_v): {s_v:.6f}")

    p_v = p[int(v)]
    print(f"\nBlocking probability (p_v): {p_v:.6f}")

    m_s = lambda_ * (1.0 - p_v)
    print(f"\nRelative throughput (m_s): {m_s:.6f}")


if __name__ == "__main__":
    main()
