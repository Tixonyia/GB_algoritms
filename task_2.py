"""2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно.
 Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""

from collections import deque


def ten_in_hex(num, num_16):
    hex_list = ['A', 'B', 'C', 'D', 'E', 'F']
    s = num // 16
    numeral = num % 16
    if s <= 15:
        if numeral > 9:
            num_16.appendleft(hex_list[numeral - 10])
        elif s < 10:
            num_16.appendleft(numeral)
        if s > 9:
            num_16.appendleft(hex_list[s - 10])
        elif s < 10:
            num_16.appendleft(s)
        return num_16
    if numeral > 9:
        num_16.appendleft(hex_list[numeral - 10])
    elif numeral < 10:
        num_16.appendleft(numeral)
    return ten_in_hex(s, num_16)


def hex_in_ten(num):
    num_10 = 0
    hex_list = ['A', 'B', 'C', 'D', 'E', 'F']
    for i in range(0, len(num)):
                numeral = num[i]
                if numeral in hex_list:
                    numeral = 10 + hex_list.index(numeral)
                num_10 += int(numeral) * (16 ** (len(num) - (1 + i)))
    return num_10


num_1_16 = list(input("Введите первое шеснадцетиричное число: "))
num_2_16 = list(input("Введите второе шеснадцетиричное число: "))


num_1_10 = hex_in_ten(num_1_16)
num_2_10 = hex_in_ten(num_2_16)

total_sum_10 = num_1_10 + num_2_10
total_mult_10 = num_1_10 * num_2_10

print(list(ten_in_hex(total_sum_10, num_16=deque([]))))
print(list(ten_in_hex(total_mult_10, num_16=deque([]))))



