import time
from random import randint



def generate_random_array(n):
    return [randint(0, n) for e in range(n)]


def shell_sort(nums):
    start = time.time()

    gap = len(nums)
    length = len(nums)

    while (gap > 0):
        for i in range(gap, length):
            for j in range(i, gap - 1, -gap):
                if (nums[j - gap] > nums[j]):
                    nums[j], nums[j - gap] = nums[j - gap], nums[j]

        if (gap == 2):
            gap = 1
        else:
            gap = gap // 2

    t = time.time() - start
    return len(nums), t

random_lists = [generate_random_array(100 * n) for n in range(1, 20)]

rst = [shell_sort(l) for l in random_lists]
rst