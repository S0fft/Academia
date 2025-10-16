import itertools  # імпортуємо для циклічного повторення

ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"  # український алфавіт
ALPHABET_SIZE = len(ALPHABET)  # розмір алфавіту


def generate_key(text, key):
    """Генерація ключа потрібної довжини"""
    # циклічно повторюємо ключ і обрізаємо до довжини тексту
    return ''.join(itertools.islice(itertools.cycle(key), len(text)))


def vigenere_encrypt(text, key):
    """Шифрування тексту за шифром Віженера"""
    key = generate_key(text, key)
    encrypted_text = ""
    for t, k in zip(text, key):
        if t in ALPHABET:
            # додаємо позиції символів і беремо за модулем розмір алфавіту
            new_index = (ALPHABET.index(t) + ALPHABET.index(k)) % ALPHABET_SIZE
            encrypted_text += ALPHABET[new_index]
        else:
            encrypted_text += t
    return encrypted_text


def vigenere_decrypt(encrypted_text, key):
    """Дешифрування тексту за шифром Віженера"""
    key = generate_key(encrypted_text, key)
    decrypted_text = ""
    for t, k in zip(encrypted_text, key):
        if t in ALPHABET:
            # віднімаємо позицію символа ключа для відновлення оригіналу
            new_index = (ALPHABET.index(t) - ALPHABET.index(k)) % ALPHABET_SIZE
            decrypted_text += ALPHABET[new_index]
        else:
            decrypted_text += t
    return decrypted_text


# Вхідний текст і ключ
text = "Всяк кулик своє болото хвалить"
key = "книга"

encrypted_text = vigenere_encrypt(text, key)
print("Зашифрований текст:", encrypted_text)

decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Розшифрований текст:", decrypted_text)
