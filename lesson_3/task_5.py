"""
 5. В массиве найти максимальный отрицательный элемент.
 Вывести на экран его значение и позицию в массиве.
 Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
 Это два абсолютно разных значения.
"""
Тут тоже что-то не то

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)
spam = []

for i, num in enumerate(array):
    if len(spam) == 0 and num < 0:
        spam.append(i)
        spam.append(num)
    elif len(spam) == 2 and 0 > num > spam[1]:
        spam[0] = i
        spam[1] = num

print(f'Индекс: {spam[0]}, Значение {spam[1]}')
