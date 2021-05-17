"""
8. Посчитать, сколько раз встречается определенная цифра в
введенной последовательности чисел. Количество вводимых чисел
и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def digit_checker(object_num, digit):
    digit_count = int()
    for i in object_num:
        if i == digit:
            digit_count += 1
    return digit_count


target_num = input('Искомая цифра? от 0 до 9: ')
quantity = int(input('Сколько чисел проверяем? '))
print('Введите число')
counter = int()
while quantity > 0:
    print(f'Осталось ввести чисел - {quantity}')
    num = input()
    result = digit_checker(num, target_num)
    counter += result
    quantity -= 1

print(f'Цифра {target_num} встретилась {counter} раз')


