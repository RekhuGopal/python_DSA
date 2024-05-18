def jumpGame(nums):
    n = len(nums)
    i = 0
    while i <= n-1:
        if (nums[i] + i) >= n-1:
            return True
        else:
            i+=1
    return False
nums = [2, 3, 3, 3, 4, 6]
print(jumpGame(nums))