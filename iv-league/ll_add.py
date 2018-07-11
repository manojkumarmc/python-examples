import random

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, val):
        if self.head is None:
            self.head = Node(val)
            return
        curr = self.head
        while curr:
            if curr.next:
                curr = curr.next
            else:
                curr.next = Node(val)
                self.tail = curr.next
                return

    def list_all_nodes(self):
        curr = self.head
        while curr:
            print('%s' % curr.val)
            if curr.next:
                curr = curr.next
            else:
                return

    def merge_lists(self, list1):
        if list1.head is None:
            print('%s' % 'Invalid list1')
            return
        self.tail.next = list1.head



ll = LinkedList()
ll.add_node(12)
ll.add_node(21)
ll.add_node(1)
ll.list_all_nodes()
print '***********'
l1 = LinkedList()
l1.add_node(99)
l1.add_node(88)
l1.add_node(100)
ll.merge_lists(l1)
ll.list_all_nodes()


