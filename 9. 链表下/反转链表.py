from Link import LinkedList
from Link import Node

# 给定反转链表的数量，反转链表
def reverseKGroup(head, k):
    if head is None or k < 2:
        return head

    next_head = head
    for i in range(k-1):
        next_head = next_head.next
        if next_head is None:
            return head
    ret = next_head

    current = head
    while next_head:
        tail = current
        prev = None
        for i in range(k):
            if next_head:
                next_head = next_head.next

            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        tail.next = next_head or current

    return ret

lst = LinkedList()
lst.add_last(1)
lst.add_last(3)
lst.add_last(5)
lst.add_last(7)
lst.add_last(9)
lst.print_list()
lst.head.next = reverseKGroup(lst.head.next, 2)
lst.print_list()
lst.head.next = reverseKGroup(lst.head.next, 3)
lst.print_list()
lst.head.next = reverseKGroup(lst.head.next, 4)
lst.print_list()
lst.head.next = reverseKGroup(lst.head.next, 5)
lst.print_list()
lst.head.next = reverseKGroup(lst.head.next, 7)
lst.print_list()