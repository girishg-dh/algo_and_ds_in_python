from stack import Stack

class MyQueue(object):

    def __init__(self):
        self.stack = Stack()

    def push(self, x):
        self.stack.push(x)

    def pop(self):
        temp_stack = Stack()
        while not self.stack.is_empty():
            temp_stack.push(self.stack.pop())
        element = temp_stack.pop()

        while not temp_stack.is_empty():
            self.stack.push(temp_stack.pop())
        return element

    def peek(self):
        temp_stack = Stack()
        if self.stack.is_empty():
            return None
        elif self.stack.size() == 1:
            return self.stack.top()
        temp_stack.stack_list = self.stack.stack_list.copy()
        while temp_stack.size() > 1:
            temp_stack.pop()
        return temp_stack.pop()



    def empty(self):
        return self.stack.is_empty()




if __name__=='__main__':
    myQ = MyQueue()
    print(myQ.empty())
    print(myQ.push(1))
    print(myQ.push(2))
    print(myQ.push(3))
    print(myQ.push(10))
    print(myQ.pop())
    print(myQ.pop())
    print(myQ.peek())
    print(myQ.empty())
