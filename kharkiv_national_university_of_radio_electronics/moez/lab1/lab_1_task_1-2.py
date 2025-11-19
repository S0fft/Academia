from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

print("--- 1. Демонстрація DES ---")

try:
    des_key = get_random_bytes(8)
    des_cipher = DES.new(des_key, DES.MODE_ECB)
    BLOCK_SIZE_DES = 8

    text_des = b'Test Text / Moez Lab 1'

    padded_text_des = pad(text_des, BLOCK_SIZE_DES)

    encrypted_des = des_cipher.encrypt(padded_text_des)

    des_decipher = DES.new(des_key, DES.MODE_ECB)
    decrypted_padded_des = des_decipher.decrypt(encrypted_des)

    original_text_des = unpad(decrypted_padded_des, BLOCK_SIZE_DES)

    print(f"Відкритий текст: {original_text_des.decode('utf-8')}")
    print(f"Шифротекст (hex): {encrypted_des.hex()}")
    print(f"Текст відновлено: {original_text_des == text_des}\n")

except Exception as e:
    print(f"Помилка DES: {e}\n")

print("--- 2. Демонстрація AES (виправлена) ---")

try:
    aes_key = get_random_bytes(16)
    aes_cipher = AES.new(aes_key, AES.MODE_ECB)

    BLOCK_SIZE_AES = 16
    text_aes = b'Test Text / Moez Lab 1'

    padded_text_aes = pad(text_aes, BLOCK_SIZE_AES)

    encrypted_aes = aes_cipher.encrypt(padded_text_aes)

    aes_decipher = AES.new(aes_key, AES.MODE_ECB)
    decrypted_padded_aes = aes_decipher.decrypt(encrypted_aes)

    original_text_aes = unpad(decrypted_padded_aes, BLOCK_SIZE_AES)

    print(f"Відкритий текст: {original_text_aes.decode('utf-8')}")
    print(f"Шифротекст (hex): {encrypted_aes.hex()}")
    print(f"Текст відновлено: {original_text_aes == text_aes}\n")

except Exception as e:
    print(f"Помилка AES: {e}\n")
