from advanced_data_structure.min_stack.stack import MainStack

class MinStack:
    def __init__(self):
        self.main_stack = MainStack()
        self.min_stack = MainStack()

    def push(self, value):
        self.main_stack.push(value)
        if self.min_stack.is_empty() or value <= self.min_stack.top():
            self.min_stack.push(value)
        else:
            self.min_stack.push(self.min_stack.top())

    def pop(self):
        self.min_stack.pop()
        return self.main_stack.pop()

    def min_number(self):
        return self.min_stack.top()