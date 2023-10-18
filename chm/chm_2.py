def sol(A, b):
    n = len(A)

    for i in range(n):
        max_row = max(range(i, n), key=lambda i: abs(A[i][i]))
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        elem = A[i][i]
        for col in range(i, n):
            A[i][col] /= elem
        b[i] /= elem
        for row in range(n):
            if row != i:
                factor = A[row][i]
                for col in range(i, n):
                    A[row][col] -= factor * A[i][col]
                b[row] -= factor * b[i]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]

    return x


A = [[3.5, 2.3, -3.7],
     [2.8, 3.4, 5.8],
     [1.2, 7.3, -2.3]]

b = [4.5, -3.2, 5.6]

x = sol(A, b)

print("Відповідь:", x)
