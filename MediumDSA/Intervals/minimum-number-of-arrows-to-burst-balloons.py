def find_min_arrows(points):
    if not points:
        return 0

    # Sort balloons by their end points
    points.sort(key=lambda x: x[1])

    arrows = 1
    end = points[0][1]

    for start, point_end in points:
        # If the current balloon starts after the end of the last arrow, increment arrows count
        if start > end:
            arrows += 1
            end = point_end  # Update end point
    return arrows

# Example usage:
points1 = [[10,16],[2,8],[1,6],[7,12]]
print(find_min_arrows(points1))  # Output: 2

points2 = [[1,2],[3,4],[5,6],[7,8]]
print(find_min_arrows(points2))  # Output: 4

points3 = [[1,2],[2,3],[3,4],[4,5]]
print(find_min_arrows(points3))  # Output: 2
