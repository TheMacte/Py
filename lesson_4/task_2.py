"""
2). Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и
возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:

sieve(2)
3
prime(4)
7
sieve(5)
11
prime(1)
2

Примечание по профилированию кода: для получения достоверных результатов при замере времени необходимо исключить/заменить команды print и input в анализируемом коде.
"""
import timeit
import cProfile


def sieve(cnt, n=1000):  # C решетом
    """
    :param cnt: Порядковый номер простого числа
    :param n: Длинна решета
    :return: Значение
    """
    sieve_ = [i for i in range(n)]
    sieve_[1] = 0
    answer = []

    for i in range(2, n):
        if sieve_[i] != 0:
            answer.append(sieve_[i])  # Собираю массив простых чисел
            if len(answer) == cnt:  # Если в массиве достаточно данных,
                return answer[-1]   # то возвращаю ответ
            j = i + i
            while j < n:
                sieve_[j] = 0
                j += i
    return None


# print(timeit.timeit('sieve(21)', number=100, globals=globals()))   # 0.016514300999915577
# print(timeit.timeit('sieve(42)', number=100, globals=globals()))   # 0.01766385600058129
# print(timeit.timeit('sieve(84)', number=100, globals=globals()))   # 0.018462884000655322
# print(timeit.timeit('sieve(168)', number=100, globals=globals()))  # 0.02165336500002013

"""
cProfile.run('sieve(168)')

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_2.py:30(sieve)
        1    0.000    0.000    0.000    0.000 task_2.py:36(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      168    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


def prime(cnt):  # Без
    """
    :param cnt: Порядковый номер простого числа
    :return: Значение
    """

    def _isit(num, arr):  # Функция определяет, является ли число простым, учитывая предыдущие
        if num != 2:
            for d in arr:
                if num % d == 0:
                    return False
        return True

    answer = [2]  # Массив простых чисел
    i = 1  # счётчик
    while len(answer) != cnt:  # Если в массиве достаточно данных, то возвращаю ответ
        if _isit(answer[-1] + i, answer):  # Проверяю является ли элемент простым числом
            answer.append(answer[-1] + i)
            i = 1
        else:
            i += 1
    else:
        return answer[-1]


# print(timeit.timeit('prime(21)', number=100, globals=globals()))   # 0.0031104560002859216
# print(timeit.timeit('prime(42)', number=100, globals=globals()))   # 0.0088886210005512110
# print(timeit.timeit('prime(84)', number=100, globals=globals()))   # 0.0279103840002790100
# print(timeit.timeit('prime(168)', number=100, globals=globals()))  # 0.0859600030007641200

"""
cProfile.run('prime(10_000)')

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.355    2.355 <string>:1(<module>)
        1    0.032    0.032    2.355    2.355 task_2.py:71(prime)
   104727    2.316    0.000    2.316    0.000 task_2.py:77(_isit)
        1    0.000    0.000    2.355    2.355 {built-in method builtins.exec}
   104728    0.006    0.000    0.006    0.000 {built-in method builtins.len}
     9999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# РЕЗУЛЬТАТ АНАЛИЗА
"""
Везде замеры проводились с N = 21, 42, 84, 168 - исходя из того,
 что в решете Эратосфера до 1 000 встречается 168 простых чисел.

В случае с решетом O(n log n) - логорифмическое, время растёт несопоставимо медленнее, чем значение N. 
 Это связанно с тем, что самые большие затраты приходятся на формирование решета.

В класическом случае поиска O(n^n) - время растёт по экспаненте.

Решето ввгоднее, если заранее известно максимальное значение, а искомое число находится ближе к концу решета.

Замеры cProfile не показывают каких либо мест, которые можно улучшить.  
"""
