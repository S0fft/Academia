import random

from sympy import isprime


def generate_prime_from_key(key):
    prime_candidate = key
    while not isprime(prime_candidate):
        prime_candidate += 1
    return prime_candidate


def generate_keys():
    key = random.randint(1000, 10000)

    p = generate_prime_from_key(key)
    q = generate_prime_from_key(p + 1)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = 65537
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    d = mod_inverse(e, phi_n)

    return ((e, n), (d, n))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


def encrypt(message, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher


def decrypt(ciphertext, private_key):
    d, n = private_key
    message = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return message


message = "PELIKH YEVHEN"
print(f"Початковий текст: {message}")

public_key, private_key = generate_keys()

ciphertext = encrypt(message, public_key)
print(f"Зашифрований текст: {ciphertext}")

decrypted_message = decrypt(ciphertext, private_key)
print(f"Розшифрований текст: {decrypted_message}")
