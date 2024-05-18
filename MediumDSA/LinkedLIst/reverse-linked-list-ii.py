class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    if left == right:
        return head

    dummy_head = ListNode(0)
    dummy_head.next = head

    # Move to the node just before left
    prev_left = dummy_head
    for _ in range(left - 1):
        prev_left = prev_left.next

    # Reverse the portion from left to right
    current = prev_left.next
    prev = None
    for _ in range(right - left + 1):
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # Connect the reversed portion to the rest of the list
    prev_left.next.next = current
    prev_left.next = prev

    return dummy_head.next

# Example usage:
# Create the linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Reverse the portion from position 2 to position 4
left = 2
right = 4
result = reverseBetween(head, left, right)

# Print the reversed list
while result:
    print(result.val, end=" ")
    result = result.next
# Output: 1 4 3 2 5