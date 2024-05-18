class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if not head or k == 0:
        return head

    # Calculate the length of the linked list
    length = 1
    current = head
    while current.next:
        length += 1
        current = current.next

    # Determine the effective rotation count
    k %= length

    # If k is 0, the list remains unchanged
    if k == 0:
        return head

    # Connect the last node to the head to form a circular list
    current.next = head

    # Find the new tail node (kth node from the end)
    new_tail_index = length - k - 1
    new_tail = head
    for _ in range(new_tail_index):
        new_tail = new_tail.next

    # Find the new head node (k+1 th node from the end)
    new_head = new_tail.next

    # Set the next pointer of the new tail node to None to break the circular list
    new_tail.next = None

    return new_head

def printLinkedList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Example usage:
# Create the linked list
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

# Rotate the list by 2 places
k1 = 2
result1 = rotateRight(head1, k1)

# Print the rotated list
printLinkedList(result1)  # Output: 4 5 1 2 3

# Create another linked list
head2 = ListNode(0)
head2.next = ListNode(1)
head2.next.next = ListNode(2)

# Rotate the list by 4 places
k2 = 4
result2 = rotateRight(head2, k2)

# Print the rotated list
printLinkedList(result2)  # Output: 2 0 1
