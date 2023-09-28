import random


def print_board(board):
    k = 0
    for i in range(3):
        for j in range(3):
            print(board[k], end=" ")
            k += 1
        print()
    print()


def check_win(board, symbol):
    win_lines = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                 (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    for i in win_lines:
        count = 0
        for j in i:
            if board[j - 1] == symbol:
                count += 1
        if count == 3:
            return True
    return False


def move_comp(board, free_cell):
    if len(free_cell) == 0:
        return
    O = random.choice(free_cell)
    free_cell.remove(O)
    board[O - 1] = "O"
    print("Мой ход:", O)
    print_board(board)


def move_me(board, free_cell):
    X = check_input_data(board)
    board[X - 1] = "X"
    free_cell.remove(X)
    print_board(board)


def check_input_data(board):
    while True:
        X = input("Ваш ход: ")
        if not X.isdigit():
            print("Вы ввели не число!")
            continue
        else:
            X = int(X)
        if X < 1 or X > 9:
            print("Неверный номер клетки!")
            continue
        elif board[X - 1] == "X" or board[X - 1] == "O":
            print(f"Клетка {X} уже занята!")
            continue
        return X


if __name__ == "__main__":

    board = [i for i in range(1, 10)]
    free_cell = board.copy()
    print_board(board)
    while True:
        if len(free_cell) == 0:
            print("Ничья!")
            break
        move_me(board, free_cell)
        if check_win(board, "X"):
            print("Вы выиграли!")
            break
        move_comp(board, free_cell)
        if check_win(board, "O"):
            print("Вы проиграли!")
            break

# При разработке выбраны процедурная, структурная и императивная парадигмы:
# процедурная - повторяющиеся блоки кода вынесены в отдельные функции;
# структурная - в теле функций используются присваивания, ветвления и циклы, без goto;
# императивная - в теле функций используется линейный (последовательный) код с использованием
# минимального количества встроенных функций, отсутствуют ф-ии высшего порядка (map, filter  и т.д.).
# Было принято решение отказаться от применения парадигмы ООП ввиду слишком малого количества
# необходимых классов и их объектов (игровое поле, клетка поля, игрок 1, игрок 2 - компьютер).