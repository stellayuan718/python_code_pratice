input = [6,7,1,2,3,4,5]
print(input)



'''
自己的思路：先比较左边和右边，
再比较中间数的左边和右边 

'''
def search(input):
    if input ==0:
        return -1
    length = len(input)
    mid_index = length // 2
    left = 0
    right = length - 1
    while left < right:
        if input[left] <= input[right]:
            if input[mid_index] < input[mid_index+1]:
                right = mid_index
            else:
                right = mid_index + 1
        elif input[left] > input[right]:
            if input[mid_index-1] > input[mid_index]:
                left = mid_index
            else:
                left = mid_index-1
        if left < right:
            mid_index = (left + right) // 2
            item = mid_index
        elif left == right:
            item = left

    return item

item = search(input)
print(input[item])

'''
答案思路：
假设3 4 5 6 7 1 2
L与M比较，判断左半边数组是否是排好序的数组 ，如果是的话，最小值可能是最左边的数，
再使M与R比较，判断右边是否是排好序的，如果右半边没有排好序，那么拐点可能在后半部分
找到的拐点即断点有可能是需要找的数字
时间复杂度为T(n)=T(/2)+1 即lgn

'''

def search_3(alist):
    if len(alist) == 0:
        return -1
    left, right = 0, len(alist)-1
    while left + 1 < right:   # 于此无关
        #if(alist[left] < alist[right]):
            #return alist[left]
        mid = left + (right - left)//2
        if(alist[mid] >= alist[left]):
            left = mid + 1
        else:
            right = mid
    return alist[left] if alist[left] < alist[right] else alist[right]

print(search_3(input))
