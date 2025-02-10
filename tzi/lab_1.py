def caesar_cipher_encrypt(text, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_text = ""

    text = text.upper()

    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += char

    return encrypted_text


def caesar_cipher_decrypt(text, shift):
    """
    Функція для дешифрування тексту за допомогою шифру Цезаря
    """
    return caesar_cipher_encrypt(text, -shift)


text = "PELIKH YEVHEN"

shift = 3

encrypted_text = caesar_cipher_encrypt(text, shift)
print(f"Зашифрований текст (зсув {shift}): {encrypted_text}")

decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
print(f"Розшифрований текст: {decrypted_text}")
