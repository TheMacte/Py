"""
 1. В диапазоне натуральных чисел от 2 до 99 определить,
 сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
base_arr = (_ for _ in range(2, 99 + 1))
span_arr = {_ for _ in range(2, 9 + 1)}
answer_arr = [0] * len(span_arr)
for num in base_arr:
    for i, divider in enumerate(span_arr):
        if num % divider == 0:
            answer_arr[i] += 1
print(answer_arr)
