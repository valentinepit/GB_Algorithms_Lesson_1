'''
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9
'''


def substr_count(data):
    sub_list = []
    len_str = len(data)
    step = 1
    while step < len_str:
        for i in range(0, len_str):
            if hash(data[i:i+step]) not in sub_list:
                sub_list.append(hash(data[i:i+step]))
                #print(data[i:i+step])
        step += 1
    return len(sub_list)


def main():
    string = input('Введите сторку для анализа: ')
    res = substr_count(string)
    print(f'в строке {string} - {res} подстрок')


if __name__ == '__main__':
    main()
