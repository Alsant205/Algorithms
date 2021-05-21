"""
4. Определить, какое число в массиве встречается чаще всего.
"""

import random

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

counter = {}  # для хранения значений и частоты их появления
new_value = 1  # счетчика появления значений
max_val = 0  # для регистрации максимального количества совпадений
for element in array:
    if element in counter:
        new_value = counter.get(element) + 1
        max_val = new_value if new_value > max_val else max_val
    counter.update({element: new_value})
    new_value = 1
frequent = {key: val for key, val in counter.items()
            if val == max_val}
print('most frequent =', *frequent)
