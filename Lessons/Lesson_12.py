#Tic Tac Toe
#Крестики нолики
#variables
# playr1_symbol = 'X'
# player2_symbol = 'O'
# playr1_choice = 0
# playr2_choice = 0
# board_1 = '1'
# board_2 = '2'
# board_3 = '3'
# board_4 = '4'
# board_5 = '5'
# board_6 = '6'
# board_7 = '7'
# board_8 = '8'
# board_9 = '9'
# turn = 'X'
# #show_board
# board = f'{board_1}|{board_2}|{board_3}\n-----\n{board_4}|{board_5}|{board_6}\n-----\n{board_7}|{board_8}|{board_9}'
# print(board)
# #print(board_1, board_2, board_3,'\n',board_4, board_5, board_6, '\n',board_7, board_8, board_9)
#
# #Game choice
# playr1_choice = str(input(f'Please enter your choice{playr1_choice}: '))
# #Board update
# if playr1_choice == board_1:
#     board_1 = playr1_symbol
#     break
# elif playr1_choice == board_2:
#     board_2 = playr1_symbol
#     break
# elif playr1_choice == board_3:
#     board_3 = playr1_symbol
#     break
# elif playr1_choice == board_4:
#     board_4 = playr1_symbol
#     break
# elif playr1_choice == board_5:
#     board_5 = playr1_symbol
#     break
# elif playr1_choice == board_6:
#     board_6 = playr1_symbol
#     break
# elif playr1_choice == board_7:
#     board_7 = playr1_symbol
#     break
# elif playr1_choice == board_8:
#     board_8 = playr1_symbol
#     break
# elif playr1_choice == board_9:
#     board_9 = playr1_symbol
#     break
#
# #Game choice
# playr2_choice = str(input(f'Please enter your choice{playr2_choice}: '))
# #Board update
# if playr2_choice == board_1:
#     board_1 = playr2_symbol
#     break
# elif playr2_choice == board_2:
#     board_2 = playr2_symbol
#     break
# elif playr2_choice == board_3:
#     board_3 = playr2_symbol
#     break
# elif playr2_choice == board_4:
#     board_4 = playr2_symbol
#     break
# elif playr2_choice == board_5:
#     board_5 = playr2_symbol
#     break
# elif playr2_choice == board_6:
#     board_6 = playr2_symbol
#     break
# elif playr2_choice == board_7:
#     board_7 = playr2_symbol
#     break
# elif playr2_choice == board_8:
#     board_8 = playr2_symbol
#     break
# elif playr2_choice == board_9:
#     board_9 = playr2_symbol
#     break





#Крестики Нолики
#Tic Tac Toe
#Variables
player1_symbol = 'X'
player2_symbol = 'O'
player1_choice = '0'
player2_choice = '0'
board_1 = '1'
board_2 = '2'
board_3 = '3'
board_4 = '4'
board_5 = '5'
board_6 = '6'
board_7 = '7'
board_8 = '8'
board_9 = '9'
turn = 'X'
#Show board (simple)
# print(board_1,board_2,board_3)
# print(board_4,board_5,board_6)
# print(board_7,board_8,board_9)
while count <= 5:
for i in range(5):
    #Show board (pro)
    board = f'{board_1}|{board_2}|{board_3}\n-----\n{board_4}|{board_5}|{board_6}\n-----\n{board_7}|{board_8}|{board_9}'
    print(board)

    while True:
        #Game choice
        player1_choice = str(input(f'Enter your choice {player1_symbol}: '))
        #Board update
        if player1_choice == board_1:
            board_1 = player1_symbol
            break
        elif player1_choice == board_2:
            board_2 = player1_symbol
            break
        elif player1_choice == board_3:
            board_3 = player1_symbol
            break
        elif player1_choice == board_4:
            board_4 = player1_symbol
            break
        elif player1_choice == board_5:
            board_5 = player1_symbol
            break
        elif player1_choice == board_6:
            board_6 = player1_symbol
            break
        elif player1_choice == board_7:
            board_7 = player1_symbol
            break
        elif player1_choice == board_8:
            board_8 = player1_symbol
            break
        elif player1_choice == board_9:
            board_9 = player1_symbol
            break

    #Check winner(simple)
    if board_1 == board_2 == board_3:
        if board_1 == player1_symbol:
            print('Player 1 win!')
            break
        elif board_1 == player2_symbol:
            print('Player 2 win!')
            break
    if board_4 == board_5 == board_6:
        if board_4 == player1_symbol:
            print('Player 1 win!')
            break
        elif board_4 == player2_symbol:
            print('Player 2 win!')
            break
    if board_7 == board_8 == board_9:
        if board_7 == player1_symbol:
            print('Player 1 win!')
            break
        elif board_7 == player2_symbol:
            print('Player 2 win!')
            break
    if board_1 == board_4 == board_7:
        if board_1 == player1_symbol:
            print('Player 1 win!')
            break
        elif board_1 == player2_symbol:
            print('Player 2 win!')
            break
    if board_2 == board_5 == board_8:
        if board_2 == player1_symbol:
            print('Player 1 win!')
            break
        elif board_2 == player2_symbol:
            print('Player 2 win!')
            break
    if board_3 == board_6 == board_9:
        if board_3 == player1_symbol:
            print('Player 1 win!')
            break
        elif board_3 == player2_symbol:
            print('Player 2 win!')
            break
    if board_7 == board_5 == board_3:
        if board_7 == player1_symbol:
            print('Player 1 win!')
            break
        elif board_7 == player2_symbol:
            print('Player 2 win!')
            break
    if board_1 == board_5 == board_9:
        if board_1 == player1_symbol:
            print('Player 1 win!')
            break
        elif board_1 == player2_symbol:
            print('Player 2 win!')
            break
    #Show board (pro)
    board = f'{board_1}|{board_2}|{board_3}\n-----\n{board_4}|{board_5}|{board_6}\n-----\n{board_7}|{board_8}|{board_9}'
    print(board)
    if count == 5:
    while True:
        #Game choice
        player2_choice = str(input(f'Enter your choice {player2_symbol}: '))
        #Board update
        if player2_choice == board_1:
            board_1 = player2_symbol
            break
        elif player2_choice == board_2:
            board_2 = player2_symbol
            break
        elif player2_choice == board_3:
            board_3 = player2_symbol
            break
        elif player2_choice == board_4:
            board_4 = player2_symbol
            break
        elif player2_choice == board_5:
            board_5 = player2_symbol
            break
        elif player2_choice == board_6:
            board_6 = player2_symbol
            break
        elif player2_choice == board_7:
            board_7 = player2_symbol
            break
        elif player2_choice == board_8:
            board_8 = player2_symbol
            break
        elif player2_choice == board_9:
            board_9 = player2_symbol
            break

    #Check winner(simple)
    if board_1 == board_2 == board_3:
        if board_1 == player1_symbol:
            print('Player 1 win!')
            break
        elif board_1 == player2_symbol:
            print('Player 2 win!')
            break
    if board_4 == board_5 == board_6:
        if board_4 == player1_symbol:
            print('Player 1 win!')
            break
        elif board_4 == player2_symbol:
            print('Player 2 win!')
            break
    if board_7 == board_8 == board_9:
        if board_7 == player1_symbol:
            print('Player 1 win!')
            break
        elif board_7 == player2_symbol:
            print('Player 2 win!')
            break
    if board_1 == board_4 == board_7:
        if board_1 == player1_symbol:
            print('Player 1 win!')
            break
        elif board_1 == player2_symbol:
            print('Player 2 win!')
            break
    if board_2 == board_5 == board_8:
        if board_2 == player1_symbol:
            print('Player 1 win!')
            break
        elif board_2 == player2_symbol:
            print('Player 2 win!')
            break
    if board_3 == board_6 == board_9:
        if board_3 == player1_symbol:
            print('Player 1 win!')
            break
        elif board_3 == player2_symbol:
            print('Player 2 win!')
            break
    if board_7 == board_5 == board_3:
        if board_7 == player1_symbol:
            print('Player 1 win!')
            break
        elif board_7 == player2_symbol:
            print('Player 2 win!')
            break
    if board_1 == board_5 == board_9:
        if board_1 == player1_symbol:
            print('Player 1 win!')
            break
        elif board_1 == player2_symbol:
            print('Player 2 win!')
            break
    count = count + 1








def display_board(board):
    for i in range(1, board + 1):
        if i == 1:
            print(i, i + 1, i + 2)

        if i == 4:
            print(i, i + 1, i + 2)

        if i == 7:
            print(i, i + 1, i + 2)

        else:
            continue

    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    # return board


def enter_move(board):
    a = input(firs_name, "please enter your move: (from 1 to 9) ")
    if a == 1:


# The function accepts the board's current status, asks the user about their move,
# checks the input, and updates the board according to the user's decision.


# def make_list_of_free_fields(board):
#     # The function browses the board and builds a list of all the free squares;
#     # the list consists of tuples, while each tuple is a pair of row and column numbers.


# def victory_for(board, sign):
#     # The function analyzes the board's status in order to check if
#     # the player using 'O's or 'X's has won the game


# def draw_move(board):
#     # The function draws the computer's move and updates the board.

board = 9
comp = X
you = 0
display_board(board)
enter_move(board)