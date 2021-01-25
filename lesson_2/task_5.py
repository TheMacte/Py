"""
 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
 Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def tbl(start, stop, cnt=10, string='') -> str:
    if start == stop + 1:
        return string
    else:
        if cnt > 0:
            if start < 100:
                string += ' '
            string += f'{start}-"{chr(start)}"  '
            cnt -= 1
        else:
            string += '\n'
            cnt = 10
        start += 1
    return tbl(start, stop, cnt, string)


print(tbl(32, 127))
