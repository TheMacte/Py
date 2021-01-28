"""
 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

# max_min_info = [[id_max, id_min], [value_max, value_min]]
spam = [[0, 0], [MIN_ITEM, MAX_ITEM]]

for i, num in enumerate(array):
    if num > spam[1][0]:
        spam[1][0] = num
        spam[0][0] = i
    if num < spam[1][1]:
        spam[1][1] = num
        spam[0][1] = i

array[spam[0][0]], array[spam[0][1]] = array[spam[0][1]], array[spam[0][0]]

print(spam)
print(array)