class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.curr_node = None
        
    def add_node(self, data):
        new_node = Node(data)
        new_node.next = self.curr_node
        self.curr_node = new_node

    def l_print(self):
        node = self.curr_node
        while node:
            print node.data
            node = node.next


ll = LinkedList()
ll.add_node(1)
ll.add_node(23)
ll.add_node(14)
ll.l_print()
