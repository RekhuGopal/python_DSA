class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    if not root:
        return None
    
    def flatten_helper(node):
        if not node:
            return None
        
        # Traverse the left subtree
        left_last = flatten_helper(node.left)
        # Traverse the right subtree
        right_last = flatten_helper(node.right)
        
        # If there is a left subtree, move it to the right
        if node.left:
            left_last.right = node.right
            node.right = node.left
            node.left = None
        
        # Return the last node of the flattened tree
        return right_last if right_last else left_last if left_last else node
    
    flatten_helper(root)

# Example usage:
# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(5)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.right = TreeNode(6)

flatten(root1)

# Print the flattened tree
current = root1
while current:
    print(current.val, end=" ")
    current = current.right
# Output: 1 2 3 4 5 6

# Example 2
root2 = None
flatten(root2)
print(root2)  # Output: None

# Example 3
root3 = TreeNode(0)
flatten(root3)
current = root3
while current:
    print(current.val, end=" ")
    current = current.right
# Output: 0