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
    if position == 1 and board[0][0] == ' ':
        board[0][0] = turn
        return board
    elif position == 2 and board[0][2] == ' ':
        board[0][2] = turn
        return board
    elif position == 3 and board[0][4] == ' ':
        board[0][4] = turn
        return board
    elif position == 4 and board[2][0] == ' ':
        board[2][0] = turn
        return board
    elif position == 5 and board[2][2] == ' ':
        board[2][2] = turn
        return board
    elif position == 6 and board[2][4] == ' ':
        board[2][4] = turn
        return board
    elif position == 7 and board[4][0] == ' ':
        board[4][0] = turn
        return board
    elif position == 8 and board[4][2] == ' ':
        board[4][2] = turn
        return board
    elif position == 9 and board[4][4] == ' ':
        board[4][4] = turn
        return board
    else:
        print('That spot is already taken! try another')
        select_play(board, turn)


# takes board and the current symbol as arguments
# returns nothing. recursive.
def select_play(board, turn):
    if board is None:
        print('\n\nThe selections are as follows:')
        print_board([['1', '|', '2', '|', '3'],
                     ['-', '+', '-', '+', '-'],
                     ['4', '|', '5', '|', '6'],
                     ['-', '+', '-', '+', '-'],
                     ['7', '|', '8', '|', '9']])
        print('\n')
        board = [[' ', '|', ' ', '|', ' '],
                 ['-', '+', '-', '+', '-'],
                 [' ', '|', ' ', '|', ' '],
                 ['-', '+', '-', '+', '-'],
                 [' ', '|', ' ', '|', ' ']]
    print_board(board)

    key = input("It's " + turn + "'s move. Where would you like to play 1-9?\n")
    while not key.isnumeric():
        key = input("That is not a valid selection.\nPlease select a number 1-9\n")
    while not (0 < int(key) < 10):
        key = input("That is not a valid selection.\nPlease select a number 1-9\n")
    new_board = play(int(key), board, turn)
    new_turn = switch_turn(turn)
    win_checker(new_board)
    # Recursion begins here
    select_play(new_board, new_turn)


# ends game when 9 X's or O's are on the board.
# TO-DO: check if a player has won and notify them.
def win_checker(board):
    # DIAGONAL WIN CHECKER
    # detects a win on diagonal 1,5,9
    if board[0][0] == 'X' and board[2][2] == 'X' and board[4][4] == 'X':
        print_board(board)
        print("Game over! X wins!")
        sys.exit()
    if board[0][0] == 'O' and board[2][2] == 'O' and board[4][4] == 'O':
        print_board(board)
        print("Game over! O wins!")
        sys.exit()
    # detects a win on diagonal 3,5,7
    if board[0][4] == 'O' and board[2][2] == 'O' and board[4][0] == 'O':
        print_board(board)
        print("Game over! O wins!")
        sys.exit()
    if board[0][4] == 'X' and board[2][2] == 'X' and board[4][0] == 'X':
        print_board(board)
        print("Game over! X wins!")
        sys.exit()

    # HORIZONTAL WIN CHECKER
    # detects a win on vertical 1,4,7
    if board[0][0] == 'X' and board[2][0] == 'X' and board[4][0] == 'X':
        print_board(board)
        print("Game over! X wins!")
        sys.exit()
    if board[0][0] == 'O' and board[2][0] == 'O' and board[4][0] == 'O':
        print_board(board)
        print("Game over! O wins!")
        sys.exit()
    # detects a win on vertical 2,5,8
    if board[0][2] == 'X' and board[2][2] == 'X' and board[4][2] == 'X':
        print_board(board)
        print("Game over! X wins!")
        sys.exit()
    if board[0][2] == 'O' and board[2][2] == 'O' and board[4][2] == 'O':
        print_board(board)
        print("Game over! O wins!")
        sys.exit()
    # detects a win on vertical 2,5,8
    if board[0][4] == 'X' and board[2][4] == 'X' and board[4][4] == 'X':
        print_board(board)
        print("Game over! X wins!")
        sys.exit()
    if board[0][4] == 'O' and board[2][4] == 'O' and board[4][4] == 'O':
        print_board(board)
        print("Game over! O wins!")
        sys.exit()

    # HORIZONTAL AND TOTAL PLAYS WIN CHECKER
    # Number of total spaces played
    count = 0
    for row in board:
        # Number of X's and O's in a row
        row_countX = 0
        row_countO = 0
        for char in row:

            # Steps to perform if character is an X
            # if count reaches 9, game is over.
            # if either row_count reaches 3, game is over
            if char == 'X':
                count = count + 1
                row_countX = row_countX + 1
                if row_countX == 3:
                    print_board(board)
                    print('Game Over! X Wins')
                    sys.exit()

            # Steps to perform if character is an O
            # if count reaches 9, game is over.
            # if either row_count reaches 3, game is over
            if char == 'O':
                count = count + 1
                row_countO = row_countO + 1
                if row_countO == 3:
                    print('Game Over! O Wins')
                    sys.exit()

    # TOTAL MOVE COUNT CHECKER
    # if count reaches 9, game is over.
    if count == 9:
        print_board(board)
        print("Game Over! It's a Draw!\n")

        sys.exit()


select_play(None, 'X')
