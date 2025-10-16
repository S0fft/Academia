import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal

K1 = 17
K2 = 0.1
K3 = 1
T1 = 0.002
T2 = 0.4
T_d = 0.0001

dt = 0.0001
steps = 5000
time = np.linspace(0, steps * dt, steps)

num = [K1 + K2]
den = [T1 * T2, (T1 + T2), 1, K3 * (K1 + K2)]

system = signal.TransferFunction(num, den)

t, step_resp = signal.step(system, T=time)
t, impulse_resp = signal.impulse(system, T=time)


def step_response_W1(t, K1, T1):
    return K1 * (1 - np.exp(-t / T1))


def step_response_W2(t, K2, T_d):
    return K2 * (t / (T_d + t))


def step_response_W3(t, K3, T2):
    return K3 * (1 - np.exp(-t / T2))


step_resp_W1 = step_response_W1(time, K1, T1)
step_resp_W2 = step_response_W2(time, K2, T_d)
step_resp_W3 = step_response_W3(time, K3, T2)

total_step_response = step_resp_W1 + step_resp_W2 + step_resp_W3

plt.figure(figsize=(12, 12))

plt.subplot(6, 1, 1)
plt.plot(t, step_resp, label='Перехідна характеристика ', color='red')
plt.title('Перехідна та імпульсна характеристики ', fontsize=14)
plt.xlabel('Час (с)', fontsize=12)
plt.ylabel('Амплітуда', fontsize=12)
plt.grid(True)
plt.legend()

plt.subplot(6, 1, 2)
plt.plot(t, impulse_resp, label='Імпульсна характеристика', color='blue')
plt.xlabel('Час (с)', fontsize=12)
plt.ylabel('Амплітуда', fontsize=12)
plt.grid(True)
plt.legend()

plt.subplot(6, 1, 3)
plt.plot(time, step_resp_W1, label='W1 ', color='blue')
plt.xlabel('Час (с)', fontsize=12)
plt.ylabel('Амплітуда', fontsize=12)
plt.grid(True)
plt.legend()

plt.subplot(6, 1, 4)
plt.plot(time, step_resp_W2, label='W2 ', color='green')
plt.xlabel('Час (с)', fontsize=12)
plt.ylabel('Амплітуда', fontsize=12)
plt.grid(True)
plt.legend()

plt.subplot(6, 1, 5)
plt.plot(time, step_resp_W3, label='W3 ', color='red')
plt.xlabel('Час (с)', fontsize=12)
plt.ylabel('Амплітуда', fontsize=12)
plt.grid(True)
plt.legend()

plt.subplot(6, 1, 6)
plt.plot(time, total_step_response, label='Загальна система (W1 + W2 + W3)', color='purple')
plt.xlabel('Час (с)', fontsize=12)
plt.ylabel('Амплітуда', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
