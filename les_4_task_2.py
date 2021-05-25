import cProfile
import timeit
"""
2). Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход
натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из
прошлых уроков. Используйте этот код и попробуйте его
улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
"""


def divider_counter(n):
    # определяем, простое число или нет
    count = 1
    devider = n
    while devider > 1:
        if n % devider == 0:
            count += 1
        if count > 2:
            return False
        devider -= 1
    return True


# num = int(input('Какое по порядку простое требуется? '))
# sieve = []  # для хранения списка простых чисел
# limit = 0
# # генерируем список простых чисел для заданного порядкового
# next_number = 2
# while limit < num:
#     if divider_counter(next_number) is True:
#         sieve.append(next_number)
#         limit += 1
#     next_number += 1
#
# print(f'sieve({num})-> {sieve.pop()}')

def sieve(n):
    sieve_num = 0  # для хранения найденного простого чисела
    limit = 0
    # ищем простое число для заданного порядкового
    next_number = 2
    while limit < n:
        if divider_counter(next_number) is True:
            sieve_num = next_number
            limit += 1
        next_number += 1
    return sieve_num


# num = int(input('Какое по порядку простое требуется? '))
# print(f'\nsieve({num})-> {sieve(num)}')

# print(timeit.timeit('sieve(10)', number=1000, globals=globals()))
# print(timeit.timeit('sieve(20)', number=1000, globals=globals()))
# print(timeit.timeit('sieve(30)', number=1000, globals=globals()))
# print(timeit.timeit('sieve(40)', number=1000, globals=globals()))
# print(timeit.timeit('sieve(50)', number=1000, globals=globals()))
# print(timeit.timeit('sieve(60)', number=1000, globals=globals()))
# print(timeit.timeit('sieve(70)', number=1000, globals=globals()))
# print(timeit.timeit('sieve(80)', number=1000, globals=globals()))

# 0.087338495           10
# 0.33939972400000007   20
# 0.470898174           30
# 1.2340523680000002    40
# 2.0584841410000005    50
# 2.7922384319999995    60
# 4.263686463           70
# 6.059666536999998     80

# cProfile.run('sieve(1000)')
#
#    6136 function calls in 1.857 seconds
#
#    Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    1.857    1.857 <string>:1(<module>)
#   6132    1.849    0.000    1.849    0.000 les_4_task_2.py:16(divider_counter)
#      1    0.009    0.009    1.857    1.857 les_4_task_2.py:42(sieve)
#      1    0.000    0.000    1.857    1.857 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
Анализ сложности показывает что основные затраты возникают при 
проверке делителей во время поиска простого числа, которая 
проводится в функции divider_counter. Значит именно это частькода
нужно оптимизировать.
"""

"""
# Эратосфен - 5 баллов методистам за имена переменных
n = int(input("вывод простых чисел до числа ... "))
a = [0] * n  # создание массива с n количеством элементов
for i in range(n):  # заполнение массива ...
    a[i] = i  # значениями от 0 до n-1

# вторым элементом является единица, которую не считают простым числом
# забиваем ее нулем.
a[1] = 0

m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
while m < n:  # перебор всех элементов до заданного числа
    if a[m] != 0:  # если он не равен нулю, то
        j = m * 2  # увеличить в два раза (текущий элемент - простое число)
        while j < n:
            a[j] = 0  # заменить на 0
            j = j+m  # перейти в позицию на m больше
    m += 1

# вывод простых чисел на экран (может быть реализован как угодно)
b = []
for i in a:
    if a[i] != 0:
        b.append(a[i])
del a
print(b)
"""
