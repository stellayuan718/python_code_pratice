import time
import random

import matplotlib.pyplot as plt

def generate_random_array(n):
    return [random.random() for e in range(n)]

random_lists = [generate_random_array(1000 * n) for n in range(1, 21)]

def search(nums):
    import time
    start  = time.time()
    r = 1 in nums
    t = time.time() - start
    return r, len(nums), t


rst = [search(l) for l in random_lists]
print(rst)