""" This file is to practice implementing the basic linear data structure stack """

class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        # return True if len(self.items) == 0 else False
        return self.items == []

    def size(self):
        return len(self.items)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)
s.pop()
print(s)
s.peek()
print(s)
print(s.isEmpty())
print(s.size())
