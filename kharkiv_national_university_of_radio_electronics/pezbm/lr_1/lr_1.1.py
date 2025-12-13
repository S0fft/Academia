import matplotlib.pyplot as plt
import numpy as np

f = 2.437e9
c = 3e8
lam = c / f
P_tx_dBm = 20
P_tx = 10**(P_tx_dBm / 10) / 1000
G_tx_dBi = 0
G_rx_dBi = 0
G_tx = 10**(G_tx_dBi / 10)
G_rx = 10**(G_rx_dBi / 10)
Band = 20e6

k_B = 1.38e-23
T_0 = 293
k_r = 10

meas_dist = np.array([1, 5, 8])
meas_rssi = np.array([-21, -42, -58])
real_speed_mbps = 20.18

A_r = (G_rx * lam**2) / (4 * np.pi)


def calc_signal_power(d, k):
    """
    Розрахунок потужності сигналу за Формулою (1).
    Повертає потужність у Ватах та dBm.
    """
    Ps_watts = (P_tx * G_tx * A_r) / (4 * np.pi * (d**k))
    Ps_dBm = 10 * np.log10(Ps_watts) + 30
    return Ps_watts, Ps_dBm


def calc_noise_power():
    """
    Розрахунок теплового шуму за Формулою (4).
    Повертає потужність шуму в смузі Band.
    """
    Pn_watts = 4 * k_B * T_0 * k_r * Band
    Pn_dBm = 10 * np.log10(Pn_watts) + 30
    return Pn_watts, Pn_dBm


def calc_capacity(S_watts, N_watts):
    """
    Розрахунок пропускної здатності за Формулою (5) (Шеннон).
    """
    SNR = S_watts / N_watts
    C_bps = Band * np.log2(1 + SNR)
    return C_bps / 1e6


d_range = np.linspace(0.5, 15, 100)

P_k2_W, P_k2_dBm = calc_signal_power(d_range, 2)
P_k3_W, P_k3_dBm = calc_signal_power(d_range, 3)
P_k4_W, P_k4_dBm = calc_signal_power(d_range, 4)

Noise_W, Noise_dBm = calc_noise_power()

C_k2 = calc_capacity(P_k2_W, Noise_W)
C_k3 = calc_capacity(P_k3_W, Noise_W)
C_k4 = calc_capacity(P_k4_W, Noise_W)

P_5m_W, P_5m_dBm = calc_signal_power(5, 2)
C_5m_theor = calc_capacity(P_5m_W, Noise_W)

print(f"--- Результати розрахунків ---")
print(f"Ефективний розкрив антени A_r: {A_r:.6f} м^2")
print(f"Рівень шуму (теоретичний): {Noise_dBm:.2f} dBm ({Noise_W:.2e} Вт)")
print(f"Теоретична ємність (Шеннон) на 5м (k=2): {C_5m_theor:.2f} Мбіт/с")
print(f"Реальна швидкість (SpeedTest) на 5м: {real_speed_mbps} Мбіт/с")
print("-" * 65)
print(f"{'Відстань (м)':<15} | {'RSSI Вимір':<15} | {'Теорія k=2':<15} | {'Теорія k=3':<15}")
for i, d_val in enumerate(meas_dist):
    _, p2 = calc_signal_power(d_val, 2)
    _, p3 = calc_signal_power(d_val, 3)
    print(f"{d_val:<15} | {meas_rssi[i]:<15} | {p2:.2f} {'':<10} | {p3:.2f}")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

ax1.plot(d_range, P_k2_dBm, 'g--', label='k=2 (Вільний простір)')
ax1.plot(d_range, P_k3_dBm, 'orange', label='k=3 (Прості перешкоди)')
ax1.plot(d_range, P_k4_dBm, 'r-.', label='k=4 (Складні перешкоди)')
ax1.scatter(meas_dist, meas_rssi, color='blue', s=80, label='Практичні виміри', zorder=5)
ax1.axhline(y=-90, color='gray', linestyle=':', label='Поріг шуму (-90 dBm)')
ax1.set_title('Залежність рівня сигналу від дальності')
ax1.set_xlabel('Відстань, м')
ax1.set_ylabel('RSSI, dBm')
ax1.grid(True, which='both', linestyle='--', alpha=0.7)
ax1.legend()

ax2.plot(d_range, C_k2, 'g--', label='Шеннон (k=2)')
ax2.plot(d_range, C_k3, 'orange', label='Шеннон (k=3)')
ax2.scatter([5], [real_speed_mbps], color='purple', marker='^', s=100, label='SpeedTest (5м)', zorder=5)
ax2.set_title('Потенційна пропускна здатність (C)')
ax2.set_xlabel('Відстань, м')
ax2.set_ylabel('Швидкість, Мбіт/с')
ax2.grid(True, which='both', linestyle='--', alpha=0.7)
ax2.legend()

plt.tight_layout()
plt.savefig('lab1_plots.png')
plt.show()
