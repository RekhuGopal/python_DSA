def length_of_longest_substring(s):
    n = len(s)
    max_len = 0
    char_index = {}  # Dictionary to store the most recent index of each character

    left = 0

    for right in range(n):
        print(s[right] )
        print(char_index)
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
            print(left)
        char_index[s[right]] = right
        max_len = max(max_len, right - left + 1)

    return max_len

# Test cases
print(length_of_longest_substring("abcabcbb"))  # Output: 3
#print(length_of_longest_substring("bbbbb"))     # Output: 1
#print(length_of_longest_substring("pwwkew"))    # Output: 3
