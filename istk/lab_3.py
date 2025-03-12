import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal

K1 = 17
K2 = 0.1
K3 = 1
T1 = 0.002
T2 = 0.4

numerator = [K1 + K2]
denominator = [T1 * T2, (T1 + T2), 1, (K1 + K2) * (-K3)]
system = signal.TransferFunction(numerator, denominator)


def hurwitz_criterion(coeffs):
    n = len(coeffs)
    hurwitz_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n - i):
            hurwitz_matrix[j, i] = coeffs[i + j] if (i + j) < n else 0

    det_values = [np.linalg.det(hurwitz_matrix[:i+1, :i+1]) for i in range(n)]
    return det_values


hurwitz_dets = hurwitz_criterion(denominator)
stable_hurwitz = all(d > 0 for d in hurwitz_dets)

print(f'Критерій Гурвіца: {hurwitz_dets} -> Система стійка: {stable_hurwitz}')


def routh_criterion(coeffs):
    n = len(coeffs)
    if coeffs[0] == 0:
        coeffs[0] = 1e-6
    R = np.zeros((n, (n + 1) // 2))

    R[0, :len(coeffs[::2])] = coeffs[::2]
    R[1, :len(coeffs[1::2])] = coeffs[1::2]

    for i in range(2, n):
        for j in range(R.shape[1] - 1):
            if R[i - 1, 0] == 0:
                R[i - 1, 0] = 1e-6
            R[i, j] = (-1 / R[i - 1, 0]) * np.linalg.det(
                [[R[i - 2, 0], R[i - 2, j + 1]],
                 [R[i - 1, 0], R[i - 1, j + 1]]]
            )
    return np.all(R[:, 0] > 0), R[:, 0]


stable_routh, routh_first_column = routh_criterion(denominator)
print(f'Критерій Рауса: {routh_first_column} -> Система стійка: {stable_routh}')

w = np.linspace(0, 10, 500)
char_poly_values = sum([denominator[i] * (1j * w) ** (len(denominator) - 1 - i) for i in range(len(denominator))])
real_part = char_poly_values.real
imag_part = char_poly_values.imag

plt.figure(figsize=(6, 6))
plt.plot(real_part, imag_part, label='Графік Михайлова')
plt.xlabel('Re')
plt.ylabel('Im')
plt.axhline(0, color='black', linestyle='--')
plt.axvline(0, color='black', linestyle='--')
plt.legend()
plt.title('Критерій Михайлова')
plt.grid()
plt.show()

stable_mikhailov = np.all(real_part >= 0)
print(f'Система {"стійка" if stable_mikhailov else "не стійка"} за критерієм Михайлова')

w, h = signal.freqresp(system)
plt.figure(figsize=(6, 6))
plt.plot(h.real, h.imag, label='Діаграма Найквіста')
plt.plot(h.real, -h.imag, linestyle='dashed', color='gray')
plt.axhline(0, color='black', linestyle='--')
plt.axvline(-1, color='red', linestyle='--', label='Точка -1')
plt.legend()
plt.title('Критерій Найквіста')
plt.grid()
plt.show()

stable_nyquist = np.all(h.real >= 0)
print(f'Система {"стійка" if stable_nyquist else "не стійка"} за критерієм Найквіста')
