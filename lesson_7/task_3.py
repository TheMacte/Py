"""
3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки,
который не рассматривался на уроках (сортировка слиянием также недопустима).
"""
from random import randint

MIN_ITEM = 0
MAX_ITEM = 50


def median(arr) -> int:
    if len(arr) == 1:
        return arr[0]
    arr.remove(max(arr))  # альтернатива на каждой рекурсии прогонять массив через цикл и искать болшее и меньшее
    arr.remove(min(arr))
    return median(arr)


m = int(input('Введите m '))
rnd_arr = [randint(MIN_ITEM, MAX_ITEM) for _ in range(2 * m + 1)]

print(rnd_arr)
print(median(rnd_arr))
