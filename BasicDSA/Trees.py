class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class Tree:
	def __init__(self):
		self.root = None

	def insert(self, value):
		if not self.root:
			self.root = Node(value)
		else:
			self._insert_recursive(self.root, value)

	def _insert_recursive(self, node, value):
		if value < node.value:
			if node.left:
				self._insert_recursive(node.left, value)
			else:
				node.left = Node(value)
		else:
			if node.right:
				self._insert_recursive(node.right, value)
			else:
				node.right = Node(value)

# Example usage:
tree = Tree()
tree.insert(10)
tree.insert(5)
tree.insert(15)