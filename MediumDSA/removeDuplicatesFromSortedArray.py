def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)

    index = 2  # Index to track the position of the next non-duplicate element

    for i in range(2, len(nums)):
        print(i , index - 2)
        print(nums[i], nums[index - 2])
        if nums[i] != nums[index - 2]:
            nums[index] = nums[i]
            index += 1
        print(index)
    return index
nums = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(nums))