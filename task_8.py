# https://drive.google.com/file/d/1t9zURmW15RtbXv1gXkw6Hr_j_6gCyh8I/view?usp=sharing

"""8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры."""

numer = int(input('Введите цифру: '))
quantity = int(input('Введите количество чисел: '))
total = 0


def count_numer(total, num):
    while num > 0:
        if num % 10 == numer:
            total += 1
        num = num // 10
    return total


for i in range(0, quantity):
    num = int(input('Введите число: '))
    total = count_numer(total, num)

print(f'Цифра {numer} встречается {total} раз.')