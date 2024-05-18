class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    
    # Construct a dictionary to store the index of each element in the inorder list
    inorder_map = {}
    for i, val in enumerate(inorder):
        inorder_map[val] = i
    
    def build_tree_helper(in_start, in_end, post_start, post_end):
        if post_start > post_end:
            return None
        
        # The last element in the postorder list is the root of the subtree
        root_val = postorder[post_end]
        root = TreeNode(root_val)
        
        # Find the index of the root element in the inorder list
        root_index = inorder_map[root_val]
        
        # Calculate the number of elements in the right subtree
        right_subtree_size = in_end - root_index
        
        # Recursively construct the right subtree
        root.right = build_tree_helper(root_index + 1, in_end, post_end - right_subtree_size, post_end - 1)
        # Recursively construct the left subtree
        root.left = build_tree_helper(in_start, root_index - 1, post_start, post_end - right_subtree_size - 1)
        
        return root
    
    return build_tree_helper(0, len(inorder) - 1, 0, len(postorder) - 1)

def printTree(root):
    if root:
        print(root.val, end=" ")
        printTree(root.left)
        printTree(root.right)

# Example usage:
# Example 1
inorder1 = [9,3,15,20,7]
postorder1 = [9,15,7,20,3]
result1 = buildTree(inorder1, postorder1)
printTree(result1)  # Output: 3 9 None None 20 15 None None 7 None None

# Example 2
inorder2 = [-1]
postorder2 = [-1]
result2 = buildTree(inorder2, postorder2)
printTree(result2)  # Output: -1 None None