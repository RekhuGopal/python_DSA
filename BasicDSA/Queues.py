class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, value):
		self.items.append(value)

	def dequeue(self):
		return self.items.pop(0)

	def peek(self):
		return self.items[0]

# Example usage:
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())  # Output: 10