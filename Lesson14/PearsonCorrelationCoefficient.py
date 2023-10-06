# Cкрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами).

from random import randint
from math import sqrt
from statistics import mean


def coefficient_Pearson(array_x, array_y):
    Mx = mean(array_x)
    My = mean(array_y)
    return (sum(list(map(lambda x, y: (x - Mx) * (y - My), array_x, array_y))) /
            (sqrt(sum(list(map(lambda x: (x - Mx)**2, array_x)))) *
             sqrt(sum(list(map(lambda y: (y - My)**2, array_y))))))


# для проверки решения (пошагово, в императивном стиле)
def check_solution(array_x, array_y):
    Mx = mean(array_x)
    My = mean(array_y)
    numerator = 0
    denominator = 0
    denominator1 = 0
    denominator2 = 0
    for i in range(len(array_x)):
        numerator += ((array_x[i] - Mx) * (array_y[i] - My))
        denominator1 += ((array_x[i] - Mx) ** 2)
        denominator2 += ((array_y[i] - My) ** 2)
    denominator = sqrt(denominator1 * denominator2)
    return numerator / denominator


if __name__ == "__main__":
    SIZE = 10     # размер массивов
    RANGE = 10    # диапазон значений массивов
    X = list(map(lambda _: randint(0, RANGE), range(SIZE)))
    Y = list(map(lambda _: randint(0, RANGE), range(SIZE)))
    print(X)
    print(Y)
    print(coefficient_Pearson(X, Y))
    print(check_solution(X, Y))
