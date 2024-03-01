def search_peak(alist):
    return peak_helper(alist, 0, len(alist) - 1)

def peak_helper(alist, start, end):
    if start == end:  # 首先判断两个index是否为同一个
        return start

    if (start + 1 == end):  # 其次判断两个index是否相邻
        if alist[start] > alist[end]:
            return start

        return end

    mid = (start + end) // 2   # 否则取中间值
    if alist[mid] > alist[mid - 1] and alist[mid] > alist[mid + 1]:
        return mid  # 找到峰值
    if alist[mid - 1] > alist[mid] and alist[mid] > alist[mid + 1]:
        return peak_helper(alist, start, mid - 1)
    return  peak_helper(alist, mid + 1, end)


data = [1,3,5,4,6,3,9,5]
a = search_peak(data)
print(a)
