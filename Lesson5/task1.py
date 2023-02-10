# Задача 1.
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def degree_of_number(A, B):
    if B == 1:
        return A
    return A * degree_of_number(A, B - 1)


x = int(input("Введите число: "))
y = int(input("Введите степень: "))
print(degree_of_number(x, y))
