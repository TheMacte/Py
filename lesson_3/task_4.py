"""
 4. Определить, какое число в массиве встречается чаще всего.
"""
Перепроверить, что я тут накрутил!

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)
# Если 2 числа будут встречаться максимальное количество раз, то будет выдано только одно.
# Миниальный размер SIZE = 1

nums = list(set(array))
cnt = [0]*len(nums)
max_id = 0

for n in array:
    for i, num in enumerate(nums):
        if n == num:
            cnt[i] += 1

for i, max_n in enumerate(cnt):
    if i == len(cnt) - 1:
        break
    if max_n > cnt[i + 1]:
        max_id = i

print(nums[max_id])
