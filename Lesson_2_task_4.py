"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
"""


def func(n):
    if n == 0:
        return 0.5 ** n
    return 0.5 ** n + func(n - 1)


if __name__ == '__main__':
    n = int(input('Введите целое число n: '))
    print(f'Сумма рядя элементов рана {func(n - 1)}')
