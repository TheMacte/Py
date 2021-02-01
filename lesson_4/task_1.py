"""
  1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
  Примечание. Идеальным решением будет:
  ● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
  ● написать 3 варианта кода (один у вас уже есть),
  ● проанализировать 3 варианта и выбрать оптимальный,
  ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
  ● написать общий вывод: какой из трёх вариантов лучше и почему.
"""

"""
 Урок 3, задача 3
 Потому, что именно в ней у меня было допущено много ошибок (работа над ошибками).
"""
import sys
import timeit
import cProfile

# Исходный вариант (с исправлениями)
import random


def main(n):  # Упаковываю задачу в функцию, для облегчения работы с ней
    size = n  # Здесь это переменная, но в оригинальном коде это константы
    min_item = 0  # Здесь это переменная, но в оригинальном коде это константы
    max_item = 100  # Здесь это переменная, но в оригинальном коде это константы
    array = [random.randint(min_item, max_item) for _ in range(size)]

    id_max, id_min = 0, 0
    value_max, value_min = array[0], array[0]

    for i, num in enumerate(array):
        if num > value_max:
            value_max = num
            id_max = i
        if num < value_min:
            value_min = array[i]
            id_min = i

    array[id_max], array[id_min] = array[id_min], array[id_max]

    return array

# print(timeit.timeit('main(100)', number=100, globals=globals()))  # 0.007690101999287435
# print(timeit.timeit('main(200)', number=100, globals=globals()))  # 0.01483299400024407
# print(timeit.timeit('main(400)', number=100, globals=globals()))  # 0.02737550799974997
# print(timeit.timeit('main(800)', number=100, globals=globals()))  # 0.05330492999928538

# cProfile.run('main(1_000_000)')
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    1.426    1.426 <string>:1(<module>)
  1000000    0.438    0.000    0.927    0.000 random.py:200(randrange)
  1000000    0.233    0.000    1.160    0.000 random.py:244(randint)
  1000000    0.350    0.000    0.489    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.062    0.062    1.425    1.425 task_1.py:17(main)
        1    0.203    0.203    1.364    1.364 task_1.py:21(<listcomp>)
        1    0.000    0.000    1.426    1.426 {built-in method builtins.exec}
  1000000    0.057    0.000    0.057    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1267575    0.083    0.000    0.083    0.000 {method 'getrandbits' of '_random.Random' objects}
"""


def main2(n):  # выворачивую через рекурсию
    size = n
    min_item = 0
    max_item = 100
    array = [random.randint(min_item, max_item) for _ in range(size)]

    def id_max_id_min(arr, cnt=0, id_max=0, id_min=0, value_max=0, value_min=0):
        if cnt == len(arr):
            return id_max, id_min
        else:
            if cnt == 0:
                value_max = arr[0]
                value_min = arr[0]
            if arr[cnt] > value_max:
                value_max = arr[cnt]
                id_max = cnt
            if arr[cnt] < value_min:
                value_min = arr[cnt]
                id_min = cnt
            cnt += 1
            return id_max_id_min(arr, cnt, id_max, id_min, value_max, value_min)

    id_mx, id_mn = id_max_id_min(array)
    array[id_mx], array[id_mn] = array[id_mn], array[id_mx]
    return array


# print(timeit.timeit('main2(100)', number=100, globals=globals()))  # 0.0096767879986146
# print(timeit.timeit('main2(200)', number=100, globals=globals()))  # 0.019719559999430203
# print(timeit.timeit('main2(400)', number=100, globals=globals()))  # 0.035659070999827236
# print(timeit.timeit('main2(800)', number=100, globals=globals()))  # 0.07222636599908583


"""
sys.setrecursionlimit(10_000) # для проведения замеров, значение больше ой компьютер не воспринимает
cProfile.run('main2(10_000)')
sys.setrecursionlimit(998)

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.025    0.025 <string>:1(<module>)
    10000    0.004    0.000    0.010    0.000 random.py:200(randrange)
    10000    0.003    0.000    0.012    0.000 random.py:244(randint)
    10000    0.004    0.000    0.005    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.025    0.025 task_1.py:61(main2)
        1    0.002    0.002    0.014    0.014 task_1.py:65(<listcomp>)
  10001/1    0.010    0.000    0.011    0.011 task_1.py:67(id_max_id_min)
        1    0.000    0.000    0.025    0.025 {built-in method builtins.exec}
    10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12595    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

"""


def main3(n):
    size = n
    min_item = 0
    max_item = 100
    array = [random.randint(min_item, max_item) for _ in range(size)]
    array[array.index(max(array))], array[array.index(min(array))] = array[array.index(min(array))], array[array.index(max(array))]

    return array

#
# print(timeit.timeit('main3(100)', number=100, globals=globals()))  # 0.008066536000114866
# print(timeit.timeit('main3(200)', number=100, globals=globals()))  # 0.015032216999316006
# print(timeit.timeit('main3(400)', number=100, globals=globals()))  # 0.026853510000364622
# print(timeit.timeit('main3(800)', number=100, globals=globals()))  # 0.05211360900102591


"""
cProfile.run('main3(1_000_000)')

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    1.386    1.386 <string>:1(<module>)
  1000000    0.429    0.000    0.911    0.000 random.py:200(randrange)
  1000000    0.230    0.000    1.141    0.000 random.py:244(randint)
  1000000    0.345    0.000    0.482    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    1.385    1.385 task_1.py:115(main3)
        1    0.197    0.197    1.338    1.338 task_1.py:119(<listcomp>)
        1    0.000    0.000    1.386    1.386 {built-in method builtins.exec}
        2    0.027    0.013    0.027    0.013 {built-in method builtins.max}
        2    0.019    0.010    0.019    0.010 {built-in method builtins.min}
  1000000    0.056    0.000    0.056    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1267101    0.081    0.000    0.081    0.000 {method 'getrandbits' of '_random.Random' objects}
        4    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""


# РЕЗУЛЬТАТ АНАЛИЗА
"""
Везде замеры проводились с N = 100, 200, 400, 800
O(1) - линейное, т.к. с увеличением N в 2 раза время выполнения увеличивалось примерно в двое
Простой цикл показал время близкое к использованию встроенных функций.
Рекурсия показала заметно худшее время выполнения.
Замеры cProfile не показывают каких либо мест, которые можно улучшить, т.к. cProfile бъёт выполняемый од по функциям.    

Для данной задачи лучшим решением является main3(n), так как по быстродействию он практически идентичен циклу,
но значительно проще в написании.
"""
