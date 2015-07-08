class Node():
    def __init__(self, data=None):
        self.prev = None
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_node(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

            
    def l_print(self):
        node = self.head
        while node:
            print node.data
            node = node.next

    def remove(self, d):
        cn = self.head
        while cn:
            if cn.data == d:
                if cn.prev is not None:
                    cn.prev.next = cn.next
                    cn.next.prev = cn.prev
                else:
                    self.head = cn
                    cn.next.prev = None
            cn = cn.next
                

ll = LinkedList()
ll.add_node(1)
ll.add_node(23)
ll.add_node(14)
ll.add_node(4)
ll.add_node(90)
ll.l_print()

print 'head'
print ll.head.data

print 'tail'
print ll.tail.data

print "removing data"
print "=============="

ll.remove(23)
ll.l_print()
