import time

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


def benchmark_encryption(cipher, text, rounds=1000):
    start_time = time.time()
    for _ in range(rounds):
        encrypted_text = cipher.encrypt(text)
    return time.time() - start_time


text = b"Text to be encrypted in different modes to analyze performance!"
text_padded = pad(text, 16)
aes_key = get_random_bytes(16)
iv = get_random_bytes(16)

ciphers = {
    "ECB": AES.new(aes_key, AES.MODE_ECB),
    "CBC": AES.new(aes_key, AES.MODE_CBC, iv),
    "CFB": AES.new(aes_key, AES.MODE_CFB, iv),
    "OFB": AES.new(aes_key, AES.MODE_OFB, iv),
}

results_modes = {}
print(f"\n--- Аналіз швидкодії режимів AES ---")

for mode, cipher in ciphers.items():
    encryption_time = benchmark_encryption(cipher, text_padded)
    results_modes[mode] = encryption_time
    print(f"Режим {mode}: Час шифрування: {encryption_time:.6f} секунд")

print("\n--- Результати аналізу режимів ---")

for mode, time_taken in results_modes.items():
    print(f"Режим {mode}: Час шифрування {time_taken:.6f} секунд")
