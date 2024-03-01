from Link import LinkedList
from Link import Node

def has_cycle(lst):
    return has_cycle_helper(lst.head)

def has_cycle_helper(head):

    if head is None:
        return False

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            return True

    return False

node1 = Node(1)
print(has_cycle_helper(node1))
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
print(has_cycle_helper(node1))
node3.next = node1
print(has_cycle_helper(node1))
