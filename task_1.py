"""4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры."""
import timeit
import sys
import cProfile
sys.setrecursionlimit(15000)


def version_1(n):
    total = 0
    num = 1
    for i in range(0, n):
        total += num
        num = num * (-0.5)
    return total


print(timeit.timeit('version_1(10)', number=100, globals=globals()))  # 0.0001520080004411284
print(timeit.timeit('version_1(100)', number=100, globals=globals()))  # 0.001075336000212701
print(timeit.timeit('version_1(1000)', number=100, globals=globals()))  # 0.02208938499825308
print(timeit.timeit('version_1(10000)', number=100, globals=globals()))  # 0.11081997099972796
cProfile.run('version_1(10000)')
"""        4 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 task_1.py:9(version_1)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


def version_2(n):
    total = 0

    def recursion(total, n):
        if n == 1:
            total += 1
            return total
        else:
            total += (-0.5) ** (n - 1)
            n = n - 1
            return recursion(total, n)

    return recursion(total, n)


print(timeit.timeit('version_2(10)', number=100, globals=globals()))  # 0.0005996940017212182
print(timeit.timeit('version_2(100)', number=100, globals=globals()))  # 0.005675541000528028
print(timeit.timeit('version_2(1000)', number=100, globals=globals()))  # 0.10174595300122746
print(timeit.timeit('version_2(10000)', number=100, globals=globals()))  # 1.2910935040017648
cProfile.run('version_2(10000)')

"""
         10004 function calls (5 primitive calls) in 0.016 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.016    0.016 <string>:1(<module>)
        1    0.000    0.000    0.016    0.016 task_1.py:24(version_2)
  10000/1    0.016    0.000    0.016    0.016 task_1.py:27(recursion)
        1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


def version_3(n):
    list_progression = []
    num = 1
    total = 0
    while True:
        if n == num:
            list_progression.append((-0.5) ** (n - 1))
            break
        else:
            list_progression.append((-0.5) ** (n - 1))
            n = n - 1
    for i in list_progression:
        total += i
    return total


print(timeit.timeit('version_3(10)', number=100, globals=globals()))  # 0.0004950930015183985
print(timeit.timeit('version_3(100)', number=100, globals=globals()))  # 0.004673250998166623
print(timeit.timeit('version_3(1000)', number=100, globals=globals()))  # 0.052834680001978995
print(timeit.timeit('version_3(10000)', number=100, globals=globals()))  # 0.5759949979983503
cProfile.run('version_3(10000)')

"""         10004 function calls in 0.009 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
        1    0.008    0.008    0.009    0.009 task_1.py:45(version_3)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
    10000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


def version_4(n):
    total = (((-0.5) ** (n - 1)) * (-0.5) - 1) / ((-0.5) - 1)
    return total


print(timeit.timeit('version_4(10)', number=100, globals=globals()))  # 5.279999822960235e-05
print(timeit.timeit('version_4(100)', number=100, globals=globals()))  # 5.0590002501849085e-05
print(timeit.timeit('version_4(1000)', number=100, globals=globals()))  # 5.2598999900510535e-05
print(timeit.timeit('version_4(10000)', number=100, globals=globals()))  # 5.6905999372247607e-05
cProfile.run('version_4(10000)')

"""         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_1.py:105(version_4)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

""" Вывод. 

Самым быстрым является код первой функции. Плюс его и в том, что он линеен. 

Второй по скорости код функции номер три (отстаёт примерно в пять раз от фаворита). 
Причина в наличии списка и операций с ним. Так же является линенйной по времени.

Вторая функция работает как вторая на малом количетве данных, но значительно отстаёт при повышении.
График не линеен. Прослеживается квадратичная зависимость ввиду рекурсии.

Четвёртую в вывод не включаю.
 И так понятно практически нулевое константное время выполнения арефметических выражений.
 Графиком, думаю, будет прямая практически перпендикулярная оси времени.
"""