# https://drive.google.com/file/d/18axNWEmjhOimJlqEhiFrJBnEA_Lzq638/view?usp=sharing
"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0)
и 2 нечетные (3 и 5).
"""


def even_odd(num, even=int(), odd=int()):

    if num > 0:
        digit = num % 10
        num = num // 10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        res = even_odd(num, even, odd)
        return res

    if num == 0:
        result = f'четных - {even},\n' \
                 f'нечетных - {odd}'
        return result


number = int(input('Введите натуральное число: '))
print(even_odd(number))

#
# num = 12345
# num, digit = num // 10, num % 10
# print(f'{num = }, {digit = }')
