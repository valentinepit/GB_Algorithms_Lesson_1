'''
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
'''
import random

SIZE = 20
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


if __name__ == '__main__':
    index = 0
    min_el = MIN_ITEM
    for i in range(len(array)):
        if min_el < array[i] < 0:
            min_el = array[i]
            index = i
    print(f'В массиве {array}\nМаксимальный отрицательный элемент : {min_el}\nИндекс элемента : {index}')