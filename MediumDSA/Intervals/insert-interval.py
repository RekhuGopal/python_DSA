def insert_interval(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    # Add all intervals that end before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge intervals that overlap with newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    result.append(newInterval)

    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result

# Example usage:
intervals1 = [[1,3],[6,9]]
newInterval1 = [2,5]
print(insert_interval(intervals1, newInterval1))  # Output: [[1,5],[6,9]]

intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval2 = [4,8]
print(insert_interval(intervals2, newInterval2))  # Output: [[1,2],[3,10],[12,16]]
