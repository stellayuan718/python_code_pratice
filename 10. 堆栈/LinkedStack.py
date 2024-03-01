from Link import LinkedList
from Link import Node

class LinkedStack(object):
    def __init__(self):
        self._list = LinkedList()

    def __len__(self):
        return self._list.length

    def is_empty(self):
        return self._list.length == 0

    def push(self, e):
        self._list.add_first(e)

    def top(self):
        return self._list.get_first().value

    def pop(self):
        return self._list.remove_first().value

    def printstack(self):
        self._list.print_list()