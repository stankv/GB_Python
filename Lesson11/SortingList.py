# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
# Написать точно такую же процедуру, но в декларативном стиле.

import random

# Сортировка выбором (по убыванию). Императивный стиль.
def ImpSortList(num_list):
    counter = 0
    for i in range(counter, len(num_list)):
        for j in range(counter + 1, len(num_list)):
            if (num_list[j] > num_list[i]):
                temp = num_list[i]
                num_list[i] = num_list[j]
                num_list[j] = temp
        counter += 1
    return num_list


# Сортировка выбором (по убыванию). Декларативный стиль.
def DeclSortList(num_list):
    return sorted(num_list, reverse=True)


if __name__ == "__main__":

    numbers = [random.randint(-10, 10) for i in range(10)]
    print("Исходный массив: ", numbers)
    print("Имп. стиль:      ", ImpSortList(numbers))
    print("Декл. стиль:     ", DeclSortList(numbers))
