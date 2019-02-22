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

    def append_node(self, value):
        """ Implemented with an algorithmic complexity of O(n) """
        current = self.head
        previous = None

        while current != None:
            previous = current
            current = current.get_next()

        new_node = Node(value)
        previous.set_next(new_node)
        return True

    def insert_node(self, value, index):
        previous = None
        current = self.head
        position = 0

        while position != index:
            previous = current
            current = current.get_next()
            position += 1

        new_node = Node(value)
        if position == 0:
            new_node.set_next(current)
            self.head = new_node
        elif current == None:
            previous.set_next(new_node)
        else:
            new_node.set_next(current)
            previous.set_next(new_node)

        return True

class ImprovedLinkedList:
    """ Linked List implementation with append function as O(1) """
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def add_node(self, value):
        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node

        if self.tail == None:
            self.tail = new_node

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
        """ Method now includes functionality to update tail of linked list """
        previous = None
        current = self.head

        while current != None:
            if current.get_data() == node:
                if previous == None:
                    self.head = current.get_next()
                elif current.get_next() == None:
                    self.tail = previous
                    previous.set_next(current.get_next())
                else:
                    previous.set_next(current.get_next())
                
                return True

            else:
                # This process is referred to as inch-worming
                previous = current
                current = current.get_next()

    def append_node(self, value):
        """ Implemented with an algorithmic complexity of O(1) """
        current = self.tail
        
        new_node = Node(value)
        current.set_next(new_node)
        self.tail = new_node
        return True


linked_list = LinkedList()
print(linked_list.is_empty())
linked_list.add_node(13)
linked_list.add_node(15)
linked_list.add_node(17)
print(linked_list.is_empty())
print(linked_list.search(13))
print(linked_list.append_node(16))
print(linked_list.insert_node(3, 0))
print(linked_list.insert_node(5, 5))
print(linked_list.insert_node(7, 3))


# new_linked_list = ImprovedLinkedList()
# print(new_linked_list.is_empty())
# new_linked_list.add_node(13)
# new_linked_list.add_node(15)
# new_linked_list.add_node(17)
# print(new_linked_list.is_empty())
# print(new_linked_list.search(13))
# print(new_linked_list.search(14))
# print(new_linked_list.search(17))
# print(new_linked_list.remove_node(13))
# print(new_linked_list.remove_node(17))
# print(new_linked_list.search(17))
# print(new_linked_list.append_node(16))
# print(new_linked_list.search(16))