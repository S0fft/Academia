import matplotlib.pyplot as plt
import numpy as np

K1 = 17
K2 = 0.1
K3 = 1
T1 = 0.002
T2 = 0.4

dt = 0.001
steps = 2000
time = np.linspace(0, steps * dt, steps)


def step_response_variant(t, K1, K2, K3, T1, T2):
    term1 = K1 * (1 - np.exp(-t / T1))
    term2 = K2 * t
    term3 = K3 * (1 - np.exp(-t / T2))
    return term1 + term2 + term3


def impulse_response_variant(t, K1, K2, K3, T1, T2):
    term1 = K1 * (np.exp(-t / T1) / T1)
    term2 = K2
    term3 = K3 * (np.exp(-t / T2) / T2)
    return term1 + term2 + term3


step_resp_variant = step_response_variant(time, K1, K2, K3, T1, T2)
impulse_resp_variant = impulse_response_variant(time, K1, K2, K3, T1, T2)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(time, step_resp_variant, label='Перехідна характеристика', color='red')
plt.title('Перехідна та імпульсна характеристики', fontsize=14)
plt.xlabel('Час (с)', fontsize=12)
plt.ylabel('Амплітуда', fontsize=12)
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, impulse_resp_variant, label='Імпульсна характеристика', color='red')
plt.xlabel('Час (с)', fontsize=12)
plt.ylabel('Амплітуда', fontsize=12)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
