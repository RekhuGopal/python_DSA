def groupAnagrams(strs):
    # Define a dictionary to store groups of anagrams
    anagrams = {}

    # Iterate through each word in the input list
    for word in strs:
        # Sort the characters of the word to create a unique key
        sorted_word = ''.join(sorted(word))
        
        # If the sorted word is not in the dictionary, add it as a new group
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        
        # Add the original word to its corresponding group
        anagrams[sorted_word].append(word)
    
    # Return the values of the dictionary, which are lists of anagrams
    return list(anagrams.values())

# Example usage:
strs1 = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs1))  # Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

strs2 = [""]
print(groupAnagrams(strs2))  # Output: [[""]]

strs3 = ["a"]
print(groupAnagrams(strs3))  # Output: [["a"]]
