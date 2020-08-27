"""1. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры."""

import sys


def version_1(n):
    total = 0
    num = 1
    for i in range(0, n):
        total += num
        num = num * (-0.5)
    return locals()


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

    return locals()


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
    return locals()


def version_4(n):
    total = (((-0.5) ** (n - 1)) * (-0.5) - 1) / ((-0.5) - 1)
    return locals()


def show(x, total):
    total.append(sys.getsizeof(x))
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show(key, total)
                show(value, total)
        elif not isinstance(x, str):
            for item in x:
                show(item, total)
    return f'Сумма занимаемой памяти: {sum(total)}({sum(total) - 248}). Из них 248 это словарь локальных переменных.'


print(show(version_1(10), total=[]))
"""type=<class 'dict'>, size=248, obj={'n': 10, 'total': 0.666015625, 'num': 0.0009765625, 'i': 9}
type=<class 'str'>, size=50, obj=n
type=<class 'int'>, size=28, obj=10
type=<class 'str'>, size=54, obj=total
type=<class 'float'>, size=24, obj=0.666015625
type=<class 'str'>, size=52, obj=num
type=<class 'float'>, size=24, obj=0.0009765625
type=<class 'str'>, size=50, obj=i
type=<class 'int'>, size=28, obj=9
Сумма занимаемой памяти: 558. Из них 248 это словарь локальных переменных.
"""

print(show(version_2(10), total=[]))
"""type=<class 'dict'>, size=248, obj={'n': 10, 'total': 0, 'recursion': <function version_2.<locals>.recursion at 0x7fc2b58c3d40>}
type=<class 'str'>, size=50, obj=n
type=<class 'int'>, size=28, obj=10
type=<class 'str'>, size=54, obj=total
type=<class 'int'>, size=24, obj=0
type=<class 'str'>, size=58, obj=recursion
type=<class 'function'>, size=144, obj=<function version_2.<locals>.recursion at 0x7fc2b58c3d40>
Сумма занимаемой памяти: 606. Из них 248 это словарь локальных переменных."""

print(show(version_3(10), total=[]))
"""type=<class 'dict'>, size=248, obj={'n': 1, 'list_progression': [-0.001953125, 0.00390625, -0.0078125, 0.015625, -0.03125, 0.0625, -0.125, 0.25, -0.5, 1.0], 'num': 1, 'total': 0.666015625, 'i': 1.0}
type=<class 'str'>, size=50, obj=n
type=<class 'int'>, size=28, obj=1
type=<class 'str'>, size=65, obj=list_progression
type=<class 'list'>, size=200, obj=[-0.001953125, 0.00390625, -0.0078125, 0.015625, -0.03125, 0.0625, -0.125, 0.25, -0.5, 1.0]
type=<class 'float'>, size=24, obj=-0.001953125
type=<class 'float'>, size=24, obj=0.00390625
type=<class 'float'>, size=24, obj=-0.0078125
type=<class 'float'>, size=24, obj=0.015625
type=<class 'float'>, size=24, obj=-0.03125
type=<class 'float'>, size=24, obj=0.0625
type=<class 'float'>, size=24, obj=-0.125
type=<class 'float'>, size=24, obj=0.25
type=<class 'float'>, size=24, obj=-0.5
type=<class 'float'>, size=24, obj=1.0
type=<class 'str'>, size=52, obj=num
type=<class 'int'>, size=28, obj=1
type=<class 'str'>, size=54, obj=total
type=<class 'float'>, size=24, obj=0.666015625
type=<class 'str'>, size=50, obj=i
type=<class 'float'>, size=24, obj=1.0
Сумма занимаемой памяти: 1063. Из них 248 это словарь локальных переменных."""

print(show(version_4(10), total=[]))
"""type=<class 'dict'>, size=248, obj={'n': 10, 'total': 0.666015625}
type=<class 'str'>, size=50, obj=n
type=<class 'int'>, size=28, obj=10
type=<class 'str'>, size=54, obj=total
type=<class 'float'>, size=24, obj=0.666015625
Сумма занимаемой памяти: 404. Из них 248 это словарь локальных переменных.
"""

"""Вывод.

Выбрал задачу которую делал на тест времени исполнения
для комбинированного сравнения временем выполнения и обьёма занимаемой памяти.

Четвёртый способ опять в расчёт не берём(чистая математика что с неё взять, она крута.)

Первое место поделили функция 1 и 2. Небольшое количество постоянно перебираемых переменных.
Однако надо помнить, что функция номер два(с рекурсией) имеет крайне медленную скорость на большом
количетве данных. Так что номер функция номер один наш фаворит!!!

Функция номер три занимае значительное количество памяти относительно первых двух. И этот показатель
будет рости с увеличением количества данных (наличие словаря). Однако ели встанет задаче вычислить
уже найденный член прогрессии, минус превратиться в плюс)
"""