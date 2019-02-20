""" This file is to practice implementing the basic linear data structure linked list,
which is a type of unordered list. """

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


class LinkedList:
    def __init__(self):
        # It is important to remember that the LinkedList does not contain any
        # node objects, only a single reference to the first node in the linked structure
        self.head = None

    def is_empty(self):
        return self.head == None

    def add_node(self, value):
        # Don't forget to set next node to the head of the list before setting
        # the head of the list to the new node
        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.get_next()

        return count

    def search(self, node):
        current = self.head

        while current != None:
            if current.get_data() == node:
                return True
            else:
                current = current.get_next()

        return False

    def remove_node(self, node):
        previous = None
        current = self.head

        while current != None:
            if current.get_data() == node:
                if previous == None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                
                return True

            else:
                # This process is referred to as inch-worming
                previous = current
                current = current.get_next()


linked_list = LinkedList()
print(linked_list.is_empty())
linked_list.add_node(13)
linked_list.add_node(15)
linked_list.add_node(17)
print(linked_list.is_empty())
print(linked_list.search(13))
print(linked_list.search(14))
print(linked_list.search(17))
print(linked_list.remove_node(13))
print(linked_list.remove_node(17))
print(linked_list.search(17))