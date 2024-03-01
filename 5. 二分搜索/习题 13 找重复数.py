
def findDuplicate(nums):
    low = 1
    high = len(nums)-1
    while low < high:
        mid = low + (high - low)//2
        count = 0
        for i in nums:  # 统计所有数字中比中间数小的数字
            if i <= mid:
                count += 1

        if count <= mid:
            low = mid + 1
        else:
            high = mid
    return low

nums = [3,5,6,3,1,4,2]
a = findDuplicate(nums)
print(a)

# 第一轮：中间数字为3，小于中间数的数字为4， 则重复数字在左边，右边数等于中间数 即3
# 第二轮：中间数字是2，比2小的数字为2，则重复数字在右边，则左边数等于中间数+1 即3
# 第三轮