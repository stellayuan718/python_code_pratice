# 数据流 在无限流序列中找到元素1
# 使用倍增法 复杂度是lgn
from 习题6 import search_range

def search_first(alist):

    left, right = 0,1

    while alist[right] == 0:
        left == right

        right = 2*right

        if right > len(alist):
            right = len(alist) - 1
            break

    return left + search_range (alist[left:right+1], 1)[0]


alist = [0, 0, 0, 0, 0, 1]
r = search_first(alist)
print(r)