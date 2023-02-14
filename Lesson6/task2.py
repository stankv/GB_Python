# Задача 2.
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
import os
os.system('cls')

array = [randint(-10, 11) for _ in range(21)]
print(array)
min = int(input("Нижняя граница диапазона: ").strip())
max = int(input("Верхняя граница диапазона: ").strip())
print([i for i in range(21) if array[i] >= min and array[i] <= max])
