# # Tic Tac Toe game

# board = [' ' for x in range(10)] # Initialize the board with blank spaces

# # Function to print the board
# def print_board(board):
#     print('   |   |')
#     print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
#     print('   |   |')
#     print('-----------')
#     print('   |   |')
#     print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
#     print('   |   |')
#     print('-----------')
#     print('   |   |')
#     print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
#     print('   |   |')

# # Function to check if a space on the board is empty
# def is_space_free(position):
#     return board[position] == ' '

# # Function to check if the board is full
# def is_board_full(board):
#     return not ' ' in board

# # Function to insert a player's mark (X or O) into a specific position on the board
# def insert_letter(letter, position):
#     board[position] = letter

# # Function to check if a player has won the game
# def is_winner(board, letter):
#     return ((board[1] == letter and board[2] == letter and board[3] == letter) or
#             (board[4] == letter and board[5] == letter and board[6] == letter) or
#             (board[7] == letter and board[8] == letter and board[9] == letter) or
#             (board[1] == letter and board[4] == letter and board[7] == letter) or
#             (board[2] == letter and board[5] == letter and board[8] == letter) or
#             (board[3] == letter and board[6] == letter and board[9] == letter) or
#             (board[1] == letter and board[5] == letter and board[9] == letter) or
#             (board[3] == letter and board[5] == letter and board[7] == letter))

# # Function to get the player's next move
# def get_player_move():
#     while True:
#         move = input('Please enter a position to place your letter (1-9): ')
#         try:
#             move = int(move)
#             if move >= 1 and move <= 9:
#                 if is_space_free(move):
#                     return move
#                 else:
#                     print('That position is already occupied. Please try again.')
#             else:
#                 print('Invalid input. Please enter a number between 1 and 9.')
#         except ValueError:
#             print('Invalid input. Please enter a number between 1 and 9.')

# # Function to get the computer's next move
# def get_computer_move():
#     # Check if there's a winning move for the computer
#     for i in range(1, 10):
#         if is_space_free(i):
#             insert_letter('O', i)
#             if is_winner(board, 'O'):
#                 return i
#             else:
#                 insert_letter(' ', i)

#     # Check if there's a winning move for the player
#     for i in range(1, 10):
#         if is_space_free(i):
#             insert_letter('X', i)
#             if is_winner(board, 'X'):
#                 insert_letter('O', i)
#                 return i




board = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

players = ['X','O']

player_turn = True
empty_board = False
check_win = False

cell = ''
row = 0
column = 0

def check_row(player):
    for i in range(3):
        if((board[i][0]==player and board[i][1]==player and board[i][2]==player)):
            return True
    return False

def check_column(player):
    for i in range(3):
        if((board[0][i]==player and board[1][i]==player and board[2][i]==player)):
            return True
    return False

def check_diagonal(player):
    if((board[0][0]==player and board[1][1]==player and board[2][2]==player)):
        return True
    elif((board[0][2]==player and board[1][1]==player and board[2][0]==player)):
        return True
    else:
        return False


def print_board():
    print("\n    1   2   3\n")
    for i in range(3):
        print(f"{i+1}",end='')
        for j in range(3):
            print(" | "+board[i][j], end='')
        
        if(i!=2):
            print("\n   ---+---+---")
        else:
            print()

    # print("1   " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    # print("   ---+---+---")
    # print("2   " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    # print("   ---+---+---")
    # print("3   " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + "\n")

def player_to_board(player):
    cell = input(f"{player}'s turn please enter the row, column: ")
    row = int(cell[0])
    column = int(cell[2])

    if( 1<=row<=3 and 1<=column<=3):
        pass
    else:
        print("\nInput index out of range please input value between 1,3.\n")
        player_to_board(player)

    if(board[row-1][column-1] == " "):
        board[row-1][column-1] = player
    else:
        print("\nEntered cell is not empty please enter again.\n")
        player_to_board(player)


def board_empty(board):
    for sublist in board:
        if " " in sublist:
            return False
        
    return True


if __name__ =="__main__":
    print_board()
    print()
    while(empty_board == False):
        if(player_turn):
            player_to_board(players[0])
        else:
            player_to_board(players[1])
        
        print_board()
        if(player_turn ==True):
            check_win = (check_row(players[0]) or check_column(players[0]) or check_diagonal(players[0]))
            if(check_win):
                print(f"\n{players[0]} wins.")
                break
        else:
            check_win = (check_row(players[1]) or check_column(players[1]) or check_diagonal(players[1]))
            if(check_win):
                print(f"\n{players[1]} wins.")
                break

        player_turn = not player_turn
        empty_board = board_empty(board)
    else:
        print("\nIt's a tie.\n")

    

    
