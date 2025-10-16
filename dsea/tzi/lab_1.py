def caesar_cipher_encrypt(text, shift):
    """
    Функція для шифрування тексту за допомогою шифру Цезаря
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_text = ""

    # Преобразуємо текст у верхній регістр
    text = text.upper()

    for char in text:
        if char in alphabet:
            # Знаходимо індекс символу в алфавіті
            index = alphabet.index(char)
            # Розраховуємо новий індекс з урахуванням зсуву
            new_index = (index + shift) % len(alphabet)
            # Додаємо символ з новим індексом у результат
            encrypted_text += alphabet[new_index]
        else:
            # Якщо символ не з алфавіту, додаємо його як є (наприклад, пробіли)
            encrypted_text += char

    return encrypted_text


def caesar_cipher_decrypt(text, shift):
    """
    Функція для дешифрування тексту за допомогою шифру Цезаря
    """
    # Використовуємо ту саму функцію, але змінюємо знак зсуву на протилежний
    return caesar_cipher_encrypt(text, -shift)


# Вхідний текст
text = "PELIKH YEVHEN"

# Зсув
shift = 3

# Шифруємо текст
encrypted_text = caesar_cipher_encrypt(text, shift)
print(f"Зашифрований текст (зсув {shift}): {encrypted_text}")

# Дешифруємо текст
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
print(f"Розшифрований текст: {decrypted_text}")
