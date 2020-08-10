# https://drive.google.com/file/d/1SD-cJh9KIadtAGhpSOXfHvuJsbK8XMk_/view?usp=sharing
"""Вводятся три разных числа.
 Найти, какое из них является средним (больше одного, но меньше другого)."""

a = float(input('Введите первое число: '))
b = float(input('Введите второе число, неравное первому: '))
c = float(input('Введите третье число, неравное первым двум: '))

if a > b and a > c:
    if b > c:
        print(f'Среднее из значений: {b}')
    else:
        print(f'Среднее из значений: {c}')

elif b > a and b > c:
    if a > c:
        print(f'Среднее из значений: {a}')
    else:
        print(f'Среднее из значений: {c}')

else:
    if b > a:
        print(f'Среднее из значений: {b}')
    else:
        print(f'Среднее из значений: {a}')