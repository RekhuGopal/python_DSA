def rotate(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        print(i)
        for j in range(i, n):
            print(j)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Example usage:
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix1)
print(matrix1)  # Output: [[7,4,1],[8,5,2],[9,6,3]]

matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix2)
print(matrix2)  # Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
