class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)
    
    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    
    def hasNext(self):
        return len(self.stack) > 0
    
    def next(self):
        if not self.hasNext():
            return None
        
        current = self.stack.pop()
        self._push_left(current.right)
        return current.val

# Example usage:
# Example 1
root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

bSTIterator = BSTIterator(root)
print(bSTIterator.next())    # Output: 3
print(bSTIterator.next())    # Output: 7
print(bSTIterator.hasNext()) # Output: True
print(bSTIterator.next())    # Output: 9
print(bSTIterator.hasNext()) # Output: True
print(bSTIterator.next())    # Output: 15
print(bSTIterator.hasNext()) # Output: True
print(bSTIterator.next())    # Output: 20
print(bSTIterator.hasNext()) # Output: False