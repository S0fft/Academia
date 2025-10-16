from collections import Counter


def arithmetic_encode(text):
    """
    Шифрування тексту за допомогою арифметичного кодування, враховуючи пробіли
    """
    # Підрахунок частоти кожного символа в тексті
    freq = Counter(text)
    total = len(text)

    # Обчислюємо ймовірність кожного символу
    probabilities = {char: count / total for char, count in freq.items()}

    # Визначаємо інтервал для кожного символа
    intervals = {}
    start = 0.0
    for symbol, prob in probabilities.items():
        intervals[symbol] = (start, start + prob)
        start += prob

    # Початкові значення для інтервалу
    low = 0.0
    high = 1.0

    # Процес кодування
    for symbol in text:
        symbol_low, symbol_high = intervals[symbol]
        # Сузимо інтервал для кожного символа
        range_ = high - low
        high = low + range_ * symbol_high
        low = low + range_ * symbol_low

    # Повертаємо середнє значення інтервалу як закодоване число
    return (low + high) / 2, probabilities


def arithmetic_decode(encoded_value, probabilities, length):
    """
    Розшифрування тексту за допомогою арифметичного кодування
    """
    # Визначаємо інтервал для кожного символа
    intervals = {}
    start = 0.0
    for symbol, prob in probabilities.items():
        intervals[symbol] = (start, start + prob)
        start += prob

    # Початкові значення для інтервалу
    low = 0.0
    high = 1.0

    # Розшифровка
    decoded_text = []
    for _ in range(length):
        range_ = high - low
        # Визначаємо, до якого інтервалу належить закодоване число
        value = (encoded_value - low) / range_

        # Знаходимо символ, відповідний цьому значенню
        for symbol, (symbol_low, symbol_high) in intervals.items():
            if symbol_low <= value < symbol_high:
                decoded_text.append(symbol)
                low = low + range_ * symbol_low
                high = low + range_ * (symbol_high - symbol_low)
                break

    return ''.join(decoded_text)


# Текст для шифрування
text = "PELIKH YEVHEN"

# Шифрування
encoded_value, probabilities = arithmetic_encode(text)

# Розшифровка
decoded_text = arithmetic_decode(encoded_value, probabilities, len(text))

# Виведення результатів
print(f"Закодоване число: {encoded_value}")
print(f"Ймовірності символів: {probabilities}")
print(f"Розшифрований текст: {decoded_text}")
