class Stack:
	def __init__(self):
		self.items = []

	def push(self, value):
		self.items.append(value)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  # Output: 20