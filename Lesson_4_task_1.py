"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и
вывести на экран. Например, если введено число 3486, надо вывести 6843.
"""
import timeit
import cProfile

def reverse_first(a):
    if a <= 10:
        return str(a)
    b = reverse_first(a // 10)
    need_more_actions = a ** 100
    return str(a % 10) + b


def reverse_second(a):
    result = ''
    while a > 10:
        result += str(a % 10)
        a = a // 10
        need_more_actions = a ** 100
    return int(result + str(a))


def reverse_third(a):
    result = str(a)[::-1]
    return int(result)


def main(n):
    return {'first': reverse_first(n), 'second': reverse_second(n), 'third': reverse_third(n)}


if __name__ == '__main__':
    interesting_thing = main(58668558668598765432198798798798798798723434234324234)
    '''
    print(timeit.timeit('reverse_first(586)', number=1000, globals=globals()))      # 0.0008377999999999997
    print(timeit.timeit('reverse_first(5867)', number=1000, globals=globals()))     # 0.0010267000000000054
    print(timeit.timeit('reverse_first(58679)', number=1000, globals=globals()))    # 0.0013488999999999932
    print(timeit.timeit('reverse_first(586792)', number=1000, globals=globals()))   # 0.00153200000000000566
    print(timeit.timeit('reverse_first(5867921)', number=1000, globals=globals()))  # 0.0017749000000000098
    # Линейная зависимость
    
    print(timeit.timeit('reverse_second(586)', number=1000, globals=globals()))      # 0.0007725000000000024
    print(timeit.timeit('reverse_second(5867)', number=1000, globals=globals()))     # 0.0009543000000000051
    print(timeit.timeit('reverse_second(58679)', number=1000, globals=globals()))    # 0.0011687000000000017
    print(timeit.timeit('reverse_second(586792)', number=1000, globals=globals()))   # 0.0014040999999999984
    print(timeit.timeit('reverse_second(5867921)', number=1000, globals=globals()))  # 0.0016642999999999936
    # Линейная зависимость

    print(timeit.timeit('reverse_third(586)', number=1000, globals=globals()))      # 0.0003445000000000045
    print(timeit.timeit('reverse_third(5867)', number=1000, globals=globals()))     # 0.00034690000000000415
    print(timeit.timeit('reverse_third(58679)', number=1000, globals=globals()))    # 0.00035099999999999715
    print(timeit.timeit('reverse_third(586792)', number=1000, globals=globals()))   # 0.0003677000000000055
    print(timeit.timeit('reverse_third(5867921)', number=1000, globals=globals()))  # 0.000375300000000002
    print(timeit.timeit('reverse_third(5867921654789)', number=1000, globals=globals()))  # 0.00040020000000000333
    # Линейная зависимость (Ну очень плавное увеличение времени) Явно лучший вариант из трех
    '''
    cProfile.run('main(58668558668598765432198798798798798798723434234324234655554564646545465456465465465465)')

   #ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #    1    0.000    0.000    0.010    0.010 <string>:1(<module>)
    #    1    0.005    0.005    0.005    0.005 Lesson_4_task_1.py:16(reverse_second)
    #    1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:25(reverse_third)
    #    1    0.000    0.000    0.010    0.010 Lesson_4_task_1.py:30(main)
    # 86/1    0.005    0.000    0.005    0.005 Lesson_4_task_1.py:8(reverse_first)
    #    1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
    #    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}