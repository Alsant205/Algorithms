import cProfile
import timeit

"""
1). Проанализировать скорость и сложность одного любого алгоритма
из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите
в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом
(не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""

"""
урок 2 задача 3. Сформировать из введенного числа обратное по порядку 
входящих в него цифр и вывести на экран. Например, если введено 
число 3486, надо вывести 6843.
"""


# первый релиз
def revers_num_1(num, new_num=''):
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
            result = revers_num_1(num, new_num)
            return result


# второй релиз
def revers_num_2(num, new_num=''):
    if num == 0:
        return new_num
    while num != 0:
        digit = num % 10
        num = num // 10
        new_num = new_num + str(digit)
    return new_num


# третий релиз
def revers_num_3(num):
    new_num = int()
    for _ in range(len(str(num))):
        new_num = num % 10 + new_num * 10
        num //= 10
    return new_num


# print(timeit.timeit('revers_num_1(123456789 ** 1)', number=1000, globals=globals()))
# print(timeit.timeit('revers_num_1(123456789 ** 20)', number=1000, globals=globals()))
# print(timeit.timeit('revers_num_1(123456789 ** 40)', number=1000, globals=globals()))
# print(timeit.timeit('revers_num_1(123456789 ** 60)', number=1000, globals=globals()))
# print(timeit.timeit('revers_num_1(123456789 ** 80)', number=1000, globals=globals()))
# print(timeit.timeit('revers_num_1(123456789 ** 100)', number=1000, globals=globals()))
# print(timeit.timeit('revers_num_1(123456789 ** 120)', number=1000, globals=globals()))

"""
На значениях выше 120 происходит переполнение стека. Поэтому 
алгоритм представляется неподходящим для работы с большими числами.
Так же на одинаковых значениях в сравнении с другими  алгаритмами, 
этот отрабатывает более чем в три раза дольше
"""
# 0.012570651000000002  1
# 0.47108525799999995   20
# 0.773620302           40
# 1.5625264239999999    60
# 3.6487483670000005    80
# 5.023987394000001     100
# 7.292783477           120


# print(timeit.timeit('revers_num_2(123456789 ** 1)', number=1000, globals=globals()))
# print(timeit.timeit('revers_num_2(123456789 ** 50)', number=1000, globals=globals()))
# print(timeit.timeit('revers_num_2(123456789 ** 100)', number=1000, globals=globals()))
# print(timeit.timeit('revers_num_2(123456789 ** 150)', number=1000, globals=globals()))
# print(timeit.timeit('revers_num_2(123456789 ** 200)', number=1000, globals=globals()))
# print(timeit.timeit('revers_num_2(123456789 ** 250)', number=1000, globals=globals()))
# print(timeit.timeit('revers_num_2(123456789 ** 300)', number=1000, globals=globals()))

# 0.005124322999999993  1
# 0.596701238           50
# 1.349278679           100
# 3.106351531           150
# 4.586539334           200
# 6.941688925000001     250
# 9.939764439000001     300

# доппроверка
# print(timeit.timeit('revers_num_2(123456789 ** 2000)', number=1000, globals=globals()))
# 94.71317611299999     1000
# 212.665187866         1500
# 380.747185138         2000


# print(timeit.timeit('revers_num_3(123456789 ** 1)', number=1000, globals=globals()))
# print(timeit.timeit('revers_num_3(123456789 ** 50)', number=1000, globals=globals()))
# print(timeit.timeit('revers_num_3(123456789 ** 100)', number=1000, globals=globals()))
# print(timeit.timeit('revers_num_3(123456789 ** 150)', number=1000, globals=globals()))
# print(timeit.timeit('revers_num_3(123456789 ** 200)', number=1000, globals=globals()))
# print(timeit.timeit('revers_num_3(123456789 ** 250)', number=1000, globals=globals()))
# print(timeit.timeit('revers_num_3(123456789 ** 300)', number=1000, globals=globals()))

# 0.003912779999999991  1
# 0.44594931800000004   50
# 1.254129437           100
# 2.6077661050000005    150
# 4.647830958000001     200
# 7.259295927           250
# 10.373958621000003    300

# доппроверка
# print(timeit.timeit('revers_num_3(123456789 ** 2000)', number=1000, globals=globals()))
# 104.359506398         1000
# 229.626408116         1500
# 407.50547225699995    2000


"""
Все три алгоритма получилось сравнить только на значении в степени 
100, это показало что алгоритм с рекурсией не только неработоспособен 
с бОльшими числами (из-за переполнения стека на степени выше 120),
но и в 3,5 раза дольше работает. Из двух оставшихся лушее время 
показал второй алгоритм, с использованием цикла while хотя и с 
небольшой разницей. 
У всех вариантов наблюдается квадратичная асимптотика 
"""

"""
Проверка с помощью cProfile показала что цикл while (0.187 секунды) 
работает в два раза быстрее чем цикл for (0.347 секунды).
Соответственно оптимальным алгоритмом является второй, с 
использованием цикла while.
"""

# cProfile.run('revers_num_1(123456789 ** 120)')
# тестируем на значении в степени 120

#       1943 function calls (974 primitive calls) in 0.018 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.018    0.018 <string>:1(<module>)
#  970/1    0.018    0.000    0.018    0.018 les_4_task_1.py:24(revers_num_1)
#      1    0.000    0.000    0.018    0.018 {built-in method builtins.exec}
#    970    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('revers_num_2(123456789 ** 1200)')
# тестируем на значении в степени 1200

#       4 function calls in 0.187 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.187    0.187 <string>:1(<module>)
#      1    0.187    0.187    0.187    0.187 les_4_task_1.py:40(revers_num_2)
#      1    0.000    0.000    0.187    0.187 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('revers_num_3(123456789 ** 1200)')
# тестируем на значении в степени 1200

#       5 function calls in 0.347 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.001    0.347    0.347 <string>:1(<module>)
#      1    0.347    0.347    0.347    0.347 les_4_task_1.py:51(revers_num_3)
#      1    0.000    0.000    0.347    0.347 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
