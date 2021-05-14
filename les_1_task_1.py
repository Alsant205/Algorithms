# Ссылка на файл со схемами к заданиям
# https://drive.google.com/file/d/1EjeM14iTq4Bc4kR9yS5MpJ76yK02iQOc/view?usp=sharing
"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит
пользователь.
"""

a = input('Введите трехзначное число:')
a = list(a)
b = a.pop()
c = a.pop()
a = a.pop()
print(f'summ = {int(a) + int(b) + int(c)}, ',
      f'mult = {int(a) * int(b) * int(c)}')
