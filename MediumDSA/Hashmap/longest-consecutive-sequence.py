def longestConsecutive(nums):
    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Only start counting if num - 1 is not in the set (starting point of a sequence)
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # Continue counting consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            # Update max_length if the current sequence is longer
            max_length = max(max_length, current_length)

    return max_length

# Example usage:
nums1 = [9,1,4,7,3,-1,0,5,8,-1,6]
print(longestConsecutive(nums1))  # Output: 4

nums2 = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums2))  # Output: 9
