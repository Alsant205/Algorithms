"""
5. Пользователь вводит две буквы. Определить, на каких местах
алфавита они стоят, и сколько между ними находится букв.
"""

print('Введите две буквы, после каждой нажмите ENTER')
a, b = input(), input()
a1, b1 = ord(a), ord(b)
if a == b:
    print(f'Обе буквы одинаковы\n'
          f'Порядковый номер {a} = {a1 - 96}\n')
else:
    c = max(a1, b1) - min(a1, b1) - 1
    print(f'Порядковый номер {a} = {a1 - 96}\n'
          f'Порядковый номер {b} = {b1 - 96}\n'
          f'Букв между ними - {abs(c)}')
