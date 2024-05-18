class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left_lca = lowestCommonAncestor(root.left, p, q)
    right_lca = lowestCommonAncestor(root.right, p, q)
    
    if left_lca and right_lca:
        return root
    elif left_lca:
        return left_lca
    else:
        return right_lca

# Example usage:
# Example 1
root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.right.left = TreeNode(0)
root1.right.right = TreeNode(8)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)
p1 = root1.left
q1 = root1.right
print(lowestCommonAncestor(root1, p1, q1).val)  # Output: 3

# Example 2
root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(2)
root2.right.left = TreeNode(0)
root2.right.right = TreeNode(8)
root2.left.right.left = TreeNode(7)
root2.left.right.right = TreeNode(4)
p2 = root2.left
q2 = root2.left.right.right
print(lowestCommonAncestor(root2, p2, q2).val)  # Output: 5

# Example 3
root3 = TreeNode(1)
root3.right = TreeNode(2)
p3 = root3
q3 = root3.right
print(lowestCommonAncestor(root3, p3, q3).val)  # Output: 1