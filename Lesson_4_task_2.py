'''
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте
его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
'''
import timeit
import cProfile


def erast(i):
    n = i *10
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0

    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    i = int(n/10) - 1
    #print(b[i])

def is_prime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

def simple(i):
    prime_list = []
    number = 2
    while len(prime_list) < i:
        if is_prime(number):
            prime_list.append(number)
        number += 1

    return prime_list[i-1]




if __name__ == '__main__':
    '''
    print(timeit.timeit('erast(55)', number=1000, globals=globals()))  # 0.1326013
    print(timeit.timeit('erast(550)', number=1000, globals=globals()))  # 1.3423132999999998
    print(timeit.timeit('erast(5550)', number=1000, globals=globals()))  # 14.8518597
    # Зависимость десятичная (дясетикратная) при увеличении параметра, время улетает в космос

    '''
    cProfile.run('erast(5500)')

# 5594 function calls in 0.017 seconds

# Ordered by: standard name

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#    1    0.000    0.000    0.017    0.017 <string>:1(<module>)
#    1    0.017    0.017    0.017    0.017 Lesson_4_task_2.py:15(erast)
#    1    0.000    0.000    0.017    0.017 {built-in method builtins.exec}
# 5590    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


    #print(timeit.timeit('simple(55)', number=1000, globals=globals()))  # 0.0957054
    #print(timeit.timeit('simple(550)', number=1000, globals=globals()))  # 2.8120105
    #print(timeit.timeit('simple(5550)', number=1000, globals=globals()))  # 90.9903735

    #cProfile.run('simple(5500)')

# C:\Study\Algorithms\Lesson_1\Lesson_1\venv\Scripts\python.exe C:/Study/Algorithms/Lesson_1/Lesson_1/Lesson_4_task_2.py
# 113489 function calls in 0.112 seconds

# Ordered by: standard name

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#   1    0.000    0.000    0.112    0.112 <string>:1(<module>)
# 53992    0.091    0.000    0.091    0.000 Lesson_4_task_2.py:39(is_prime)
#   1    0.017    0.017    0.112    0.112 Lesson_4_task_2.py:45(simple)
#   1    0.000    0.000    0.112    0.112 {built-in method builtins.exec}
# 53993    0.004    0.000    0.004    0.000 {built-in method builtins.len}
# 5500    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#   1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


