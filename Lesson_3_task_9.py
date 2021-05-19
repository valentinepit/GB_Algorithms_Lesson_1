"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random

SIZE_M = 15
SIZE_N = 5
MIN_ITEM = -100
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)] for _ in range(SIZE_N)]


def matrix_out(matrix):
    """
    :param matrix: матрица 4х5
    Выводит отформатированную матрицу
    """
    for n in matrix:
        for m in n:
            print(f'{m:>7}', end='')
        print()


def find_row_min(row_index):
    '''
    :param row_index: Номер рассматриваемого столбца
    :return: Минимальное значение в стодбце
    Ищем и возвращаем минимальное значение заданного столбца исходной матрицы
    '''
    min_el = matrix[0][row_index]
    for i in range(1, len(matrix)):
        if matrix[i][row_index] < min_el:
            min_el = matrix[i][row_index]
    return min_el


if __name__ == '__main__':
    matrix_out(matrix)
    max_el = find_row_min(0)
    for i in range(1, len(matrix[0])):
        min_el = find_row_min(i)
        if min_el > max_el:
            max_el = min_el
    print(f'AND THE WINNER IIIIIIIIIIIIIS!!!! {max_el}')
