'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def min_max():
    '''
    Проход по массиву с поиском минимального и максимального элементов и возвращение их индексов
    :return: index_min, index_max
    '''
    index_min = index_max = 0
    min_el = max_el = array[0]
    for i in range(1, len(array)):
        if array[i] > max_el:
            max_el = array[i]
            index_max = i
        if array[i] < min_el:
            min_el = array[i]
            index_min = i
    return index_min, index_max


if __name__ == '__main__':
    print(f'Исходный массив: {array}')
    index_min, index_max = min_max()
    print(f'минимальный элемент: {array[index_min]}\nмаксимальный элемент: {array[index_max]}')
    array[index_max], array[index_min] = array[index_min], array[index_max]
    print(f'Результат замены: {array}')
