"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и
вывести на экран. Например, если введено число 3486, надо вывести 6843.
"""


def reverse(a):
    if a <= 10:
        return str(a)
    b = reverse(a // 10)
    return str(a % 10) + b


if __name__ == '__main__':
    a = int(input('Введите число: '))
    result = reverse(a)
    while result.startswith('0'):
        result = result.replace('0', '', 1)
    print(f'{result}')
