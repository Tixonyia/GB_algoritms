"""4. Определить, какое число в массиве встречается чаще всего."""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

counted = []
count_items = []
for _ in array:
    count_item = 0
    for i in array:
        if _ == i and _ not in counted:
            count_item += 1
    if _ not in counted:
        count_items.append(count_item)
        counted.append(_)

max_count = 0
total = []

for _ in count_items:
    if _ >= max_count:
        max_count = _

for _ in count_items:
    if _ == max_count:
        total.append(counted[count_items.index(_)])
    count_items[count_items.index(_)] = 0

print(array, f'Числа с максимальным вхождением: ', sep='\n')
print(*total)
