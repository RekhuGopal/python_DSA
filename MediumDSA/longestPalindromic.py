def longest_palindromic_substring(s):
    n = len(s)
    if n <= 1:
        return s

    # Create a table to store whether substrings are palindromes
    dp = [[False] * n for _ in range(n)]

    start, max_len = 0, 1  # Initialize variables to track the start index and length of the longest palindrome

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check substrings of length greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1  # Ending index of the substring
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    start = i
                    max_len = length

    return s[start:start + max_len]

# Example usage:
s = "babad"
print(longest_palindromic_substring(s))  # Output: "bab" or "aba"