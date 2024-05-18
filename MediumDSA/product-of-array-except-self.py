def productExceptSelf(nums):
    n = len(nums)
    # Initialize arrays to store prefix and suffix products
    prefix_products = [1] * n
    suffix_products = [1] * n
    
    # Calculate prefix products
    for i in range(1, n):
        prefix_products[i] = prefix_products[i - 1] * nums[i - 1]
    
    # Calculate suffix products
    for i in range(n - 2, -1, -1):
        suffix_products[i] = suffix_products[i + 1] * nums[i + 1]
    
    # Calculate answer array
    answer = [prefix_products[i] * suffix_products[i] for i in range(n)]
    
    return answer

# Test cases
nums1 = [1, 2, 3, 4]
print("Output for nums1:", productExceptSelf(nums1))  # Output: [24, 12, 8, 6]

nums2 = [-1, 1, 0, -3, 3]
print("Output for nums2:", productExceptSelf(nums2))  # Output: [0, 0, 9, 0, 0]
