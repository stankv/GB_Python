# Задача 3.
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import os
os.system('cls')

N = int(input("N: "))
if N <= 0:
    print("Некорректное значение!")
elif N == 1:
    print(1)
elif N >= 2:
    degree = 0
    while True:
        res = 2 ** degree
        if res <= N:
            print(res, end=' ')
        else:
            break
        degree += 1
print()
