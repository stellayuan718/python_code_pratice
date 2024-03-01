# 有重复数字

def subsets2(nums):
    res = [[]]
    for num in nums:
        res += [i + [num] for i in res if i + [num] not in res]


def subsets_recursive2(nums):
    lst = []
    result = []
    nums.sort()
    subsets2_recursive_helper(result, lst, nums, 0)
    return result

def subsets2_recursive_helper(result, lst, nums, pos):
    result.append(lst[:])
    for i in range(pos, len(nums)):
        if (nums[i] == nums[i-1]):
            continue
        lst.append(nums[i])
        subsets2_recursive_helper(result, lst, nums, i+1)
        lst.pop()

nums = [1,5,2,2,2,4]
print(subsets2(nums))
print(subsets_recursive2(nums))
