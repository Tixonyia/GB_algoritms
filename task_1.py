# https://drive.google.com/file/d/1t9zURmW15RtbXv1gXkw6Hr_j_6gCyh8I/view?usp=sharing

"""Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
 Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает
 новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
 Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова
 запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления на ноль,
если он ввел его в качестве делителя."""


def calculator():
    num_1, num_2 = map(float, input('Введите два числа через пробел: ').split())
    sign = input('Введите знак операции("+", "-", "*", "/", "0" - для завершения): ')

    if sign == '0':
        return print('Программа завершена пользователем.')

    while sign != '+' and sign != '-' and sign != '*' and sign != '/':
        print('Вы ввели неверный символ операции!')
        sign = input('Введите знак операции("+", "-", "*", "/", "0" - для завершения): ')

        if sign == '0':
            return print('Программа завершена пользователем.')
    else:
        while sign == '/' and num_2 == 0:
            print('А Марья Ивановна говорит, что на ноль делить нельзя!')
            num_2 = float(input('Введите делитель не равный нулю: '))

        if sign == '+':
            result = f'Результат: {num_1 + num_2}'
        elif sign == '-':
            result = f'Результат: {num_1 - num_2}'
        elif sign == '*':
            result = f'Результат: {num_1 * num_2}'
        elif sign == '/':
            result = f'Результат: {num_1 / num_2}'

        print(result)
        calculator()


calculator()




