from collections import Counter


def arithmetic_encode(text):
    """
    Шифрування тексту за допомогою арифметичного кодування, враховуючи пробіли
    """
    freq = Counter(text)
    total = len(text)

    probabilities = {char: count / total for char, count in freq.items()}

    intervals = {}
    start = 0.0
    for symbol, prob in probabilities.items():
        intervals[symbol] = (start, start + prob)
        start += prob

    low = 0.0
    high = 1.0

    for symbol in text:
        symbol_low, symbol_high = intervals[symbol]
        range_ = high - low
        high = low + range_ * symbol_high
        low = low + range_ * symbol_low

    return (low + high) / 2, probabilities


def arithmetic_decode(encoded_value, probabilities, length):
    """
    Розшифрування тексту за допомогою арифметичного кодування
    """
    intervals = {}
    start = 0.0
    for symbol, prob in probabilities.items():
        intervals[symbol] = (start, start + prob)
        start += prob

    low = 0.0
    high = 1.0

    decoded_text = []
    for _ in range(length):
        range_ = high - low
        value = (encoded_value - low) / range_

        for symbol, (symbol_low, symbol_high) in intervals.items():
            if symbol_low <= value < symbol_high:
                decoded_text.append(symbol)
                low = low + range_ * symbol_low
                high = low + range_ * (symbol_high - symbol_low)
                break

    return ''.join(decoded_text)


text = "PELIKH YEVHEN"

encoded_value, probabilities = arithmetic_encode(text)

decoded_text = arithmetic_decode(encoded_value, probabilities, len(text))

print(f"Закодоване число: {encoded_value}")
print(f"Ймовірності символів: {probabilities}")
print(f"Розшифрований текст: {decoded_text}")
