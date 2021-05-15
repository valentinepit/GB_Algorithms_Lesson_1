"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


def find_sum(a):
    if a <= 10:
        return a
    return a % 10 + find_sum(a // 10)


if __name__ == '__main__':
    a = 1
    max_sum = 0
    while a != 0:
        a = int(input('Введите натуральное число. Для окончания введите "0" '))
        new_sum = find_sum(a)
        if new_sum > max_sum:
            max_sum = new_sum
    print(f'Максимальная сумма цифр во введенных числах = {max_sum}')