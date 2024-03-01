# 区间搜索
# 搜索一个区间，找到给定目标值的开始和结束位置
# 排好序的，且有重复值 target是某一个数
# 找两次，先找左边index， 再找右边index

input = [4,6,7,7,7,7,8,9]

def search_range(alist, target):
    if len(alist) == 0:
        return

    lbound, rbound = -1, -1

    # search for left bound
    left, right = 0, len(alist)-1
    while(left + 1 < right):

        mid = left + (right - left) // 2
        if alist[mid] == target:
            right = mid

        elif alist[mid] < target:
            left = mid

        else:
            right = mid


    if alist[left] == target:
        lbound = left

    elif alist[right] == target:
        lbound = right

    else:
        return(-1, -1)


    # search for right bound

    left, right = 0, len(alist)-1
    while(left + 1 < right):

        mid = left + (right - left) // 2
        if alist[mid] == target:
            left = mid

        elif alist[mid] < target:
            left = mid

        else:
            right = mid

    if alist[right] == target:
        rbound = right

    elif alist[left] == target:
        rbound = left

    else:
        return(-1,-1)

    return (lbound, rbound)