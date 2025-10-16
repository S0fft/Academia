import math


def vertical_transposition_encrypt(text, key):
    """
    Шифрування тексту за допомогою шифру вертикальної перестановки
    """
    text = text.replace(" ", "").upper()  # Видаляємо пробіли і переводимо текст у верхній регістр
    key_order = sorted(range(len(key)), key=lambda k: key[k])  # Визначаємо порядок ключа
    columns = [""] * len(key)

    # Заповнюємо стовпці текстом
    for i, char in enumerate(text):
        columns[i % len(key)] += char

    # Переставляємо стовпці за порядком ключа
    encrypted_text = ""
    for idx in key_order:
        encrypted_text += columns[idx]

    return encrypted_text


def vertical_transposition_decrypt(encrypted_text, key):
    """
    Розшифрування тексту за допомогою шифру вертикальної перестановки
    """
    key_order = sorted(range(len(key)), key=lambda k: key[k])  # Визначаємо порядок ключа
    num_rows = math.ceil(len(encrypted_text) / len(key))  # Розраховуємо кількість рядків
    columns = [""] * len(key)

    # Визначаємо кількість символів у кожному стовпці
    col_lengths = [num_rows] * len(key)
    for i in range(len(encrypted_text) - num_rows * len(key)):  # Визначаємо, скільки стовпців повинні бути коротшими
        col_lengths[key_order[i]] -= 1

    # Заповнюємо стовпці
    idx = 0
    for order_idx in key_order:
        columns[order_idx] = encrypted_text[idx:idx + col_lengths[order_idx]]
        idx += col_lengths[order_idx]

    # Відновлюємо текст по рядках
    decrypted_text = ""
    for i in range(num_rows):
        for col in columns:
            if i < len(col):
                decrypted_text += col[i]

    return decrypted_text


def winston_cipher_encrypt(text, key):
    """
    Шифрування тексту за допомогою шифру Уінстона
    """
    text = text.upper().replace(" ", "")  # Преобразуємо текст у верхній регістр і видаляємо пробіли
    encrypted_text = ""

    # Повторюємо ключ до довжини тексту
    full_key = (key * (len(text) // len(key) + 1))[:len(text)]

    # XOR кожного символу тексту та ключа
    for t_char, k_char in zip(text, full_key):
        encrypted_char = chr(((ord(t_char) - 65) ^ (ord(k_char) - 65)) + 65)
        encrypted_text += encrypted_char

    return encrypted_text


def winston_cipher_decrypt(encrypted_text, key):
    """
    Розшифрування тексту за допомогою шифру Уінстона
    """
    decrypted_text = ""

    # Повторюємо ключ до довжини тексту
    full_key = (key * (len(encrypted_text) // len(key) + 1))[:len(encrypted_text)]

    # XOR для дешифрування
    for e_char, k_char in zip(encrypted_text, full_key):
        decrypted_char = chr(((ord(e_char) - 65) ^ (ord(k_char) - 65)) + 65)
        decrypted_text += decrypted_char

    return decrypted_text


# Основний текст
text = "PELIKH YEVHEN"

# Шифр вертикальної перестановки
key_vt = "KEY"
encrypted_vt = vertical_transposition_encrypt(text, key_vt)
decrypted_vt = vertical_transposition_decrypt(encrypted_vt, key_vt)

# Шифр Уінстона
key_winston = "SECRET"
encrypted_winston = winston_cipher_encrypt(text, key_winston)
decrypted_winston = winston_cipher_decrypt(encrypted_winston, key_winston)

# Виведення результатів
print("Шифр вертикальної перестановки:")
print(f"  Зашифрований текст: {encrypted_vt}")
print(f"  Розшифрований текст: {decrypted_vt}")
print()
print("Шифр Уінстона:")
print(f"  Зашифрований текст: {encrypted_winston}")
print(f"  Розшифрований текст: {decrypted_winston}")
