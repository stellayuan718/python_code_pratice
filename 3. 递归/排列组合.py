def perm(result, nums):
    if(len(nums) == 0):
        print(result)

    for i in range(len(nums)):
        perm(result+str(nums[i]), nums[0:i]+nums[i+1:])


# 没有用递归，用的for循环
def permute(nums):
    perms = [[]]

    for n in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(perm)+1):
                new_perms.append(perm[:i] + [n] + perm[i:])
            perms = new_perms
    return perms


# 有重复数字
def permUnique(result, nums):
    nums.sort()
    if(len(nums) == 0):
        print(result)

    for i in range(len(nums)):
        if(i!=0 and nums[i-1] == nums[i]):
            continue;
        permUnique(result+str(nums[i]), nums[0:i]+nums[i+1:])


# 从数组中挑选其中的几个数字
def permutation(result, nums, k):
    if k==0:
        print(result)
    for i in range(len(nums)):
        permutation(result+nums[i], nums[0:i] + nums[i+1:], k-1)

nums = [1,2,3]
perm('', nums)
print(permute(nums))
nums = [3,2,3]
permUnique('', nums)

