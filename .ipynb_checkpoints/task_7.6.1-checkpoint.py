def greet():
    print(f'''
    ------------------------
    Играем в крестики-нолики
    ------------------------
       формат ввода: х у
       х - номер строки
       у - номер столбца
            ''')


field = [[' '] * 3 for i in range(3)]


def game():
    print()
    print(f"  | 0 | 1 | 2 |")
    print('---------------')
    for i, row in enumerate(field):
        print(f"{i} | {' | '.join(row)} |")
        print('---------------')
    print()


def your_turn():
    while True:
        coord = input('Ваш ход - ').split()
        if len(coord) != 2:
            print("Введите две координаты:")
            continue
        x, y = coord

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа:")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона!")
            continue

        if field[x][y] != " ":
            print("Клетка занята!")
            continue

        return x, y


def check_win():
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coord in win_coord:
        symbol = []
        for i in coord:
            symbol.append(field[i[0]][i[1]])
            if symbol == ["X", "X", "X"]:
                print("ПОБЕДИЛИ КРЕСТИКИ!!!")
                return True
            if symbol == ["O", "O", "O"]:
                print("ПОБЕДИЛИ НОЛИКИ!!!")
                return True
    return False


greet()
count = 0
while True:
    count += 1
    game()
    if count % 2 == 1:
        print("Поставьте крестик")
    else:
        print("Поставьте нолик")

    x, y = your_turn()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if count == 9:
        print("Ничья")
        break

    if check_win():
        break
