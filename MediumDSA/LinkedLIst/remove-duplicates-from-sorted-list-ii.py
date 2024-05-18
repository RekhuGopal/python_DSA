class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    # Create a dummy node to handle the case where the first node is a duplicate
    dummy_head = ListNode(0)
    dummy_head.next = head
    prev = dummy_head

    while head:
        if head.next and head.val == head.next.val:
            # Skip all consecutive nodes with the same value
            while head.next and head.val == head.next.val:
                head = head.next
            prev.next = head.next  # Remove the duplicate nodes
        else:
            prev = prev.next
        head = head.next

    return dummy_head.next

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
head1.next.next.next = ListNode(3)
head1.next.next.next.next = ListNode(4)
head1.next.next.next.next.next = ListNode(4)
head1.next.next.next.next.next.next = ListNode(5)

# Delete duplicate nodes
result1 = deleteDuplicates(head1)

# Print the modified list
printLinkedList(result1)  # Output: 1 2 5

# Create another linked list
head2 = ListNode(1)
head2.next = ListNode(1)
head2.next.next = ListNode(1)
head2.next.next.next = ListNode(2)
head2.next.next.next.next = ListNode(3)

# Delete duplicate nodes
result2 = deleteDuplicates(head2)

# Print the modified list
printLinkedList(result2)  # Output: 2 3
