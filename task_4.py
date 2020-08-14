# https://drive.google.com/file/d/1t9zURmW15RtbXv1gXkw6Hr_j_6gCyh8I/view?usp=sharing

"""4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры."""

n = int(input('Введите количество суммируемых элементов ряда: '))
summ = 0
num = 1
for i in range(0, n):
    summ += num
    num = num * (-0.5)
print(summ)