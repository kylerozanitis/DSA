""" This file is to practice implementing the basic linear data structure queue,
which maintains the First-In First-Out ordering property (FIFO)."""

class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

q = Queue()
print(q)
q.enqueue("Printer 1")
q.enqueue("Printer 2")
q.enqueue("Printer 3")
print(q.size())
print(q.dequeue())
print(q.size())
print(q.is_empty())