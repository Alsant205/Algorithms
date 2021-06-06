"""
1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный
и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход
массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться
сортировка пузырьком. Улучшенные версии сортировки, например, расчёской,
шейкерная и другие в зачёт не идут.
"""

# генерируем массив
import random
from timeit import timeit


# исходный алгаритм метода пузырька
def buble_sort_1(data):
    iter_count = (len(data) - 1) * 10
    while iter_count != 0:
        for i in range(len(data) - 1):
            iter_count -= 1
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
    return data


# оптимизированный алгаритм метода пузырька
def buble_sort_2(data):
    for j in range(len(data) - 1, 0, -1):  # уменьшаем размер части для сравненя
        for i in range(j):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
    return data


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

print(buble_sort_1(array))
print(timeit('buble_sort_1(array)', number=1000, globals=globals()))

print(buble_sort_2(array))
print(timeit('buble_sort_2(array)', number=1000, globals=globals()))

