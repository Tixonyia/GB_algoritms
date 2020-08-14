# https://drive.google.com/file/d/1t9zURmW15RtbXv1gXkw6Hr_j_6gCyh8I/view?usp=sharing

"""2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""

num = int(input('Введите натуральное число: '))
res_1 = 0
res_2 = 0

while num > 0:
    if num % 2 == 0:
        res_2 += 1

    else:
        res_1 += 1
    num = num // 10

print(f'Нечётных: {res_1}, чётных: {res_2}.')
