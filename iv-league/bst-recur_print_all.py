import random

class Node():
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class Tree():
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        curr = self.root
        while curr:
            if val < curr.v:
                if curr.l is None:
                    curr.l = Node(val)
                    return
                else:
                    curr = curr.l
            elif val > curr.v:
                if curr.r is None:
                    curr.r = Node(val)
                    return
                else:
                    curr = curr.r

    def print_all(self, node=None):
        if node.l:
            print('%s' % node.v)
            self.print_all(node.l)
        if node.r:
            print('%s' % node.v)
            self.print_all(node.r)
        if not node.l and not node.r:
            print('%s ' % node.v)

    def min_val(self):
        current = self.root
        while current:
            if current.l:
                current = current.l
            else:
                print '%s' % current.v
                break

t_o = Tree()
for x in xrange(1,10):
    a_num = random.randint(-1000,1000)
    print(a_num)
    t_o.add(a_num)

print('*' * 72)
t_o.min_val()
print('#' * 72)
t_o.print_all(t_o.root)



