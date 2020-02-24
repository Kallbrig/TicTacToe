def print_board(board):
    # print("Printing Board")
    for row in board:
        for char in row:
            print(char, end=' ')

        print()


def select_play(board):
    if board is None:
        board = [[' ', '|', ' ', '|', ' '],
                 ['-', '+', '-', '+', '-'],
                 [' ', '|', ' ', '|', ' '],
                 ['-', '+', '-', '+', '-'],
                 [' ', '|', ' ', '|', ' ']]
    print_board(board)

    key = input("Where would you like to play 1-9?\n")
    while not key.isnumeric():
        key = input("that's not a valid selection.\nPlease select a number 1-9\n")
    while not (0 < int(key) < 10):
        key = input("that's not a valid selection.\nPlease select a number 1-9\n")

    select_play(play(int(key), board))


# Switch Statement replacement
def play(position, board):
    if position == 1:
        board[0][0] = 'X'
        return board
    elif position == 2:
        board[0][2] = 'X'
        return board
    elif position == 3:
        board[0][4] = 'X'
        return board
    elif position == 4:
        board[2][0] = 'X'
        return board
    elif position == 5:
        board[2][2] = 'X'
        return board
    elif position == 6:
        board[2][4] = 'X'
        return board
    elif position == 7:
        board[4][0] = 'X'
        return board
    elif position == 8:
        board[4][2] = 'X'
        return board
    elif position == 9:
        board[4][4] = 'X'
        return board
    else:
        return "Hello"


select_play(None)
