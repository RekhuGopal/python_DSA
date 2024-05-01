class Node:
	def __init__(self, value):
		self.value = value
		self.adjacent = []

class Graph:
	def __init__(self):
		self.nodes = []

	def add_node(self, value):
		self.nodes.append(Node(value))

	def add_edge(self, node1, node2):
		node1.adjacent.append(node2)
		node2.adjacent.append(node1)

# Example usage:
graph = Graph()
node1 = graph.add_node(10)
node2 = graph.add_node(20)
graph.add_edge(node1, node2)