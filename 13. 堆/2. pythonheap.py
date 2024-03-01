from heapq import heappush, heappop
import heapq
heap = []
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
for item in data:
    heappush(heap, item)

ordered = []
while heap:
    ordered.append(heappop(heap))

print(ordered)
data = [1,5,3,2,8,5]
heapq.heapify(data)