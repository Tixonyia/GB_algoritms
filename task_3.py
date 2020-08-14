# https://drive.google.com/file/d/1t9zURmW15RtbXv1gXkw6Hr_j_6gCyh8I/view?usp=sharing

"""3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
если введено число 3486, надо вывести 6843."""

num = int(input('Введите натуральное число: '))
result = 0

while num > 0:
    result = result * 10 + num % 10
    num = num // 10

print(f'Результат: {result}')