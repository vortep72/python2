# Задание "Упрощение дроби"
import math

def parse_fraction(raw_fraction: str):
    """
    Извлекает из строки элементы дроби: целую часть(whole), числитель(numerator) и знаменатель(denominator).
    Также определяет знак дроби(sign) +/-
    """
    sign = 1
    if raw_fraction.startswith("-"):
        sign = -1
        raw_fraction = raw_fraction[1:]
    pair = raw_fraction.split()
    whole = 0
    if len(pair) == 2:
        whole = int(pair[0])
        raw_fraction = pair[-1]
    pair = raw_fraction.split('/')
    numerator = int(pair[0])
    denominator = int(pair[1])
    return {"sign": sign, "whole": whole, "numerator": numerator, "denominator": denominator}


def simplificator(fraction):
    fraction_parse = parse_fraction(fraction)
    numerator = fraction_parse["numerator"]
    denominator = fraction_parse["denominator"]
    gcd = math.gcd(numerator, denominator)
    numerator = numerator // gcd
    denominator = denominator // gcd
    new_whole = 0
    if numerator > denominator:
        new_whole = numerator // denominator
        numerator = numerator % denominator

    whole = fraction_parse["whole"] + new_whole
    whole = whole * fraction_parse["sign"]
    if whole:
        return f"{whole} {numerator}/{denominator}"
    else:
        numerator = numerator * fraction_parse["sign"]
        return f"{numerator}/{denominator}"


# Простые дроби заданы в виде строки формата: целая_часть числитель/знаменатель
# целая_часть может отсутствовать, числитель и знаменатель всегда присутствуют
# если целая часть присутствует, то всегда отделяется от дробной пробелом
# дроби могут быть отрицательными или положительными
# Примеры дробей
fraction1 = "3 12/15"
fraction2 = "-1 11/6"
fraction3 = "2/4"
fraction4 = "-5/4"

# TODO: Задание: Напишите функцию simplificator, которая возвращает дробь в упрощенном виде с выделением целой части
print(simplificator("3 12/15"))  # --> 3 4/5
print(simplificator("-1 11/6"))  # --> -2 5/6
print(simplificator("2/4"))  # --> 1/2
print(simplificator("-3/4"))  # --> -3/4
print(simplificator("3 15/4"))  # --> 6 3/4

# Подсказки: смотри файлы helpers/parse_fraction.py и helpers/lcmp_gcd.py