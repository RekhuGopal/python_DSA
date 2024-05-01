class Array:
	def __init__(self, size):
		self.size = size
		self.array = [None] * size

	def insert(self, index, value):
		if index < self.size:
			self.array[index] = value

	def get(self, index):
		if index < self.size:
			return self.array[index]

# Example usage:
arr = Array(5)
arr.insert(0, 10)
arr.insert(1, 20)
print(arr.get(0))  # Output: 10