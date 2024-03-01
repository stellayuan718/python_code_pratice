# 有重复的节点全部删掉
from Link import LinkedList
from Link import Node

def deleteDuplicates2(head):
    dummy = pre = Node(0)
    dummy.next = head
    while head and head.next:
        if head.value == head.next.value:
            while head and head.next and head.value == head.next.value:
                head = head.next
            head = head.next
            pre.next = head

        else:
            pre.next = head
            head = head.next

    return dummy.next

lst = LinkedList()
lst.add_last(1)
lst.add_last(3)
lst.add_last(3)
lst.add_last(3)
lst.add_last(5)
lst.add_last(7)
lst.add_last(7)
lst.add_last(9)
lst.print_list()
lst.head.next = deleteDuplicates2(lst.head.next)
lst.print_list()