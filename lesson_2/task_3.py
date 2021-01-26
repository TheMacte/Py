"""
 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
 Например, если введено число 3486, надо вывести 6843.
"""


def revers(num_in, tmp=None, cnt=None) -> int:
    if cnt == 1:
        return tmp
    elif cnt is None:
        cnt = len(str(num_in))
    else:
        cnt -= 1
    tmp = num_in % 10 if tmp is None else int(str(tmp) + str(num_in % 10))
    return revers(num_in // 10, tmp, cnt)


print(revers(int(input('Введите натуральное число: '))))
