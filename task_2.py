"""2). Отсортируйте по возрастанию методом слияния одномерный вещественный
 массив, заданный случайными числами на промежутке [0; 50).
 Выведите на экран исходный и отсортированный массивы."""

from random import uniform

array = [float("{0:.3f}".format(uniform(0, 50))) for i in range(10)]
print(array)  # для просмотра исходного списка


def my_sort(list_sort):
    s = len(list_sort)
    n = 1
    while n < s:
        for i in range(s - 1):
            if list_sort[i] > list_sort[i + 1]:
                list_sort[i], list_sort[i + 1] = list_sort[i + 1], list_sort[i]
                if i == s - 2:
                    s -= 1
                    n += 1
        n += 1
    return list_sort


def merge(left, right):
    result = []
    l_ind = 0
    r_ind = 0
    while True:
        if l_ind == len(left):
            for i in right[r_ind:]:
                result.append(i)
            return result
        elif r_ind == len(right):
            for i in left[l_ind:]:
                result.append(i)
            return result

        if left[l_ind] < right[r_ind]:
            result.append(left[l_ind])
            l_ind += 1

        elif right[r_ind] < left[l_ind]:
            result.append(right[r_ind])
            r_ind += 1
        elif right[r_ind] == left[l_ind]:
            result.append(left[l_ind])
            result.append(right[r_ind])
            l_ind += 1
            r_ind += 1


def merge_sort(list_merge):
    if len(list_merge) <= 1:
        return list_merge
    if len(list_merge) > 1:
        med = len(list_merge) // 2
        left = [list_merge[i] for i in range(med)]
        right = [list_merge[i] for i in range(med, len(list_merge))]

        right = my_sort(right)
        left = my_sort(left)

        return merge(left, right)


print(merge_sort(array))
