class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy_head = ListNode(0)
    dummy_head.next = head

    # Find the length of the list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    # Calculate the position of the node to be removed from the beginning
    remove_index = length - n

    # Traverse the list again to find the node just before the node to be removed
    prev = dummy_head
    for _ in range(remove_index):
        prev = prev.next

    # Remove the node
    prev.next = prev.next.next

    return dummy_head.next

# Example usage:
# Create the linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Remove the 2nd node from the end
n = 2
result = removeNthFromEnd(head, n)

# Print the modified list
while result:
    print(result.val, end=" ")
    result = result.next
# Output: 1 2 3 5