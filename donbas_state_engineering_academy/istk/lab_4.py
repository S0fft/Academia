import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal

K1 = 17
K2 = 0.1
K3 = 1
T1 = 0.002
T2 = 0.4

num = [K1 + K2]
den = [T1 * T2, T1 + T2, 1, (K1 + K2) * K3]

system = signal.TransferFunction(num, den)

time = np.linspace(0, 5, 100)
t, y = signal.step(system, T=time)

first_peak_time = t[np.argmax(y)]
peak_values = y[np.argmax(y):]
zero_crossings = np.where(np.diff(np.sign(peak_values - np.mean(peak_values))))[0]

if len(zero_crossings) > 1:
    period = np.mean(np.diff(t[zero_crossings]))
    frequency = 1 / period
else:
    frequency = np.nan

rise_time = t[np.where(y >= 0.9 * max(y))[0][0]]
overshoot = (max(y) - 1) * 100

settling_indices = np.where(np.abs(y - 1) <= 0.02)[0]

if len(settling_indices) > 0:
    settling_time = t[settling_indices[-1]]
else:
    settling_time = np.nan

if len(peak_values) > 1:
    damping_decrement = (peak_values[0] - 1) / (peak_values[1] - 1)
else:
    damping_decrement = None

steady_state_error = 1 - y[-1]

static_gain = K1 * K2 / (T1 * T2)

resonance_frequency = frequency

integral_square_error = np.trapz((y - 1) ** 2, t)

print(f'1. Час досягнення першого максимуму: {first_peak_time:.4f} с')
print(f'2. Частота коливань: {frequency if not np.isnan(frequency) else "Немає коливань"} Гц')

print(f'3. Час нарастання перехідного процесу: {rise_time:.4f} с')
print(f'4. Перерегулювання: {overshoot:.2f} %')

print(f'5. Час регулювання: {settling_time if not np.isnan(settling_time) else "Не знайдено"} с')
print(f'6. Декремент затухання: {damping_decrement if damping_decrement is not None else "Невизначено"}')

print(f'7. Установившася помилка: {steady_state_error:.4f}')
print(f'8. Коефіцієнт статизму: {static_gain:.4f}')

print(f'9. Резонансна частота: {resonance_frequency if not np.isnan(resonance_frequency) else "Немає коливань"} Гц')
print(f'10. Квадратична інтегральна оцінка: {integral_square_error:.4f}')

plt.figure(figsize=(8, 6))
plt.plot(t, y, label='Перехідна характеристика')
plt.axhline(1, color='r', linestyle='--', label='Встановлена величина')
plt.title('Перехідна характеристика системи')
plt.xlabel('Час (с)')
plt.ylabel('Вихідна величина')
plt.legend()
plt.grid(True)
plt.show()
