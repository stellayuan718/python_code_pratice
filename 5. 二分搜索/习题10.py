# sqrt(10)

def sqrt(x):
    if x == 0:
        return 0
    left, right = 1, x
    while left <= right:
        mid = left + (right - left) // 2
        if (mid == x//mid):  # //地板除
            return mid
        if(mid < x // mid):
            left = mid + 1
        else:
            right = mid - 1

    return right


# 牛顿法
def sqrtNewton(x):
    r = x
    while r*r > x:
        r = (r + x//r)//2
    return r


a = sqrt(46)
print(a)
b = sqrtNewton(125348)
print(b)