def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]

    for interval in intervals[1:]:
        # If the current interval overlaps with the previous one, merge them
        if interval[0] <= merged_intervals[-1][1]:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        else:
            merged_intervals.append(interval)

    return merged_intervals

# Example usage:
intervals1 = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals1))  # Output: [[1,6],[8,10],[15,18]]

intervals2 = [[1,4],[4,5]]
print(merge_intervals(intervals2))  # Output: [[1,5]]
