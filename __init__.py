import sys


def print_board(board):
    # print("Printing Board")
    for row in board:
        for char in row:
            print(char, end=' ')

        print()


def switch_turn(turn):
    if turn == 'X':
        return 'O'
    elif turn == 'O':
        return 'X'


# takes the desired position, the current board and the symbol of the current player as arguments
# returns new board
def play(position, board, turn):
    if position == 1:
        board[0][0] = turn
        return board
    elif position == 2:
        board[0][2] = turn
        return board
    elif position == 3:
        board[0][4] = turn
        return board
    elif position == 4:
        board[2][0] = turn
        return board
    elif position == 5:
        board[2][2] = turn
        return board
    elif position == 6:
        board[2][4] = turn
        return board
    elif position == 7:
        board[4][0] = turn
        return board
    elif position == 8:
        board[4][2] = turn
        return board
    elif position == 9:
        board[4][4] = turn
        return board
    else:
        return "You shouldn't be seeing this you stupid bitch"


# takes board and the current symbol as arguments
# returns nothing. recursive.
def select_play(board, turn):
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
    new_board = play(int(key), board, turn)
    new_turn = switch_turn(turn)
    win_checker(new_board)
    # Recursion begins here
    select_play(new_board, new_turn)


# ends game when 9 X's or O's are on the board.
# TO-DO: check if a player has won and notify them.
def win_checker(board):
    count = 0
    for row in board:
        for cha in row:
            if cha == 'X' or cha == 'O':
                count = count + 1
    if count == 9:
        print('Game Over! Congratulations!')
        sys.exit()


def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


select_play(None, 'X')
