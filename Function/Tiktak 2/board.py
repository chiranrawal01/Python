#
board = {
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' '],
}
board_size = 3
def print_board():
    print("\n 1  2  3\n")
    for i in range(board_size):
        print(f"{i+1}", end='')
        for j in range(board_size):
            print("|"+board[i][j],end='')
    if(i!=2):
        print("\n    ........+........")
    else :
        print()
print(board_size)

