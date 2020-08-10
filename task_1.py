# https://drive.google.com/file/d/1SD-cJh9KIadtAGhpSOXfHvuJsbK8XMk_/view?usp=sharing

"""Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь."""

a = int(input('Введите трёхзначное число: '))
s1 = a // 100
s2 = a % 100 // 10
s3 = a % 10
summ = s1 + s2 + s3
mul = s1 * s2 * s3
print(f'Cумма =  {summ}, произведение = {mul}')