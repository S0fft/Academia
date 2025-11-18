from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

BLOCK_SIZE_DES = 8
BLOCK_SIZE_AES = 16


def flip_bit(byte_seq, bit_index):
    """
    Функція змінює один біт у байтовому рядку.
    """

    byte_list = list(byte_seq)
    byte_pos = bit_index // 8
    bit_pos_in_byte = bit_index % 8

    byte_list[byte_pos] ^= (1 << bit_pos_in_byte)

    return bytes(byte_list)


def calculate_hamming_distance(b_seq1, b_seq2):
    """
    Функція розраховує відстань Геммінга (кількість
    відмінних бітів) між двома байтовими рядками.
    """
    xor_result = bytes(b1 ^ b2 for b1, b2 in zip(b_seq1, b_seq2))

    bit_count = sum(bin(byte).count('1') for byte in xor_result)
    return bit_count


text_des = get_random_bytes(BLOCK_SIZE_DES)
text_aes = get_random_bytes(BLOCK_SIZE_AES)
des_key = get_random_bytes(BLOCK_SIZE_DES)
aes_key = get_random_bytes(BLOCK_SIZE_AES)
BIT_TO_FLIP = 3

print(f"--- 4. Лавинний ефект (зміна 1 біта у тексті) ---")

text_des_flipped = flip_bit(text_des, BIT_TO_FLIP)
text_aes_flipped = flip_bit(text_aes, BIT_TO_FLIP)

des_cipher = DES.new(des_key, DES.MODE_ECB)
aes_cipher = AES.new(aes_key, AES.MODE_ECB)

encrypted_des_original = des_cipher.encrypt(text_des)
encrypted_aes_original = aes_cipher.encrypt(text_aes)
encrypted_des_flipped_text = des_cipher.encrypt(text_des_flipped)
encrypted_aes_flipped_text = aes_cipher.encrypt(text_aes_flipped)

des_diff_text = calculate_hamming_distance(encrypted_des_original, encrypted_des_flipped_text)
aes_diff_text = calculate_hamming_distance(encrypted_aes_original, encrypted_aes_flipped_text)

print(f"DES (64 біти): Змінено {des_diff_text} біт(ів). ({des_diff_text/64*100:.2f}%)")
print(f"AES (128 біт): Змінено {aes_diff_text} біт(ів). ({aes_diff_text/128*100:.2f}%)")
print(f"\n--- 5. Лавинний ефект (зміна 1 біта у ключі) ---")

des_key_flipped = flip_bit(des_key, BIT_TO_FLIP)
aes_key_flipped = flip_bit(aes_key, BIT_TO_FLIP)

des_cipher_flipped_key = DES.new(des_key_flipped, DES.MODE_ECB)
aes_cipher_flipped_key = AES.new(aes_key_flipped, AES.MODE_ECB)

encrypted_des_flipped_key = des_cipher_flipped_key.encrypt(text_des)
encrypted_aes_flipped_key = aes_cipher_flipped_key.encrypt(text_aes)

des_diff_key = calculate_hamming_distance(encrypted_des_original, encrypted_des_flipped_key)
aes_diff_key = calculate_hamming_distance(encrypted_aes_original, encrypted_aes_flipped_key)

print(f"DES (64 біти): Змінено {des_diff_key} біт(ів). ({des_diff_key/64*100:.2f}%)")
print(f"AES (128 біт): Змінено {aes_diff_key} біт(ів). ({aes_diff_key/128*100:.2f}%)")
