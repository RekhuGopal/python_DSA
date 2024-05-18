class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root):
    def dfs(node, current_sum):
        if not node:
            return 0
        
        current_sum = current_sum * 10 + node.val
        
        # If it's a leaf node, return the formed number
        if not node.left and not node.right:
            return current_sum
        
        # Otherwise, continue DFS traversal
        return dfs(node.left, current_sum) + dfs(node.right, current_sum)
    
    return dfs(root, 0)

# Example usage:
# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
print(sumNumbers(root1))  # Output: 25

# Example 2
root2 = TreeNode(4)
root2.left = TreeNode(9)
root2.right = TreeNode(0)
root2.left.left = TreeNode(5)
root2.left.right = TreeNode(1)
print(sumNumbers(root2))  # Output: 1026