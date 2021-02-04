"""
 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
 При этом каждое число представляется как коллекция, элементы которой — цифры числа.
 Например, пользователь ввёл A2 и C4F.
 Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
 Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque


def extra_zero(num_1, num_2):
    """
    :param num_1: очередь
    :param num_2: очередь
    :return: две очереди
    """
    max_size = 0  # максимальная длинна
    if len(num_1) > len(num_2):  # Для всех чисел одинаковую разрядность
        for _ in range(len(num_1)):
            max_size += 1
            if len(num_1) < max_size:
                num_1.appendleft([0])
            if len(num_2) < max_size:
                num_2.appendleft([0])
    else:
        for _ in range(len(num_2)):
            max_size += 1
            if len(num_2) < max_size:
                num_2.appendleft('0')
            if len(num_1) < max_size:
                num_1.appendleft('0')
    return num_1, num_2


def hex_sum(num_1, num_2):
    """
    :param num_1: Шестнадцатириное число в виде строки, к которому будем прибавлять
    :param num_2: Шестнадцатириное число в виде строки, которое будем прибавлять
    :return: Шестнадцатириное число в виде списка, которое получится в результате
    """
    my_connector = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                    '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}  # Формирую словарь
    num_1, num_2, answer = deque(num_1), deque(num_2), deque()

    tmp = 0  # То что в детстве называлось "1 в уме".

    num_1, num_2 = extra_zero(num_1, num_2) # Для всех чисел одинаковую разрядность

    for _ in range(len(num_1), 0, -1):
        spam = my_connector[num_1.pop()] + my_connector[num_2.pop()] + tmp
        if spam < 16:
            answer.appendleft(spam)
            tmp = 0
        else:
            answer.appendleft(spam - 16)
            tmp = 1
    else:
        if tmp != 0:
            answer.appendleft(tmp)

    for _ in range(len(answer)):
        n = answer.pop()
        for d in my_connector:
            if my_connector[d] == n:
                answer.appendleft(d)

    return answer

#### Запутался ####

# def hex_mlt(num_1, num_2):
#     """
#     :param num_1: Шестнадцатириное число в виде строки, к которому будем прибавлять
#     :param num_2: Шестнадцатириное число в виде строки, которое будем прибавлять
#     :return: Шестнадцатириное число в виде списка, которое получится в результате
#     """
#     my_connector = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
#                     '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}  # Формирую словарь
#     num_1, num_2, answer = deque(num_1), deque(num_2), deque()
#
#     num_1, num_2 = extra_zero(num_1, num_2)  # Для всех чисел одинаковую разрядность
#     tmp = 0  # То что в детстве называлось "1 в уме".
#
#     for _ in range(len(num_1), 0, -1):
#         spam = my_connector[num_1.pop()] * my_connector[num_2.pop()] + tmp
#         if spam <= 16:
#             answer.appendleft(spam)
#             tmp = 0
#         else:
#             while spam >= 15:
#                 tmp += 1
#                 spam = spam - 16
#                 answer.appendleft(spam)
#     else:
#         if tmp < 16:
#             answer.appendleft(tmp)
#         # else:
#         #     eggs2 = 0
#         #     while tmp >= 15:
#         #         eggs2 += 1
#         #         tmp = tmp - 16
#         #     answer.appendleft(tmp)
#
#     for _ in range(len(answer)):
#         n = answer.pop()
#         for d in my_connector:
#             if my_connector[d] == n:
#                 answer.appendleft(d)
#
#     return answer


print('Сложение')
print(hex_sum(input('Первое шестнадцатиричное число '), input('Второе шестнадцатиричное число ')))

#print('Умножение')
#print(hex_mlt(input('Первое шестнадцатиричное число '), input('Второе шестнадцатиричное число ')))
