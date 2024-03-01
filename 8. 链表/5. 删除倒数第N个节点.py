from Link import LinkedList
from Link import Node
def remove_nth(lst, n):
    assert n <= lst.length() and n >0

    fast = lst.head
    while n > 0:
        fast = fast.next
        n = n - 1

    slow = lst.head
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    result = slow.next
    slow.next = slow.next.next

    lst.length = lst.length() - 1
    return result


lst = LinkedList()
lst.add_last(1)
lst.add_last(3)
lst.add_last(5)
lst.add_last(7)
lst.add_last(9)
lst.print_list()
print(remove_nth(lst, 3).value)
lst.print_list()