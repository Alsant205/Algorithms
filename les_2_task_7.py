"""
7. Напишите программу, доказывающую или проверяющую, что для
множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""

num = int(input('Введите любое натуральное число: '))
left_sum = int()
right_sum = num * (num + 1) // 2

while num > 0:
    left_sum += num
    num -= 1

if left_sum == right_sum:
    print(f'Равенство выполняется, {left_sum = }, {right_sum = }')
else:
    print(f'Равенство не выполняется, {left_sum = }, {right_sum = }')
