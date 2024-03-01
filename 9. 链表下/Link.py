class Node:
    def __init__(self, value = None, next = None, prev = None):
        self.value = value # 存放值
        self.next = next   # 存放标签
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = Node()  # 头部节点 空节点
        self.tail = Node()
        self.size = 0

    #O(1)
    def add_first(self, value):
        node = Node(value, None)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def add_last(self, value):
        new_node = Node(value)
        node = self.head
        while node.next != None:
            node = node.next
        node.next = new_node
        self.size += 1

    def remove_first(self):
        node = self.head.next
        self.head.next = node.next
        self.size -= 1

        pass

    def remove_last(self):
        node = self.head
        while node.next != None:
            pre_node = node
            node = node.next
        pre_node.next = None


    def insert_at(self, value, index):
        if (index < 0 or index > self.size):
            raise ValueError("")
        new_node = Node(value)
        node = self.head
        for i in range(index-1): # 找到第index个位置
            node = node.next

        new_node.next = node.next
        node.next = new_node
        self.size += 1

    def remove_at(self, index):
        if (index < 0 or index > self.size):
            raise ValueError("")
        node = self.head
        for i in range(index - 1):
            node = node.next
        node_next = node.next
        node.next = node_next.next
        self.size -= 1


    # O(n)
    def print_list(self):
        node = self.head
        while node.next != None:
            node = node.next
            print(node.value, end = " ")

        print()

    def length(self):
        return self.size


if 'name' == '__main__':
    L1 = LinkedList()
    L1.add_first(5)
    L1.add_first(8)
    L1.add_last(10)
    print(L1.length())
    L1.print_list()
    L1.insert_at(3,3)
    L1.print_list()
    L1.remove_at(2)
    L1.print_list()