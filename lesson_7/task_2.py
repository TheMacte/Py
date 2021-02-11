"""
2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50


def merge_sort(arr):

    def _merge(in_first, in_second):
        first_i = 0   # Итератор для первого масива
        second_i = 0  # Итератор для второго масива
        cat_array = []

        while (first_i < len(in_first)) and (second_i < len(in_second)):
            if in_first[first_i] < in_second[second_i]:
                cat_array.append(in_first[first_i])
                first_i += 1
            else:
                cat_array.append(in_second[second_i])
                second_i += 1

        while first_i < len(first):
            cat_array.append(first[first_i])
            first_i += 1

        while second_i < len(second):
            cat_array.append(second[second_i])
            second_i += 1

        return cat_array

    if len(arr) == 1:
        return arr
    else:  # Можно убрать, но так читается легче.
        mid = len(arr) // 2
        first = arr[:mid]
        second = arr[mid:]

        return _merge(merge_sort(first), merge_sort(second))


rnd_arr = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(rnd_arr)
print(merge_sort(rnd_arr))
