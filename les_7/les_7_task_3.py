"""
3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным
образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий
его на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это
слишком сложно, используйте метод сортировки, который не рассматривался на
уроках (сортировка слиянием также недопустима).
"""
import random


def gnome_sort(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data


m = int(input('Введитте целое число ддя определения размера массива: '))
SIZE = 2 * m + 1
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

sorted_array = gnome_sort(array)
i = len(array) // 2
median = sorted_array[i]

print(f'{median = }')
print(sorted(array))
