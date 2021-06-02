'''
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
'''

from collections import namedtuple


def create_company(number):
    profit = 0
    name = input('Введите название предприятия: ')
    Company = namedtuple('Company', ['name', 'profit'])
    for i in range(1, 5):
        profit_q = int(input(f'Введите прибыль за {i}-й квартал: '))
        profit += profit_q

    return Company (name, profit)


def output(lst, av):
    downshifters = []
    print('Компании на плаву:')
    for e, cmp in enumerate(lst):
        if cmp.profit >= av:
            print(cmp.name)
        else:
            downshifters.append(e)
    print('Не переживут кризис: ')
    for i in downshifters:
        print(lst[i].name)


def main():
    forbes = []
    all_profit = 0
    n = int(input('Введите количество предприятий: '))
    for i in range(n):
        forbes.append(create_company(i))
        all_profit += forbes[i].profit
    av_profit = all_profit / n
    output(forbes, av_profit)


if __name__ == '__main__':
    main()


