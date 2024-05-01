class Matrix:
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.data = [[0 for _ in range(cols)] for _ in range(rows)]

	def get(self, row, col):
		return self.data[row][col]

	def set(self, row, col, value):
		self.data[row][col] = value
		
matrix = Matrix(3, 3)
matrix.set(0, 0, 1)
matrix.set(1, 1, 2)
matrix.set(2, 2, 3)
print(matrix.get(0, 0))  # Output: 1
print(matrix.get(1, 1))  # Output: 2
print(matrix.get(2, 2))  # Output: 3