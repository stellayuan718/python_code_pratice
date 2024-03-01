candidates = [2, 3, 6, 7]

# 列出总和为7的所有组合
t = 7

def comb(candidates, t):
    result = []
    tmp = []
    remains = t
    nums = candidates
    combHelper(result, tmp, nums, remains, 0)
    print(result)

def combHelper(result, tmp, nums, remains, start):
    if remains == 0:
        result.append(tmp[:])

    elif remains < 0:
        return

    else:
        for i in range(start, len(nums)):
            tmp.append(nums[i])
            combHelper(result, tmp, nums, remains-nums[i], i)
            tmp.pop()




comb(candidates, t)
