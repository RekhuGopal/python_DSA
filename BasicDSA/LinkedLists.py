class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, value):
		node = Node(value)
		node.next = self.head
		self.head = node

	def get(self, index):
		current = self.head
		while index > 0 and current:
			current = current.next
			index -= 1
		return current.value if current else None

# Example usage:
dll = LinkedList()
dll.insert(10)
dll.insert(20)
print(dll.get(1))  # Output: 10