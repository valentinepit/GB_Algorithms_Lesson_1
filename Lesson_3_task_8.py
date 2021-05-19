"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных
элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""

SIZE_M = 3
SIZE_N = 5


# MIN_ITEM = 0
# MAX_ITEM = 100
# matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)] for _ in range(SIZE_N)]

def matrix_in():
    """
    :return: matrix
    Создание матрицы 3х5 со значением None в каждом элементе.
    Получение значений для элементов матрицу от пользователя
    """
    matrix = [[None for _ in range(SIZE_M)] for _ in range(SIZE_N)]
    for n in range(SIZE_N):
        for m in range(SIZE_M):
            matrix[n][m] = int(input(f'Введите {m + 1}-й элемент {n + 1}-й строки: '))
    return matrix


def row_sum(row):
    """
    :param row: строка матрицы
    :return: сумма элемнтов строки
    Посчитывает и возвращает сумму элементов строки
    """
    r_sum = 0
    for item in row:
        r_sum += item
    return r_sum


def matrix_out():
    """
    Выводит отформатированную матрицу
    """
    for n in matrix:
        for m in n:
            print(f'{m:>7}', end='')
        print()


if __name__ == '__main__':
    matrix = matrix_in()
    for i, row in enumerate(matrix):
        matrix[i].append(row_sum(row))
    matrix_out()
