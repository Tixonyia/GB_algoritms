"""5. В массиве найти максимальный отрицательный элемент.
 Вывести на экран его значение и позицию в массиве.
  Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
 Это два абсолютно разных значения."""

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

array_negative = []
for _ in array:
    if _ < 0:
        array_negative.append(_)

max_min_num = MIN_ITEM

index_list = []
print(array)

for _ in array_negative:
    if _ > max_min_num:
        max_min_num = _

index = 0
for _ in array:
    if _ == max_min_num:
        index_list.append(index)
    index += 1

print(f'Максимальное отрицательное число: {max_min_num}')
print(f'Его индексы вхождений: ', *index_list)




