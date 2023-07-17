
import random


def print_board(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print("| " + ' | '.join(row) + ' |')


def game():
    board = [' ' for i in range(9)]
    counter = 0
    turn = 'X'
    print_board(board)
    print('Welcome, please choose number from 0 to 8   ')
    print('You play with:', turn)
    for i in range(9):
        user_pos = int(input('Your turn(0-8):'))
        if board[user_pos] == ' ':

            board[user_pos] = 'X'
            turn= 'X'
            print_board(board)
            available_moves = [i for i, v in enumerate(board) if v == " "]
            counter+= 1
            if win(counter,board,turn):
                print('X is a winner')
                break
            elif counter == 9:
                print('Draw!')
                break
            print("It's O's turn!")
            opponent = int(random.choice(available_moves))
            board[opponent] = 'O'
            turn= '0'
            available_moves = [i for i, v in enumerate(board) if v == " "]
            counter += 1
            print_board(board)
            if win(counter, board, turn):
             print("O is a winner!")
             break
            elif counter == 9:
             print('Draw!')
             break


def win(counter, board, turn):
    if board[0] == board[1] == board[2] and board[1] != " ":
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        return True
    # строки
    elif board[0] == board[3] == board[6] and board[0] != " ":
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":

        return True
    # столбцы

    elif all([board[i] == turn for i in (0, 4, 8)]) and board[0] != " ":
        return True
    elif all([board[i] == turn for i in (2, 4, 6)]) and board[2] != " ":
        return True
    # диогонали
    else:
        return False


game()
