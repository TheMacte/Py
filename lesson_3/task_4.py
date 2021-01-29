"""
 4. Определить, какое число в массиве встречается чаще всего.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

assert SIZE >= 1, 'Только для SIZE >= 1'
# Если 2 числа будут встречаться максимальное количество раз, то будет выдано только одно.

nums = list(set(array))
cnt = [0]*len(nums)
max_id = 0

for n in array:
    for i, num in enumerate(nums):
        if n == num:
            cnt[i] += 1

max_cnt = cnt[0]

for i, n in enumerate(cnt):
    if n > max_cnt:
        max_cnt = n
        max_id = i

print(f'число {nums[max_id]} встречается максимально часто в массиве {array}')
