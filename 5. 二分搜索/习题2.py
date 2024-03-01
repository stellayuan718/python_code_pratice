def binarysearch(alist, item):
    if len(alist) == 0:
        return -1

    left, right = 0, len(alist)-1
    while left + 1 < right:
        # 跳出循环体的条件：1. L与R乡邻 2. L与R指向同一元素

        mid = left + (right - left)//2
        if alist[mid] == item:
            right = mid
        elif alist[mid] < item:
            left = mid
        elif alist[mid] > item:
            right = mid

    if alist[left] == item:
        return left
    if alist[right] == item:
        return right


    return 1


