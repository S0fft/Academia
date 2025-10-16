import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal

K1 = 17
K2 = 0.1
K3 = 1
T1 = 0.002
T2 = 0.4

a0 = T1 * T2 - K2 * K3 * T1
a1 = T1 + T2 - K2 * K3
a2 = 1
a3 = K1 * K3

denom = [a0, a1, a2, a3]
b0 = -K2 * T1 * T2
b1 = -K2 * T1 - K2 * T2
b2 = -K2
b3 = K1 * T2
b4 = K1
numerator = [b0, b1, b2, b3, b4]

system = signal.TransferFunction(numerator, denom)


def is_hurwitz_stable_desc(coeffs):
    a0, a1, a2, a3 = coeffs
    return (a0 > 0) and (a1 > 0) and (a3 > 0) and ((a1 * a2 - a0 * a3) > 0)


stable_hurwitz = is_hurwitz_stable_desc(denom)
delta1 = denom[1]
delta2 = denom[1]*denom[2] - denom[0]*denom[3]
print(f'Критерій Гурвіца: {delta1}, {delta2}] -> Система стійка: {stable_hurwitz}')


def routh_criterion(coeffs):
    n = len(coeffs)
    coeffs = coeffs.copy()

    if coeffs[0] == 0:
        coeffs[0] = 1e-6

    cols = (n + 1) // 2

    R = np.zeros((n, cols))
    R[0, :len(coeffs[::2])] = coeffs[::2]
    R[1, :len(coeffs[1::2])] = coeffs[1::2]

    for i in range(2, n):
        for j in range(cols - 1):
            if abs(R[i - 1, 0]) < 1e-6:
                R[i - 1, 0] = 1e-6
            R[i, j] = (-1 / R[i - 1, 0]) * np.linalg.det(
                [[R[i - 2, 0], R[i - 2, j + 1]],
                 [R[i - 1, 0], R[i - 1, j + 1]]]
            )
    return np.all(R[:, 0] > 0), R[:, 0]


stable_routh, routh_first_column = routh_criterion(denom)
print(f'Критерій Рауса: {routh_first_column} -> Система стійка: {stable_routh}')

w = np.logspace(-3, 6, 2000)
s = 1j * w

denom_norm = np.array(denom) / denom[0]
char_poly = np.polyval(denom_norm, s)

phase = np.unwrap(np.angle(char_poly))
phase_change = phase[-1] - phase[0]

if phase_change < 0:
    phase += 2 * np.pi
    phase_change = phase[-1] - phase[0]

expected_phase_change = (len(denom) - 1) * np.pi / 2
stable_mikhailov = np.isclose(phase_change, expected_phase_change, atol=0.2) and np.all(np.diff(phase) >= -1e-3)

plt.figure(figsize=(6, 6))
plt.plot(char_poly.real, char_poly.imag, label='Графік Михайлова')

plt.xlabel('Re')
plt.ylabel('Im')

plt.axhline(0, color='black', linestyle='--')
plt.axvline(0, color='black', linestyle='--')

plt.legend()
plt.title('Критерій Михайлова')

plt.grid()
plt.show()

print(f'Система {"стійка" if stable_mikhailov else "нестійка"} за критерієм Михайлова')

w_freq, h = signal.freqresp(system)

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
print(f'Система {"стійка" if stable_nyquist else "нестійка"} за критерієм Найквіста')
