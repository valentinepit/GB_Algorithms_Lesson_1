# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
# трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и
вывести на экран. Например, если введено число 3486, надо вывести 6843.
"""

import sys
from collections import deque


def var_size(x):
    res = sys.getsizeof(x)
    print(f'type={type(x)}, size={sys.getsizeof(x)}, value = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                res += var_size(key)
                res += var_size(value)

        elif not isinstance(x, str):
            for item in x:
                res += var_size(item)
    return res


def func_size(vars_dic, func_name):
    memory_sum = 0
    for key, value in vars_dic.items():
        s = var_size(value)
        memory_sum += s
        print(f'{key} = {s}')
    print(f'размер всех переменных в {func_name} = {memory_sum}')


def rev_str(a):
    # для числа 4123654789654123987456321 размер всех переменных в rev_str = 74
    a = a[::-1]
    while a.startswith('0'):
        a = a.replace('0', '', 1)
    func_size(locals(), 'rev_str')
    print(a)


def rev_lst(a):
    # для числа 4123654789654123987456321 размер всех переменных в rev_lst = 1530
    a = list(a)
    for i in range(len(a) // 2):
        a[i], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[i]
    i = 0
    while a[i] == '0':
        i += 1
    a = a[i:]
    func_size(locals(), 'rev_lst')
    print(*a, sep='')


def rev_deque(a):
    # для числа 4123654789654123987456321  размер всех переменных в rev_deque = 1948
    res = deque(a)
    res.reverse()
    while res[0] == '0':
        res.popleft()
    func_size(locals(), 'rev_deque')
    print(*res, sep='')


def main():
    num = input('Введите число: ')
    rev_str(num)
    print('_'*50)
    rev_lst(num)
    print('_' * 50)
    rev_deque(num)


if __name__ == '__main__':
    main()

# Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
'''
На мой неискушенный взгляд, при выборе из 3-х вариантов: list, deque, string, самый оптимальный с точки зрения 
экономии ресурсов - использование строки. 
'''