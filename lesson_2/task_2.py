"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
 Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def nut_num(into, reg=0, irreg=0):
    if (into % 10) % 2 == 0:
        reg += 1
    else:
        irreg += 1
    if len(str(into)) > 1:
        into = into // 10
        return nut_num(into, reg, irreg)
    else:
        return f'Чётных: {reg}, нечётных {irreg}'


print(nut_num(int(input('Введите число n: '))))
