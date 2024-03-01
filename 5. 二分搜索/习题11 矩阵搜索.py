
def matrix_search(alist, target):
    rindex = len(matrix)-1
    cindex = 0
    while rindex >= 0 or cindex >= 0:
        if matrix[rindex][cindex] > target:
            rindex -= 1
        elif matrix[rindex][cindex] < target:
            cindex += 1
        elif matrix[rindex][cindex] == target:
            return rindex, cindex




matrix = [
    [1, 4, 8, 10,15],
    [3, 5, 6, 7, 20],
    [9, 20,22,24,29],
    [11,22,23,29,39]
]

k = 4
a = matrix_search(matrix, k)
print(a)