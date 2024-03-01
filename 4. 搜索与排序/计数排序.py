import time
from random import randint


def generate_random_array(n):
    return [randint(0, n) for e in range(n)]


def count_sort(items):
    start = time.time()
    mmax, mmin = items[0], items[0]
    for i in range(1, len(items)):
        if (items[i] > mmax):
            mmax = items[i]
        elif (items[i] < mmin):
            mmin = items[i]
    print(mmax)
    nums = mmax - mmin + 1
    counts = [0] * nums
    for i in range(len(items)):
        counts[items[i] - mmin] = counts[items[i] - mmin] + 1

    pos = 0
    for i in range(nums):
        for j in range(counts[i]):
            items[pos] = i + mmin
            pos += 1

    t = time.time() - start
    return len(items), t

random_lists = [generate_random_array(100 * n) for n in range(1, 20)]

rst = [count_sort(l) for l in random_lists]
print(rst)

