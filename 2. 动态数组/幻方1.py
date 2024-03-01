def magic_square(n):
    board = [[None] * n for i in range(n)]
    i = 0
    j = int((n-1)/2)
    board[i][j] = 1

    # 向上倾斜
    for num in range(2, n*n+1):
        temp_i = i - 1
        temp_j = j + 1
        # 右上方出了上边界
        if(temp_i < 0) and (temp_j < n):
            temp_i = n-1
        # 右上方出了右边界
        if (temp_i >= 0) and (temp_j >= n):
            temp_j = 0

        if(temp_i < 0) and (temp_j >= n):
            temp_i = i + 1
            temp_j = j
        # 右上方格子被占领
        if(board[temp_i][temp_j] is not None):
            temp_i = i + 1
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