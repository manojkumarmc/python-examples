class Node():
    def __init__(self, val):
        self.l = None
        self.r = None
        self.val = val


class BST():
    def __init__(self):
       self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
            return

        current = self.root
        while current:
            if val < current.val:
                if current.l is not None:
                    current = current.l
                else:
                    current.l = Node(val)
                    break
            if val > current.val:
                if current.r is not None:
                    current = current.r
                else:
                    current.r = Node(val)
                    break

    def min_val(self):
        current = self.root
        while current:
            if current.l:
                current = current.l
            else:
                print '%s' % current.val
                break

bst = BST()
bst.add(10)
bst.add(20)
bst.add(8)
bst.add(3)
bst.add(100)
bst.add(-2)
bst.min_val()

