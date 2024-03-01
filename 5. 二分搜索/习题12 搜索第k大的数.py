from bisect import bisect
# 有重复数字

def kthSmallest(matrix, k):
    lo, hi = matrix[0][0], matrix[-1][-1]
    while lo < hi:
        mid = lo + (hi-lo)//2
        if sum(bisect(row, mid) for row in matrix) < k:
            lo = mid + 1
        else: # 否则往左走
            hi = mid
    return lo


# 在每一行中找中间这个值并返回索引值，如果没找到，则返回最后一个值
# 将所有的索引相加值为N， N表示比mid值小的数有N个、
# 如果N比K值小，则说明需要往右找，如果N值比K大，则需要往左边找

matrix = [
    [1, 4, 8, 10,15],
    [3, 5, 6, 7, 20],
    [9, 20,22,24,29],
    [11,22,23,29,39]
]

k = 5
a = kthSmallest(matrix, k)
print(a)