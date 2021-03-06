"""
1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
 заданный случайными числами на промежутке [-100; 100).
  Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99


def decreasing_bubble(arr):
    """
    Улучшение - проверка, на местах ли самое большое и самое малое значения.

    Если да, то количество проходов можно уменьшить, а также в каждой итерации можно не проверять на своём ли
    месте самые крайние значения. Т.к. min и max реализованиы на Си, то они работают быстрее. В худщем случае
    тратятся 2 очень быстрых прохода, в лучшем экономится 2 прохода на питоне и немного в каждой итерации (минус
    проверка первого и последнего). На небольших массивах в % это много, во времени не ощутимо, на больших масивах в % мало, но кое-что.
    """
    if len(arr) == 1:
        return arr
    n = 1
    if arr[0] == max(arr):
        n += 1
        has_max = True
    else:
        has_max = False
    if arr[len(arr) - 1] == min(arr):
        n += 1
        has_min = True
    else:
        has_min = False
    if len(arr) > 2:
        start = 1 if has_max else 0
        finish = len(arr) - 2 if has_min else len(arr) - 1
        while n < len(arr):
            for j in range(start, finish):
                if arr[j + 1] > arr[j]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            n += 1
    return arr


rnd_arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(rnd_arr)
print(decreasing_bubble(rnd_arr))
