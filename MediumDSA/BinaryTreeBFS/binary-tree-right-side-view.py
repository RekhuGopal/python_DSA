class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.pop(0)
            if i == size - 1:  # Only consider the rightmost node at each level
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

# Example usage:
# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(5)
root1.right.right = TreeNode(4)
print(rightSideView(root1))  # Output: [1, 3, 4]

# Example 2
root2 = TreeNode(1)
root2.right = TreeNode(3)
print(rightSideView(root2))  # Output: [1, 3]

# Example 3
print(rightSideView(None))  # Output: []