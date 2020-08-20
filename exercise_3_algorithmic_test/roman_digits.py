import math

roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


def int_to_roman(num: int) -> str:
    result = ""
    for i in range(len(values)):
        result += num // values[i] * roman[i]
        num %= values[i]
    return result


