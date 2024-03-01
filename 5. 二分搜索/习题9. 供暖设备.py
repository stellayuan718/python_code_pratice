from bisect import bisect  # 二分查找库

def findRadius(houses, heaters):
    heaters.sort()  # 先排序
    ans = 0

    for h in houses:
        hi = bisect(heaters, h)  # 第一个参数是列表，第二个参数是要查找的数，返回值为索引
        #对于每一个房子， 找到左边的供暖设备，右边的供暖设备，然后找到离房子最近的设备，对所有的最小值取最大值
        left = heaters[hi-1] if hi - 1 >= 0 else float('-inf')

        right = heaters[hi] if hi < len(heaters) else float('inf')

        ans = max(ans, min(h - left, right - h))

        return ans


houses = [1,2,3,4]
heaters = [1,4]

a = findRadius(houses, heaters)
print(a)