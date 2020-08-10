# https://drive.google.com/file/d/1SD-cJh9KIadtAGhpSOXfHvuJsbK8XMk_/view?usp=sharing
"""По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
 проходящей через эти точки"""

x1 = float(input('Введите x для первой точки: '))
y1 = float(input('Введите y для первой точки: '))
x2 = float(input('Введите x для второй точки: '))
y2 = float(input('Введите y для второй точки: '))

if x1 == x2:
    print('Прямая не принадлежит виду  y = kx + b')

else:
    k = int((y1 - y2) / (x1 - x2))
    b = int(y1 - k * x1)
    print(f'y = {k} * x + {b}')