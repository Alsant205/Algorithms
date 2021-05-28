from collections import deque as dq

"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных 
чисел. При этом каждое число представляется как коллекция, элементы которой — 
цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как 
[‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: 
[‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


def hex_transform(a):
    if a == 'A':
        return 10
    elif a == 'B':
        return 11
    elif a == 'C':
        return 12
    elif a == 'D':
        return 13
    elif a == 'E':
        return 14
    elif a == 'F':
        return 15
    else:
        return a


def int_transform(b):
    if b == 10:
        return 'A'
    elif b == 11:
        return 'B'
    elif b == 12:
        return 'C'
    elif b == 13:
        return 'D'
    elif b == 14:
        return 'E'
    elif b == 15:
        return 'F'
    else:
        return b


hex_num_1 = dq(input('Введите первое слогаемое: '))
hex_num_2 = dq(input('Введите второе слогаемое: '))

result = dq()
in_memo = 0
while len(hex_num_1) > 0 or len(hex_num_2) > 0:
    try:
        summand_1 = hex_num_1.pop()
        if summand_1.isalpha():
            summand_1 = hex_transform(summand_1)
    except IndexError:
        summand_1 = 0
    try:
        summand_2 = hex_num_2.pop()
        if summand_2.isalpha():
            summand_2 = hex_transform(summand_2)
    except IndexError:
        summand_2 = 0
    summ = int(summand_1) + int(summand_2) + in_memo
    in_memo = 0
    if summ > 15:
        in_memo = 1
        summ -= 16
    result.appendleft(str(int_transform(summ)))

print(f'сумма = {list(result)}')
