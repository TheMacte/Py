"""
 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
 Количество элементов (n) вводится с клавиатуры.
"""


def n_sum(n, mem=1, my_sum=1):
    if n == 1:
        return my_sum
    else:
        n -= 1
        mem = mem / -2
        my_sum += mem
        return n_sum(n, mem, my_sum)


print(n_sum(int(input('Введите число n: '))))
