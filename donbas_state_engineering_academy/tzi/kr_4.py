def caesar_encrypt(text, shift):
    # Шифрування тексту за методом Цезаря
    result = ""
    for char in text:
        if 'А' <= char <= 'Я' or 'а' <= char <= 'я':
            base = ord('А') if char.isupper() else ord('а')
            result += chr((ord(char) - base + shift) % 32 + base)
        else:
            result += char
    return result


def caesar_decrypt(text, shift):
    # Дешифрування через зворотний зсув
    return caesar_encrypt(text, -shift)


def transpose(text, block_size, order):
    # Перестановка символів в тексті
    while len(text) % block_size != 0:
        text += ' '
    blocks = [text[i:i+block_size] for i in range(0, len(text), block_size)]
    transposed = ""
    for block in blocks:
        new_block = [''] * len(block)
        for i, pos in enumerate(order):
            if i < len(block):
                new_block[pos - 1] = block[i]
        transposed += ''.join(new_block)
    return transposed


def transpose_reverse(text, block_size, order):
    # Відновлення початкового порядку символів
    blocks = [text[i:i+block_size] for i in range(0, len(text), block_size)]
    reverse_order = [order.index(i+1) for i in range(len(order))]
    transposed = ""
    for block in blocks:
        new_block = [''] * len(block)
        for i, pos in enumerate(reverse_order):
            new_block[i] = block[pos]
        transposed += ''.join(new_block)
    return transposed


def xor_encrypt(text, key):
    # Шифрування методом XOR з ключем
    result = ""
    for i, char in enumerate(text):
        result += chr(ord(char) ^ ord(key[i % len(key)]))
    return result


# Процес шифрування та дешифрування
original_text = "Пеліх Євген"  # Початковий текст
caesar_shift = 3             # Зсув для Цезаревого шифру
block_size = 4               # Розмір блоку для перестановки
order = [4, 2, 3, 1]         # Порядок перестановки
xor_key = "ключ"             # Ключ для XOR

# Етап 1: Цезарів шифр
encrypted = caesar_encrypt(original_text, caesar_shift)
# Етап 2: Перестановка
encrypted = transpose(encrypted, block_size, order)
# Етап 3: XOR шифрування
encrypted = xor_encrypt(encrypted, xor_key)
print(f"Зашифрований текст: {encrypted}")

# Дешифрування
decrypted = xor_encrypt(encrypted, xor_key)
decrypted = transpose_reverse(decrypted, block_size, order)
decrypted = caesar_decrypt(decrypted, caesar_shift)
print(f"Розшифрований текст: {decrypted}")
