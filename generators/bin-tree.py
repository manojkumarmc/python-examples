class Node:

    def __init__(self, value):
        self.left = []
        self.value = value
        self.right = []

    def iterate0(self):
        for node in self.left:
            yield node.value
        yield self.value
        for node in self.right:
            yield node.value

	def iterate1(self):
		'''
			This is the recursive mode, still not efficient
		'''
		for node in self.left:
			for value in node.iterate():
				yield value
		yield self.value
		for node in self.right:
			for value in node.iterate():
				yield value

	def iterate(self):
		'''
			This has hit the sweet spot; with the yield from keyword
		'''
		for node in self.left:
			yield from node.iterate()
		yield self.value
		for node in self.right:
			yield from node.iterate()

def main():
    root = Node(0)
    root.left = [Node(i) for i in [1, 2, 3]]
    root.right = [Node(i) for i in [4, 5, 6]]
    for value in root.iterate():
        print(value)

if __name__ == "__main__":
    main()
