import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal

K1 = 17
K2 = 0.1
K3 = 1
T1 = 0.002
T2 = 0.4

K = K1 + K3

num = [K * K2]
den = [T1 * T2, (T1 + T2), 1]

system = signal.TransferFunction(num, den)

hurwitz_matrix = np.array([
    [den[1], den[2], 0],
    [den[0], den[1], 0],
    [0, den[0], den[2]]
])
det1 = hurwitz_matrix[0, 0]
det2 = np.linalg.det(hurwitz_matrix[:2, :2])
det3 = np.linalg.det(hurwitz_matrix)

stable_hurwitz = det1 > 0 and det2 > 0 and det3 > 0
print(f'Критерій Гурвіца: дет1 = {det1:.3f}, дет2 = {det2:.3f}, дет3 = {det3:.3f} -> Система стійка: {stable_hurwitz}')


def routh_array(coeffs):
    n = len(coeffs)
    R = np.zeros((n, (n + 1) // 2))
    R[0, :len(coeffs[::2])] = coeffs[::2]
    R[1, :len(coeffs[1::2])] = coeffs[1::2]

    for i in range(2, n):
        for j in range(R.shape[1] - 1):
            R[i, j] = (-1 / R[i - 1, 0]) * np.linalg.det(
                [[R[i - 2, 0], R[i - 2, j + 1]],
                 [R[i - 1, 0], R[i - 1, j + 1]]]
            ) if R[i - 1, 0] != 0 else 0
    return R


routh = routh_array(den)
routh_str = ", ".join([f"{r:.3f}" for r in routh[:, 0]])
stable_routh = np.all(routh[:, 0] > 0)
print(f'Критерій Рауса: {routh_str} -> Система стійка: {stable_routh}')

w = np.linspace(0, 10, 500)
real_part = sum([den[i] * (1j * w) ** (len(den) - 1 - i) for i in range(len(den))]).real
imag_part = sum([den[i] * (1j * w) ** (len(den) - 1 - i) for i in range(len(den))]).imag

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
