class MapBase():

    class Item:
        __slots__ = 'key', 'value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key

        def __print__(self):
            print(str(self._key) + ":" + str(self._value), end = ",")