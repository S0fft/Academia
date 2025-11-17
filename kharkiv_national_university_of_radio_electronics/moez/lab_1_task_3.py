import time

from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


def benchmark_encryption(cipher, text, rounds=1000):
    start_time = time.time()
    for _ in range(rounds):
        encrypted_text = cipher.encrypt(text)
    return time.time() - start_time


text_sizes = [1024, 4096, 16384, 1048576]
des_key = get_random_bytes(8)
aes_key = get_random_bytes(16)
BLOCK_SIZE_DES = 8
BLOCK_SIZE_AES = 16

results = {'DES': [], 'AES': []}
print("--- 3. Аналіз швидкодії DES vs AES ---")

for size in text_sizes:
    print(f"\nТестування для розміру даних: {size} байт")
    text = get_random_bytes(size)

    des_text_padded = pad(text, BLOCK_SIZE_DES)
    aes_text_padded = pad(text, BLOCK_SIZE_AES)

    des_cipher = DES.new(des_key, DES.MODE_ECB)
    aes_cipher = AES.new(aes_key, AES.MODE_ECB)

    des_time = benchmark_encryption(des_cipher, des_text_padded)
    results['DES'].append(des_time)
    print(f"DES час шифрування: {des_time:.6f} секунд")

    aes_time = benchmark_encryption(aes_cipher, aes_text_padded)
    results['AES'].append(aes_time)
    print(f"AES час шифрування: {aes_time:.6f} секунд")

print("\n--- Результати тестування швидкодії (у секундах, 1000 раундів) ---")
print(f"{'Розмір (байт)':<15} | {'DES (час)':<15} | {'AES (час)':<15}")
print("-" * 47)

for i, size in enumerate(text_sizes):
    print(f"{size:<15} | {results['DES'][i]:<15.6f} | {results['AES'][i]:<15.6f}")
