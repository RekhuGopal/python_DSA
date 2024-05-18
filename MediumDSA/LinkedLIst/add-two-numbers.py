class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode()
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        # Get the values of the current nodes
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate the sum of the digits and the carry
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        # Create a new node with the digit
        current.next = ListNode(digit)
        current = current.next

        # Move to the next nodes if they exist
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next

# Example usage:
# Create linked lists for the inputs
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

result = addTwoNumbers(l1, l2)
# Print the result
while result:
    print(result.val, end=" ")
    result = result.next
# Output: 7 0 8