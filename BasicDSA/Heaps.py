class Heap:
	def __init__(self):
		self.heap = []

	def insert(self, value):
		self.heap.append(value)
		self._heapify_up(len(self.heap) - 1)
		
	def _heapify_up(self, index):
		while index > 0:
			parent_index = (index - 1) // 2
			if self.heap[parent_index] < self.heap[index]:
				self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
				index = parent_index
			else:
				break

	def get_max(self):
		return self.heap[0]

	def extract_max(self):
		if len(self.heap) > 1:
			max_value = self.heap[0]
			self.heap[0] = self.heap.pop()
			self._heapify_down(0)
			return max_value
		else:
			return None

	def _heapify_down(self, index):
		while True:
			left_child_index = 2 * index + 1
			right_child_index = 2 * index + 2
			largest = index
			if (
				left_child_index < len(self.heap) and
				self.heap[left_child_index] > self.heap[largest]
			):
				largest = left_child_index
			if (
				right_child_index < len(self.heap) and
				self.heap[right_child_index] > self.heap[largest]
			):
				largest = right_child_index
			if largest == index:
				break
			self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
			index = largest
			
heap = Heap()
heap.insert(5)
heap.insert(10)
heap.insert(3)
print(heap.get_max())  # Output: 10
print(heap.extract_max())  # Output: 10
print(heap.get_max())  # Output: 5