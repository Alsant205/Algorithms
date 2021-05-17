"""
3. Сформировать из введенного числа обратное по порядку входящих в
него цифр и вывести на экран. Например, если введено число 3486,
надо вывести 6843.
"""


def revers_num(num, new_num=''):
    if num == 0:
        return new_num
    else:
        digit = num % 10
        num = num // 10
        if len(str(num)) == 1:
            new_num = new_num + str(digit) + str(num)
            return new_num
        else:
            new_num = new_num + str(digit)
            result = revers_num(num, new_num)
            return result


number = int(input('Введите число больше 9: '))
print(revers_num(number))
