import math

import matplotlib.pyplot as plt
import numpy as np

rssi_values = [-21, -42, -58]
locations = ['Поруч (1м)', 'Середня (5м)', 'Дальня (8м)']
noise_floor = -90
bandwidth_hz = 20 * 10**6
real_speed_mbps = 20.18

snr_values = [rssi - noise_floor for rssi in rssi_values]

capacity_values = []
for snr_db in snr_values:
    snr_linear = 10**(snr_db / 10)
    capacity_bps = bandwidth_hz * math.log2(1 + snr_linear)
    capacity_mbps = capacity_bps / 10**6
    capacity_values.append(round(capacity_mbps, 2))

print(f"SNR Values (dB): {snr_values}")
print(f"Capacity Values (Mbps): {capacity_values}")

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

bars1 = axs[0].bar(locations, rssi_values, color=['green', 'orange', 'red'])
axs[0].set_title('Рівень сигналу (RSSI)')
axs[0].set_ylabel('Потужність (dBm)')
axs[0].set_ylim(-100, 0)
axs[0].grid(axis='y', linestyle='--', alpha=0.7)


for bar in bars1:
    height = bar.get_height()
    axs[0].text(bar.get_x() + bar.get_width()/2., height,
                f'{height} dBm',
                ha='center', va='bottom')

bars2 = axs[1].bar(locations, snr_values, color=['blue', 'cyan', 'skyblue'])
axs[1].set_title('Співвідношення Сигнал/Шум (SNR)')
axs[1].set_ylabel('SNR (dB)')
axs[1].grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars2:
    height = bar.get_height()
    axs[1].text(bar.get_x() + bar.get_width()/2., height,
                f'{height} dB',
                ha='center', va='bottom')

comparison_labels = ['Теоретична (Max)', 'Реальна (SpeedTest)']
comparison_values = [capacity_values[1], real_speed_mbps]

bars3 = axs[2].bar(comparison_labels, comparison_values, color=['purple', 'green'])
axs[2].set_title('Пропускна здатність (при SNR 48 dB)')
axs[2].set_ylabel('Швидкість (Мбіт/с)')
axs[2].grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars3:
    height = bar.get_height()
    axs[2].text(bar.get_x() + bar.get_width()/2., height,
                f'{height} Mbps',
                ha='center', va='bottom')

plt.tight_layout()
plt.savefig('wifi_analysis_lr1.png')
