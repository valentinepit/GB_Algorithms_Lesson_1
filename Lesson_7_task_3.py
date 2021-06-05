'''
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые
не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима)
'''

import random


def quickselect_median(data):
    if len(data) % 2 == 1:
        return quickselect(data, len(data) / 2, random.choice)
    else:
        return 0.5 * (quickselect(data, len(data) / 2 - 1, random.choice) +
                      quickselect(data, len(data) / 2, random.choice))


def quickselect(data, k, pivot_fn):
    if len(data) == 1:
        assert k == 0
        return data[0]

    pivot = pivot_fn(data)

    lows = [el for el in data if el < pivot]
    highs = [el for el in data if el > pivot]
    pivots = [el for el in data if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


def bubble(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def main():
    m = int(input('Введите значение m для подсчета количества элементов массива по формуле 2m + 1: '))
    array = [random.randint(0, 49) for i in range(2 * m + 1)]
    print(f'Первоначальный массив \n{array}')
    print(f'Медианный элемент\n{quickselect_median(array)}')
    print(f'Отсортированный массив для визуальной проверки резельтата \n{bubble(array)}')


if __name__ == '__main__':
    main()
