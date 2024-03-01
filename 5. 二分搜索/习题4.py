# 在旋转数组中找到相应地数字

input = [5,6,7,8,1,2,3,4]


def search(alist = input, target = 3):
    if len(alist) == 0:
        return -1
    left, right = 0, len(alist)-1
    while left + 1 < right:
        mid = (left + right)//2
        if alist[mid] == target:
            return mid
        if (alist[left] < alist[mid]):   # 如果左边的数小于右边的数，左边排好序，左边的数小于目标值，且目标值小于中间值则目标值在左边
            if alist[left] <= target and target <= alist[mid]:
                right = mid
            else:    # 否则其他情况，目标值都在右边
                left = mid

        else:    # 左边值比中间值大，则右边是排好序的
            # 如果左边比目标值小，且目标值比右边值小，则数在右边
            if alist[left] <= target and target <= alist[right]:
                left = mid
            else:
                right = mid


    if alist[left] == target:
        return left

    if alist[right] == target:
        return right

    return -1


a = search(input,8)
print(a)