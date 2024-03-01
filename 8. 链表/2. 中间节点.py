from Link import LinkedList
from Link import Node

def find_middle(lst):
    assert  lst.head is not None and lst.head.next is not None

    head = lst.head
    fast = head
    slow = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow.value

lst = LinkedList()
lst.add_last(1)
print(find_middle(lst))
lst.add_last(2)
lst.add_last(3)
lst.add_last(4)
print(find_middle(lst))