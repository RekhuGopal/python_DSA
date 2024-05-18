def reverse(x: int) -> int:
    if x == 0:
        return 0
    
    negative = x < 0
    x = abs(x)
    
    reversed_num = int(str(x)[::-1])
    
    if negative:
        reversed_num = -reversed_num
    
    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        return 0
    
    return reversed_num

# Test cases
print(reverse(123))    # Output: 321
print(reverse(-123))   # Output: -321
print(reverse(120))    # Output: 21
