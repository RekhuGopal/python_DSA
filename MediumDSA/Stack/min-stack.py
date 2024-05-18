class MinStack:

    def __init__(self):
        # Initialize two stacks
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push the value onto the main stack
        self.main_stack.append(val)
        # Update the min_stack with the minimum value seen so far
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop from the main stack
        val = self.main_stack.pop()
        # If the popped value is the minimum, remove it from min_stack
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        return self.main_stack[-1]

    def getMin(self) -> int:
        # Return the top element of the min_stack, which represents the minimum element in the stack
        return self.min_stack[-1]

# Example usage:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Output: -3
minStack.pop()
print(minStack.top())     # Output: 0
print(minStack.getMin())  # Output: -2
