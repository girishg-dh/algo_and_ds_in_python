# Implement a stack
class MainStack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return self.stack == []
    def size(self):
        return len(self.stack)
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()
    def top(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack
    