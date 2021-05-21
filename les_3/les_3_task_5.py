"""
5. В массиве найти максимальный отрицательный элемент. Вывести
на экран его значение и позицию в массиве. Примечание к задаче:
пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

import random

SIZE = 5
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_negative = globals()
check_positive = 0
pos = -1
pos_num = 0
negative = {}
for i in array:
    pos += 1
    if i < 0:
        check_positive += 1
        negative.update({pos: i})
        max_negative = i
if check_positive == 0:
    print('В массиве нет отрицательных чисел')
else:
    for key, val in negative.items():
        if val >= max_negative:
            max_negative = val
            pos_num = key
    print(f'{max_negative = }, {pos_num = }')


