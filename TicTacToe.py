board = [['-'] * 3 for i in range(3)]

current_player = 0
def board_show():
    n = 0
    print('''  0 1 2''')
    for i in board:
        print(n, *i, end='\n')
        n += 1


def turn_checker():
    global current_player
    if current_player:
        print('''Ход игрока 2!''')
    else:
        print('''Ход игрока 1!''')


def check_end():
    for i in board:
        if all(i2 == 'X' for i2 in i):
            import sys
            sys.exit('''Игрок 1 выиграл!''')
        elif all(i2 == 'O' for i2 in i):
            import sys
            sys.exit('''Игрок 2 выиграл!''')
        else:
            pass
    col_check = []
    column = 0
    while column < 3:
        col = []
        for i in board:
            col.append(i[column])
        col_check.append(col)
        column += 1
    for i in col_check:
        if all(i2 == 'X' for i2 in i):
            import sys
            sys.exit('''Игрок 1 выиграл!''')
        elif all(i2 == 'O' for i2 in i):
            import sys
            sys.exit('''Игрок 2 выиграл!''')
        else:
            pass
    diag_check = [[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]
    for i in diag_check:
        if all(i2 == 'X' for i2 in i):
            import sys
            sys.exit('''Игрок 1 выиграл!''')
        elif all(i2 == 'O' for i2 in i):
            import sys
            sys.exit('''Игрок 2 выиграл!''')
        else:
            pass
    checklist = 0
    for i in board:
        for i2 in board:
            if '-' in i2:
                checklist = 1
            else:
                pass
    if checklist:
        pass
    else:
        import sys
        sys.exit('''Ничья!''')


def turn():
    global current_player
    turn_checker()
    i, j = int(input('''Ряд(0-2): ''')), int(input('''Столбец(0-2): '''))
    if i < 0 or i > 2 or j < 0 or j > 2:
        print('''Недопустимое значение! Введите значение от 0 до 2!''')
        turn()
    else:
        if current_player:
            if board[i][j] == '-':
                board[i][j] = 'O'
                current_player = 0
                board_show()
                check_end()
                turn()
            else:
                print('''Ячейка занята!''')
                turn()
        else:
            if board[i][j] == '-':
                board[i][j] = 'X'
                current_player = 1
                board_show()
                check_end()
                turn()
            else:
                print('''Ячейка занята!''')
                turn()

turn()
