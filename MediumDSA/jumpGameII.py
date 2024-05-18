def jump(nums):
    n = len(nums)
    i = 0
    if n == 1 or n == 0:
        return 0
    elif n == 2:
        return 1
    
    while i <= n-1:
        if (nums[i] + i) >= n-1:
            return i+1
        else:
            i+=1

print(jump([]))       # Output: 0
print(jump([1]))      # Output: 0
print(jump([0]))      # Output: 0
print(jump([1, 2]))   # Output: 1
print(jump([3, 2, 1]))# Output: 1
print(jump([2, 8, 8, 8, 4])) # Output: 2
print(jump([2,3,0,1,4]))# Output: 2