class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head):
    if not head:
        return None
    
    # Create a mapping between original nodes and corresponding new nodes
    mapping = {}
    
    # First pass: create new nodes and map original nodes to new nodes
    original = head
    while original:
        mapping[original] = Node(original.val)
        original = original.next
    
    # Second pass: set next and random pointers for new nodes
    original = head
    while original:
        new_node = mapping[original]
        new_node.next = mapping.get(original.next)
        new_node.random = mapping.get(original.random)
        original = original.next
    
    # Return the head of the new list
    return mapping[head]

# Example usage:
# Create the original linked list
head = Node(7)
head.next = Node(13)
head.next.next = Node(11)
head.next.next.next = Node(10)
head.next.next.next.next = Node(1)

# Set random pointers
head.random = None
head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head

# Create a deep copy of the list
copied_head = copyRandomList(head)

# Print the copied list
while copied_head:
    print([copied_head.val, None if copied_head.random is None else copied_head.random.val])
    copied_head = copied_head.next
# Output: [[7,None],[13,7],[11,1],[10,11],[1,7]]