"""3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_ = 0
min_ = 0

print(array)  # Для удобства визуальной проверки.

for _ in array:
    if _ > max_:
        max_ = _
    elif _ < min_:
        min_ = _

array[array.index(max_)], array[array.index(min_)] = array[array.index(min_)], array[array.index(max_)]

print(array)  # Для удобства визуальной проверки.
print(min_, max_)  # Для удобства визуальной проверки.
