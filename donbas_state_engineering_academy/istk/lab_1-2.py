import matplotlib.pyplot as plt
import numpy as np

K1 = 17
K2 = 0.1
K3 = 1
T1 = 0.002
T2 = 0.4
T_d = 0.0001

dt = 0.0001
steps = 5000
time = np.linspace(0, steps * dt, steps)


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

plt.subplot(4, 1, 1)
plt.plot(time, step_resp_W1, label='W1', color='blue')
plt.title(' W1, W2, W3 та система')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(time, step_resp_W2, label='W2', color='green')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(time, step_resp_W3, label='W3', color='red')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(time, total_step_response, label='Загальна система', color='purple')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
