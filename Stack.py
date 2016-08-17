class Stack(object):

    """Docstring for Stack. """

    def __init__(self):
        """initializing the stack """
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        self.__items.pop()

    def is_empty(self):
        return self.__items == []

    def size(self):
        return len(self.__items)

    def __iter__(self):
        for i in self.__items:
            yield i
