'''
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы.
'''
import random
from random import randint


def bubble(data):

    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def main():
    array = [random.randint(0, 99) for i in range(10)]
    print(array)
    print(bubble(array))

if __name__ == '__main__':
    main()
