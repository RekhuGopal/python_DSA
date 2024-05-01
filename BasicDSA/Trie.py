class TrieNode:
	def __init__(self):
		self.children = {}
		self.end_of_word = False

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		node = self.root
		for char in word:
			if char not in node.children:
				node.children[char] = TrieNode()
			node = node.children[char]
		node.end_of_word = True

	def search(self, word):
		node = self.root
		for char in word:
			if char not in node.children:
				return False
			node = node.children[char]
		return node.end_of_word

trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("apple"))  # Output: True
print(trie.search("app"))  # Output: True
print(trie.search("banana"))  # Output: False