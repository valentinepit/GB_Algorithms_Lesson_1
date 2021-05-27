'''
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа. Например, пользователь
ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''

from collections import deque

HEX_LST = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']


def input_hex():
    a = deque(input('Введите первое число: '))
    b = deque(input('Введите второе число: '))
    if len(b) > len(a):
        a, b = b, a
    a.reverse()
    b.reverse()
    return a, b


def hex_sum(a, b):
    result = deque()
    k = 0
    for i in range(len(a)):
        one = HEX_LST.index(a[i])
        two = HEX_LST.index(b[i]) if i < len(b) else 0
        result.append(HEX_LST[(one + two + k) % 16])
        k = 1 if one + two > 15 else 0
    result.reverse()
    return result


def hex_out(res):
    print('Сумма = ', end='')
    for i in res:
        print(i, end='')


def main():
    a, b = input_hex()
    result = hex_sum(a, b)
    hex_out(result)


if __name__ == '__main__':
    main()
