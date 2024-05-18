def h_index(citations):
    citations.sort(reverse=True)  # Sort the citations in descending order
    h = 0
    for i, citation in enumerate(citations):
        if citation >= i + 1:  # Check if the citation count is greater than or equal to the current index
            h = i + 1  # Update h-index
        else:
            break
    return h

# Test cases
citations1 = [3, 0, 6, 1, 5]
print("Output for citations1:", h_index(citations1))  # Output: 3

citations2 = [1, 3, 1]
print("Output for citations2:", h_index(citations2))  # Output: 1
