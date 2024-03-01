class PriorityQueueBase:
    """Abstract base class for a priority queue."""

    class Item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

        def is_empty(self):
            return len(self) == 0

        def __str__(self):
            return str(self._key)


class HeapPriorityQueue(PriorityQueueBase):

    # 最小值堆

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def add(self, key, value):
        self._data.append(self.Item(key, value)) # 添加一个数
        self._upheap(len(self._data) - 1)  # 重新排序

    def min(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty.")
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty.")
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)

    def _parent(self, j):
        return (j - 1) // 2  # 父节点的index

    def _left(self, j):
        return 2 * j + 1     # 左节点的index

    def _right(self, j):
        return 2 * j + 2     # 右节点的index

    def _has_left(self, j):
        return self._left(j) < len(self._data)   # 左节点的index小于数据长度

    def _has_right(self, j):
        return self._right(j) < len(self._data)  # 右节点的index小于数据长度

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]   # 两个数据交换

    def _upheap(self, j):
        parent = self._parent(j)   # 得到父节点的index
        if j > 0 and self._data[j] < self._data[parent]:   #如果数据index大于0，且数据小于父节点
            self._swap(j, parent)  #子节点和父节点交换
            self._upheap(parent)   # 递归调用 传入新的父节点的index

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)


heap = HeapPriorityQueue()
heap.add(4, "D")
heap.add(3, "C")
heap.add(1, "A")
heap.add(5, "E")
heap.add(2, "B")
heap.add(7, "G")
heap.add(6, "F")
heap.add(26, "Z")

for item in heap._data:
    print(item)

print("min is: ")
print(heap.min())
print()

print("remove min: ")
print(heap.remove_min())
print("Now min is: ")
print(heap.min())
print()

print("remove min: ")
print(heap.remove_min())
print("Now min is: ")
print(heap.min())
print()

heap.add(1, "A")
print("Now min is: ")
print(heap.min())
print()