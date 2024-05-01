class HashTable:
	def __init__(self, size):
		self.size = size
		self.table = [None] * size

	def hash_function(self, key):
		return key % self.size

	def insert(self, key, value):
		hashed_key = self.hash_function(key)
		if self.table[hashed_key]:
			self.table[hashed_key].append((key, value))
		else:
			self.table[hashed_key] = [(key, value)]

	def get(self, key):
		hashed_key = self.hash_function(key)
		if self.table[hashed_key]:
			for pair in self.table[hashed_key]:
				if pair[0] == key:
					return pair[1]

# Example usage:
hash_table = HashTable(10)
hash_table.insert(10, 'apple')
hash_table.insert(20, 'banana')
print(hash_table.get(10))  # Output: apple