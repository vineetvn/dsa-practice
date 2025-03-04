def romanToInt(s: str) -> int:
    number = 0
    symbol_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    for a, b in zip(s, s[1:]):
        if symbol_map[a] < symbol_map[b]:
            number -= symbol_map[a]
        else:
            number += symbol_map[a]

    return number + symbol_map[s[-1]]


print(romanToInt("MCMXCIV"))
