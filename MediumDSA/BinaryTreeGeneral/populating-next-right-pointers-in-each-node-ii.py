class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    if not root:
        return None
    
    queue = [root]
    
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.pop(0)
            if i < size - 1:
                node.next = queue[0]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return root

def printConnectedTree(root):
    while root:
        current_level = root
        while current_level:
            print(current_level.val, end=" ")
            current_level = current_level.next
        print("#")
        root = root.left

# Example usage:
# Example 1
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.right = Node(7)

connect(root1)
printConnectedTree(root1)
# Output:
# 1 #
# 2 3 #
# 4 5 7 #