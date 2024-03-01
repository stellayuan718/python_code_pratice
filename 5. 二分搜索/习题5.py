
input = [1,5,6,7,9]
def search_insert_position(alist, target):
    if len(alist) == 0:
        return 0

    left, right = 0, len(alist)-1
    while left + 1 < right:
        mid = left + (right - left) //2
        if alist[mid] == target:
            return mid

        if (alist[mid] < target):
            left = mid
        else:
            right = mid


    if alist[left] >= target:
        return left
    if alist[right] >=target:
        return right

    return right+1

a = search_insert_position(input,15)
print(a)