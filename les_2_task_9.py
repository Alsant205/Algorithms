"""
9. Среди натуральных чисел, которые были введены, найти наибольшее
по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def summator(num, digit_1=0, digit_2=0):
    digit_1 = num % 10
    num = num // 10
    digit_2 = num % 10
    num = num // 10
    total = digit_1 + digit_2
    if num == 0:
        return total
    else:
        result = summator(num, digit_1, digit_2)
        return result + total


print('Введите натуральные числа.\n'
      'После каждого числа нажмите ENTER.\n'
      'Для окончания ввода введите 0')
number = ''  # числа вводимые пользователем
biggest = 0  # для хранения суммы цифр наибольшего числа
current_num = ''
summ = ''
while number != 0:
    number = int(input())
    if number == 0 and biggest == 0:
        print(f'Вы ничего не ввели')
    else:
        summ = summator(number)
        if biggest < summ:
            biggest = summ
            current_num = number
print(f'\nНаибольшее по сумме цифр {current_num}, сумма = {biggest}')
