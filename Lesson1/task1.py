# Задача 1.
# Сумма цифр трехзначного числа.

number = int(input("Введите трехзначное число: "))
if number >= 1000:
    print("Число цифр больше 3")
elif number <= 99 and number >= 0:
    print("Число цифр меньше 3")
elif number < 0:
    print("Отрицательное число!")
else:
    print(number % 10 + (number // 10) % 10 + number // 100)