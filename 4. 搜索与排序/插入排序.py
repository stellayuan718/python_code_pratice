import time
from random import randint

def generate_random_array(n):
    return [randint(0, n) for e in range(n)]

def insert_sort(items):
    start = time.time()
    for sort_inx in range(1,len(items)):
        unsort_inx = sort_inx
        while unsort_inx > 0 and items[unsort_inx-1] > items[unsort_inx]:
            items[unsort_inx-1], items[unsort_inx] = items[unsort_inx], items[unsort_inx-1]
            unsort_inx = unsort_inx-1
    t = time.time() - start
    return len(items), t

l = [1, 3, 5, 7, 9, 2, 4, 6, 8, 99]
insert_sort(l)
print(l)



