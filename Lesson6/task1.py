# Задача 1.
# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

import os
os.system('cls')

a1 = int(input("Введите значение первого элемента арифм. прогрессии: ").strip())
d = int(input("Введите значение разности арифм. прогрессии: ").strip())
n = int(input("Введите количество элементов арифм. прогрессии: ").strip())
print(*[a1 + (n - 1) * d for n in range(1, n + 1)])