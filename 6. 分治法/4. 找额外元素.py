# 在两个已经排好序的数组中间找重复值
#
def find_extra_fast(arr1, arr2):
    index = len(arr2)

    left, right = 0, len(arr2) - 1
    while (left <= right):
        mid = (left + right) //2
        if (arr2[mid] == arr1[mid]):
            left = mid + 1
        else:
            index = mid
            right = mid - 1
    return index


ar1 = [3, 5, 7, 9, 11, 13]
ar2 = [3, 5, 7, 11, 13]
a = find_extra_fast(ar1, ar2)
print(ar1[a])
