
class MinStack:
    def __init__(self):
        self.stack = []  # Main stack to hold the elements
        self.min_stack = []  # Stack to hold the minimum elements

    def push(self, val: int) -> None:
        self.stack.append(val)  # Push the value onto the main stack
        # Push the value onto the min stack if it's the new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()  # Pop the value from the main stack
            # If the popped value is the minimum, pop it from the min stack as well
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None  # Return the top element of the main stack

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None  # Return the minimum element

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
