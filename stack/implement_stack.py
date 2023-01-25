# Implementation of stack as a list(array)

class Stack:

    # creates an empty stack named "items"
    def __init__(self):
        self.items = []

    # check whether stack is empty or not
    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False

    # push element "item" to the stack
    def push(self, item):
        self.items.append(item)

    # pop element "item" from top of stack
    def pop(self):
        return self.items.pop()

    # peek element at top of stack
    def peek(self):
        top = len(self.items) - 1
        return self.items[top]

    # size of the stack
    def size(self):
        return len(self.items)

# stack initialization
# s = Stack()

# print(s.is_empty())      # True

# s.push(52)
# s.push("1")
# s.push("hello")

# print(s.peek())         # hello
# print(s.size())         # 3

# s.pop()

# print(s.size())         # 2