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

w = np.logspace(-1, 2, 1000)
w, mag, phase = signal.bode(system, w)

plt.figure(figsize=(10, 6))
plt.semilogx(w, mag, label='АЧХ')
plt.xlabel('Частота (рад/с)')
plt.ylabel('Амплітуда (дБ)')
plt.title('Амплітудно-частотна характеристика (АЧХ)')
plt.grid(True, which='both', linestyle='--')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.semilogx(w, phase, label='ФЧХ', color='red')
plt.xlabel('Частота (рад/с)')
plt.ylabel('Фаза (градуси)')
plt.title('Фазочастотна характеристика (ФЧХ)')
plt.grid(True, which='both', linestyle='--')
plt.legend()
plt.show()

fig, ax1 = plt.subplots(figsize=(10, 8))
ax1.semilogx(w, mag, label='ЛАЧХ')
ax1.set_xlabel('Частота (рад/с)')
ax1.set_ylabel('Амплітуда (дБ)')
ax1.grid(True, which='both', linestyle='--')
ax1.legend()
ax2 = ax1.twinx()
ax2.semilogx(w, phase, label='ЛФЧХ', color='red')
ax2.set_ylabel('Фаза (градуси)')
ax2.legend()
plt.title('ЛАЧХ і ЛФЧХ')
plt.show()

t, y = signal.step(system)
plt.figure(figsize=(10, 6))
plt.plot(t, y, label='ВЧХ', color='green')
plt.xlabel('Час (с)')
plt.ylabel('Амплітуда')
plt.title('ВЧХ')
plt.grid()
plt.legend()
plt.show()

max_mag = np.max(mag)
max_mag_freq = w[np.argmax(mag)]
print(f'1. Резонансна частота: {max_mag_freq:.2f} рад/с')

mag_3dB = max_mag - 3
low_freq = w[np.where(mag >= mag_3dB)[0][0]]
high_freq = w[np.where(mag >= mag_3dB)[0][-1]]
bandwidth = high_freq - low_freq
print(f'2. Полоса пропускання: {bandwidth:.2f} рад/с')
print(f'3. Частоти зрізу: {low_freq:.2f} - {high_freq:.2f} рад/с')
max_y = np.max(y)
t_transition = t[np.where(y >= 0.95 * max_y)[0][0]]
print(f'4. Довжина перехідного процесу: {t_transition:.2f} с')

peak_height = max_mag - np.min(mag)
resonance_width = high_freq - low_freq
oscillatory_index = resonance_width / peak_height
print(f'5. Показник коливальності: {oscillatory_index:.2f}')

print(f'6. Усталене значення: {max_y:.2f}')
overshoot = (max_y - 1) * 100
print(f'7. Перерегулювання: {overshoot:.2f}%')
positive_interval = t[np.where(y >= 0)[0][0]], t[np.where(y >= 0)[0][-1]]
print(f'8. Інтервал позитивності ВЧХ: від {positive_interval[0]:.2f} до {positive_interval[1]:.2f} с')
