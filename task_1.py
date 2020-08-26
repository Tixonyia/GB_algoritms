"""1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно 
вывести наименования предприятий, чья прибыль выше среднего и ниже среднего."""

from collections import defaultdict

def_firms_dict = defaultdict(list)

count_firms = int(input("Введите количество фирм: "))
a = 1
while a < count_firms + 1:
    name_firm = input(f'Введите название {a}-й фирмы: ')
    n = 1
    profit = 0
    while n < 5:
        profit += float(input(f'Введите прибыль за {n}-й квартал: '))
        n += 1
    total = profit / 4
    def_firms_dict[name_firm].append(total)
    a += 1
total_all = sum(sum(def_firms_dict.values(), [])) / count_firms
print(f'Средняя прибыль за год состовляет: {total_all}.')
higher = [_ for _ in def_firms_dict.keys() if def_firms_dict[_][0] > total_all]
below = [_ for _ in def_firms_dict.keys() if def_firms_dict[_][0] < total_all]
print(f'Отстающие фирмы: {(", ").join(below)}')
print(f'Лидеры: {(", ").join(higher)}')
