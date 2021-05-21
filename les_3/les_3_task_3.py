"""
3. В массиве случайных целых чисел поменять местами минимальный и
максимальный элементы.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


'------------ вариант 1 ------------'

min_elem = array[0]
min_elem_pos = 0
max_elem = int()
max_elem_pos = 0
elem_pos = -1
for i in array:
    elem_pos += 1
    if min_elem > i:
        min_elem = i
        min_elem_pos = elem_pos
    if max_elem < i:
        max_elem = i
        max_elem_pos = elem_pos

array_1 = array.copy()
array_1.insert(max_elem_pos, min_elem)
array_1.pop(max_elem_pos + 1)
array_1.insert(min_elem_pos, max_elem)
array_1.pop(min_elem_pos + 1)
print(f'{min_elem = }, {max_elem = }\n')
print(f'вар 1 =  {array_1}')  # массив с перестановкой


'------------ вариант 2 ------------'

for i in array:
    min_elem = i if min_elem > i else min_elem
    max_elem = i if max_elem < i else max_elem
array_2 = []  # для измененного массива
change_list = []  # чтобы избежать многократных замен
for i in array:
    if i == min_elem and i not in change_list:
        array_2.append(max_elem)
        change_list.append(min_elem)
    elif i == max_elem and i not in change_list:
        array_2.append(min_elem)
        change_list.append(max_elem)
    else:
        array_2.append(i)

print(f'вар 2 =  {array_2}')  # массив с перестановкой

print(f'source =  {array}')  # исходный массив
