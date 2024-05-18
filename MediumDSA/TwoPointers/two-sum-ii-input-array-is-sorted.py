def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

# Test cases
numbers1 = [2, 7, 11, 15]
target1 = 9
print(two_sum(numbers1, target1))  # Output: [1, 2]

numbers2 = [2, 3, 4]
target2 = 6
print(two_sum(numbers2, target2))  # Output: [1, 3]

numbers3 = [-1, 0]
target3 = -1
print(two_sum(numbers3, target3))  # Output: [1, 2]