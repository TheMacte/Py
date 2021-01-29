"""
 2. Во втором массиве сохранить индексы четных элементов первого массива.
 Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
 второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
 т.к. именно в этих позициях первого массива стоят четные числа.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)
spam = []

# Логичный способ, на больших данных оказался быслрее Питоновского
for i, num in enumerate(array):
    if num % 2 == 0:
        spam.append(i)

# Питоновский способ
# spam = [i for i, x in enumerate(array) if x % 2 == 0]
print(spam)
