# Задача 2.
# Петя и Катя – брат и сестра. Петя – студент, а Катя –школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя
#  делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
#  задуманные Петей числа.

# Решение: из системы уравнений X+Y=S, X*Y=P => Y=S-X, X^2 + (-S)*X + P = 0. Если D = (-S)^2 - 4*1*P < 0 то
# решений нет. Если D=0, то одно решение. Если D>0, то 2 решения. Решения будем искать перебором значений (по условию задачи
# есть ограничение диапазона значений: 0≤X,Y≤1000), c учетом значения дискриминанта. Также учтем следующее: 1). Если P=0, то X=0 и Y=S
# 2). Если S=0, то X=Y=0. И поскольку X,Y натуральные, то S>=0 и P>=0
# 3). С учетом частных случаев п.2 и 3, далее рассматриваем диапазон 1≤X,Y≤1000.

import os
os.system('cls')

flag = True
while flag:
    S = int(input("Введите значение суммы чисел: "))
    P = int(input("Введите значение произведения чисел:"))
    if S < 0 or P < 0:
        print("Некорректное значение!")
        continue
    flag = False

if S == 0:    # то и P=0
    print("X = 0, Y = 0")
elif P == 0 and S != 0:
    print(f"X = 0, Y = {S}")
elif P != 0 and S != 0:
    count = 0    # число найденных решений (1 или 2 в зависимости от дискриминанта)
    D = S * S - 4 * P
    if D >= 0:
        for X in range(1, 1001):
            for Y in range(X, 1001):
                if (X * Y == P and X + Y == S):
                    print(f"X = {X}, Y = {Y}")
                    count += 1
                    break
            if (count == 1 and D == 0) or (count == 2 and D > 0):
                break
        if count == 0:
            print("Решений в диапазоне 0-1000 нет.")
    else:
        print("Решений нет!")