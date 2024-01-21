class MyQueue:

    def __init__(self):
        self.primary_stack = []
        self.secondary_stack = []

    def push(self, x: int) -> None:
        self.primary_stack.append(x)

    def pop(self) -> int:
        while len(self.primary_stack) != 0:
            self.secondary_stack.append(self.primary_stack.pop())

        item = self.secondary_stack.pop()

        while len(self.secondary_stack) != 0:
            self.primary_stack.append(self.secondary_stack.pop())

        return item

    def peek(self) -> int:
        while len(self.primary_stack) != 0:
            self.secondary_stack.append(self.primary_stack.pop())

        item = self.secondary_stack[-1]

        while len(self.secondary_stack) != 0:
            self.primary_stack.append(self.secondary_stack.pop())
        
        return item

    def empty(self) -> bool:
        return True if len(self.primary_stack) == 0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()