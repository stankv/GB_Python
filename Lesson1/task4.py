# Задача 4.
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# Решение: отломить за раз можно либо k = n, 2n, 3n, ..., (m-1)*n, m*n
# либо k = m, 2m, 3m, ..., (n-1)*m, n*m

n = int(input("Введите n: "))
m = int(input("Введите m: "))
k = int(input("Введите k: "))
if (n < 1 or m < 1 or k < 1 or k > n * m):
    print("Некорректное значение!")
elif (k == m * n):
    print("Да")
else:
    num1 = n
    num2 = m
    count = 1
    flag = False
    while(num1 <= n * m or num2 <= n * m):
        if num1 <= n * m:
            num1 = n * count
        if num2 <= n * m:
            num2 = m * count
        if (num1 == k or num2 == k):
            flag = True
            break
        count += 1
    if flag:
        print("Да")
    else:
        print("Нет")