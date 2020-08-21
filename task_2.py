import timeit
import cProfile


def sieve(i):
    n = i * 18

    sieve = [k for k in range(n)]
    sieve[1] = 0

    for k in range(2, n):
        if sieve[k] != 0:
            j = k + k
            while j < n:
                sieve[j] = 0
                j += k

    res = [k for k in sieve if k != 0]

    return res[i - 1]


print(timeit.timeit('sieve(10)', number=100, globals=globals()))  # 0.010373723000157042
print(timeit.timeit('sieve(100)', number=100, globals=globals()))  # 0.12000668900054734
print(timeit.timeit('sieve(1000)', number=100, globals=globals()))  # 1.1920933030005472
print(timeit.timeit('sieve(10000)', number=100, globals=globals()))  # 12.247805709000204

cProfile.run('sieve(10000)')
"""        6 function calls in 0.121 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.121    0.121 <string>:1(<module>)
        1    0.009    0.009    0.009    0.009 task_2.py:18(<listcomp>)
        1    0.098    0.098    0.119    0.119 task_2.py:5(sieve)
        1    0.012    0.012    0.012    0.012 task_2.py:8(<listcomp>)
        1    0.000    0.000    0.121    0.121 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""


def not_sieve(i):
    j = i * 18
    res = []
    for n in range(2, j + 1):
        for x in res:
            if n % x == 0:
                break
        else:
            res.append(n)

    return res[i - 1]


print(timeit.timeit('not_sieve(10)', number=100, globals=globals()))  # 0.010768428999654134
print(timeit.timeit('not_sieve(100)', number=100, globals=globals()))  # 0.38583308899978874
print(timeit.timeit('not_sieve(1000)', number=100, globals=globals()))  # 21.01702712400038


cProfile.run('not_sieve(1000)')
"""2068 function calls in 0.211 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.211    0.211 <string>:1(<module>)
        1    0.210    0.210    0.211    0.211 task_2.py:42(not_sieve)
        1    0.000    0.000    0.211    0.211 {built-in method builtins.exec}
     2064    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""


"""Вывод.
Древние +1, я 0).
Основное время с решетом 'съедает' лишь добавление элементо и одноразовый перебор списка с исключением
'дырок'. Функция линейна.
Благодаря двойной вложености и неоднакратному перебору списка в моём варианте, на вычислениях на 10000 
я недождался ответа и за 10 минут. Функция похожа на квадратичную.
Мыслители рулят.
"""

