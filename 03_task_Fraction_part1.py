# Задание "Простые дроби"
import math


class Fraction:
    def __init__(self, raw_fraction):  # Дробь в конструктор передается в виде строки
        # А мы храним дробь в виде
        self.sign = 1
        if raw_fraction.startswith("-"):
            self.sign = -1
            raw_fraction = raw_fraction[1:]
        pair = raw_fraction.split()
        self.whole = 0
        if len(pair) == 2:
            whole = int(pair[0])
            raw_fraction = pair[-1]
        pair = raw_fraction.split('/')
        self.numerator = int(pair[0])
        self.denominator = int(pair[1])

    def __str__(self):
        """
        Возвращает строковое представление в формате: <Целая часть> <числитель>/<знаменатель>
        Пример: "-3 5/7"
        """

        return f"..."

    def simplificator(fraction):
        fraction_parse = Fraction.parse_fraction(fraction)
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


# Простые дроби заданы в виде строки

# Конструктор принимает простую дробь в виде строки формата: <Целая часть> <числитель>/<знаменатель>
# целая_часть может отсутствовать, числитель и знаменатель всегда присутствуют
# дроби могут быть отрицательными или положительными
f1 = Fraction("3 12/15")
f2 = Fraction("-1 11/6")
f3 = Fraction("2/4")
f4 = Fraction("-5/4")

# TODO: Задание: реализуйте class Fraction, который выводит дробь в упрощенном виде с выделением целой части
print(f1)  # 3 4/5
print(f2)  # -2 5/6
print(f3)  # 1/2
print(f4)  # -1 1/4