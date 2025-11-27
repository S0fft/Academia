import os
import time

import matplotlib.pyplot as plt
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, padding, rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF


def benchmark_rsa(key_size=2048, message=b"Test message for RSA analysis"):
    print(f"\n--- Тестування RSA ({key_size} біт) ---")

    start = time.time()
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size
    )
    public_key = private_key.public_key()
    gen_time = time.time() - start
    print(f"Час генерації ключів: {gen_time:.4f} с")

    start = time.time()
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    enc_time = time.time() - start
    print(f"Час шифрування: {enc_time:.4f} с")

    start = time.time()
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    dec_time = time.time() - start
    print(f"Час дешифрування: {dec_time:.4f} с")

    return gen_time, enc_time, dec_time


def benchmark_ecc(curve=ec.SECP256R1(), curve_name="SECP256R1", message=b"Test message for ECC analysis"):
    print(f"\n--- Тестування ECC ({curve_name}) ---")

    start = time.time()
    priv_key_A = ec.generate_private_key(curve)
    pub_key_A = priv_key_A.public_key()

    priv_key_B = ec.generate_private_key(curve)
    pub_key_B = priv_key_B.public_key()
    gen_time = time.time() - start
    print(f"Час генерації пар ключів: {gen_time:.4f} с")

    start = time.time()
    shared_key_A = priv_key_A.exchange(ec.ECDH(), pub_key_B)

    ecdh_time = time.time() - start
    print(f"Час узгодження ключа (ECDH): {ecdh_time:.4f} с")

    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data'
    ).derive(shared_key_A)

    start = time.time()
    iv = os.urandom(12)
    cipher = Cipher(algorithms.AES(derived_key), modes.GCM(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message) + encryptor.finalize()
    enc_time = time.time() - start
    print(f"Час шифрування (гібридне ECC+AES): {enc_time:.4f} с")

    start = time.time()
    decryptor = Cipher(algorithms.AES(derived_key), modes.GCM(iv, encryptor.tag)).decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    dec_time = time.time() - start
    print(f"Час дешифрування: {dec_time:.4f} с")

    return gen_time, ecdh_time, enc_time, dec_time


def run_analysis():
    rsa_keys = [1024, 2048, 4096]
    ecc_curves = [
        (ec.SECP256R1(), "SECP256R1 (256 bit)"),
        (ec.SECP384R1(), "SECP384R1 (384 bit)"),
        (ec.SECP521R1(), "SECP521R1 (521 bit)")
    ]

    rsa_results = {'gen': [], 'enc': [], 'dec': []}
    ecc_results = {'gen': [], 'enc': [], 'dec': []}

    print("=== ПОЧАТОК КОМПЛЕКСНОГО АНАЛІЗУ ===")

    for size in rsa_keys:
        g, e, d = benchmark_rsa(key_size=size)
        rsa_results['gen'].append(g)
        rsa_results['enc'].append(e)
        rsa_results['dec'].append(d)

    for curve, name in ecc_curves:
        g, ecdh, e, d = benchmark_ecc(curve=curve, curve_name=name)
        ecc_results['gen'].append(g)
        ecc_results['enc'].append(e)
        ecc_results['dec'].append(d)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    ax1.plot(rsa_keys, rsa_results['gen'], marker='o', label='RSA Key Gen', color='blue')

    ax1.set_title('Час генерації ключів RSA')
    ax1.set_xlabel('Розмір ключа (біт)')
    ax1.set_ylabel('Час (с)')
    ax1.grid(True)
    ax1.legend()

    labels = ['RSA-2048', 'ECC-256']
    times = [rsa_results['gen'][1], ecc_results['gen'][0]]

    ax2.bar(labels, times, color=['blue', 'green'])
    ax2.set_title('Порівняння генерації: RSA-2048 vs ECC-256')
    ax2.set_ylabel('Час (с)')

    plt.tight_layout()
    plt.show()

    print("\n=== АНАЛІЗ ЗАВЕРШЕНО ===")


if __name__ == "__main__":
    run_analysis()
