from Link import LinkedList
from Link import Node

def find_beginning(head):
    if head is None:
        return None

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            fast = head
            break

    if fast is None or fast.next is None:
        return None

    while fast != slow:
        fast = fast.next
        slow = slow.next

    return slow

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
node3.next = node1
print(find_beginning(node1).value)
node3.next = node2
print(find_beginning(node1).value)
node3.next = node3
print(find_beginning(node1).value)
node4 = Node(4)
node3.next = node4
node4.next = node2
print(find_beginning(node1).value)