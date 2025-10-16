import heapq  # для роботи з купою, необхідно для алгоритму Хаффмана
import itertools  # для циклічного повторення ключа
from collections import Counter, namedtuple  # для підрахунку частоти символів та створення простих класів

ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"  # український алфавіт
ALPHABET_SIZE = len(ALPHABET)  # кількість символів в алфавіті


def generate_key(text, key):
    """Генеруємо ключ потрібної довжини"""
    return ''.join(itertools.islice(itertools.cycle(key), len(text)))


def vigenere_encrypt(text, key):
    """Шифруємо текст за алгоритмом Віженера"""
    key = generate_key(text, key)
    encrypted_text = ""
    for t, k in zip(text, key):
        if t in ALPHABET:
            new_index = (ALPHABET.index(t) + ALPHABET.index(k)) % ALPHABET_SIZE
            encrypted_text += ALPHABET[new_index]
        else:
            encrypted_text += t
    return encrypted_text


def vigenere_decrypt(encrypted_text, key):
    """Дешифруємо текст за алгоритмом Віженера"""
    key = generate_key(encrypted_text, key)
    decrypted_text = ""
    for t, k in zip(encrypted_text, key):
        if t in ALPHABET:
            new_index = (ALPHABET.index(t) - ALPHABET.index(k)) % ALPHABET_SIZE
            decrypted_text += ALPHABET[new_index]
        else:
            decrypted_text += t
    return decrypted_text

# Побудова дерева Хаффмана


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


# Вхідний текст і ключ
text = "Всяк кулик своє болото хвалить"
key = "книга"

# Шифруємо та дешифруємо текст за алгоритмом Віженера
encrypted_text = vigenere_encrypt(text, key)
print("Зашифрований текст:", encrypted_text)

decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Розшифрований текст:", decrypted_text)

# Побудова дерева Хаффмана та отримання кодів для символів тексту
huffman_code = huffman_encode(text)
print("Коди Хаффмана:")
for char, code in sorted(huffman_code.items()):
    print(f"{char}: {code}")
