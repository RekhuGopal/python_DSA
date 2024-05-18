class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    # Construct a dictionary to store the index of each element in the inorder list
    inorder_map = {}
    for i, val in enumerate(inorder):
        inorder_map[val] = i
    
    def build_tree_helper(pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end:
            return None
        
        # The first element in the preorder list is the root of the subtree
        root_val = preorder[pre_start]
        root = TreeNode(root_val)
        
        # Find the index of the root element in the inorder list
        root_index = inorder_map[root_val]
        
        # Calculate the number of elements in the left subtree
        left_subtree_size = root_index - in_start
        
        # Recursively construct the left subtree
        root.left = build_tree_helper(pre_start + 1, pre_start + left_subtree_size, in_start, root_index - 1)
        # Recursively construct the right subtree
        root.right = build_tree_helper(pre_start + left_subtree_size + 1, pre_end, root_index + 1, in_end)
        
        return root
    
    return build_tree_helper(0, len(preorder) - 1, 0, len(inorder) - 1)

def printTree(root):
    if root:
        print(root.val, end=" ")
        printTree(root.left)
        printTree(root.right)

# Example usage:
# Example 1
preorder1 = [3,9,20,15,7]
inorder1 = [9,3,15,20,7]
result1 = buildTree(preorder1, inorder1)
printTree(result1)  # Output: 3 9 None None 20 15 None None 7 None None 

# Example 2
preorder2 = [-1]
inorder2 = [-1]
result2 = buildTree(preorder2, inorder2)
printTree(result2)  # Output: -1 None None