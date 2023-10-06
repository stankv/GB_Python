# Бинарный поиск O(logn). Работает с ОТСОРТИРОВАННЫМИ массивами. Рекурсия.
# Возвращает индекс искомого элемента, либо -1 если элемент не найден.

def bin_search(array, value):
    return body_search(array, value, 0, len(array) - 1)


def body_search(array, value, left, right):
    if (left > right):
        return -1
    mid = (left + right) // 2
    if (array[mid] < value):
        return body_search(array, value, mid + 1, right)
    elif (array[mid] > value):
        return body_search(array, value, left, mid - 1)
    else:
        return mid


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(bin_search(arr, 9))
    print(bin_search(arr, 100))

# Ввиду самого алгоритма поиска в решении напрашивается рекурсивный подход, 
# что и было применено. Малое количество кода исключает применение ООП и предполагает 
# применение структурной парадигмы. 
# Т.о. в решении были применены следующие парадигмы:
# процедурная - код "упакован" в 2 функции, основную и "тело поиска";
# функциональная - используется рекурсия, а так же основная функция только вызывает "тело поиска";
# структурная - "тело поиска" содержит присваивания и ветвления, нет goto.
