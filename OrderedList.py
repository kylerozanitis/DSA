""" This file is to practice implementing the basic linear data structure ordered list. """

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head

        while current != None:
            if current.get_data() == item:
                return True
            elif current.get_data() > item:
                return False
            else:
                current = current.get_next()

        return False

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        new_node = Node(item)
        if previous == None:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            new_node.set_next(current)
            previous.set_next(new_node)