from Link import LinkedList
from Link import Node



def isPalindrome(head):
    rev = None
    slow = fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.value == slow.value:
        slow = slow.next
        rev = rev.next
    return not rev

lst = LinkedList()
lst.add_last(1)
lst.add_last(3)
lst.add_last(5)
lst.add_last(7)
lst.add_last(9)
lst.print_list()
print(isPalindrome(lst.head.next))
lst.print_list()

lst = LinkedList()
lst.add_last(1)
lst.add_last(3)
lst.add_last(5)
lst.add_last(3)
lst.add_last(1)
lst.print_list()
print(isPalindrome(lst.head.next))
lst.print_list()