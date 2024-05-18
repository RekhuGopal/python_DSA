def gameOfLife(board):
    rows, cols = len(board), len(board[0])

    # Function to count live neighbors for a given cell
    def countLiveNeighbors(i, j):
        count = 0
        for x in range(max(0, i - 1), min(i + 2, rows)):
            for y in range(max(0, j - 1), min(j + 2, cols)):
                count += board[x][y] & 1
        count -= board[i][j] & 1
        return count

    # Iterate through each cell to determine the next state
    for i in range(rows):
        for j in range(cols):
            live_neighbors = countLiveNeighbors(i, j)
            if board[i][j] == 1 and (live_neighbors == 2 or live_neighbors == 3):
                board[i][j] |= 2  # Set second bit to 1 to represent the next state as live
            if board[i][j] == 0 and live_neighbors == 3:
                board[i][j] |= 2  # Set second bit to 1 to represent the next state as live

    # Update the board with the next state
    for i in range(rows):
        for j in range(cols):
            board[i][j] >>= 1  # Shift to get the next state

# Example usage:
board1 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
gameOfLife(board1)
print(board1)  # Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

board2 = [[1,1],[1,0]]
gameOfLife(board2)
print(board2)  # Output: [[1,1],[1,1]]
