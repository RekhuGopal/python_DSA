def min_subarray_len(target, nums):
    n = len(nums)
    min_len = float('inf')
    left = 0
    curr_sum = 0

    for right in range(n):
        curr_sum += nums[right]

        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    return min_len if min_len != float('inf') else 0

# Test cases
print(min_subarray_len(7, [2,3,1,2,4,3]))  # Output: 2
print(min_subarray_len(4, [1,4,4]))         # Output: 1
print(min_subarray_len(11, [1,1,1,1,1,1,1,1]))  # Output: 0
