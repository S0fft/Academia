from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


def print_binary(data):
    binary_data = ''.join(format(byte, '08b') for byte in data)
    print(binary_data)


key = b'8546abcd'

data = b'PELIKH YEVHEN'

cipher = DES.new(key, DES.MODE_ECB)

ciphertext = cipher.encrypt(pad(data, DES.block_size))

print("Зашифровані дані: ")
print_binary(ciphertext)

decrypted_data = unpad(cipher.decrypt(ciphertext), DES.block_size)
print("Розшифровані дані: ", decrypted_data.decode())
