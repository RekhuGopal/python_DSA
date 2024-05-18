def spiralOrder(matrix):
    if not matrix:
        return []

    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # Traverse bottom row
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            # Traverse left column
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

# Example usage:
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix1))  # Output: [1,2,3,6,9,8,7,4,5]

matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix2))  # Output: [1,2,3,4,8,12,11,10,9,5,6,7]
