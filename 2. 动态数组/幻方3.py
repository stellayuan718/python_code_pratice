def magic_square(n):
    board = [[None] * n for i in range(n)]
    i = 0
    j = int((n-1)/2)
    board[i][j] = 1

    # 向上倾斜
    for num in range(2, n*n+1):
        temp_i = (i - 1 + n) % n
        temp_j = (j + 1) % n

        if(board[temp_i][temp_j] is not None):
            temp_i = (i + 1) % n
            temp_j = j

        i = temp_i
        j = temp_j
        board[i][j] = num

    return board

def show(board):
    for x in board:
        print(x, sep=" ")
    print()

board = magic_square(9)
show(board)