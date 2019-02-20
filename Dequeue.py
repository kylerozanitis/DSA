""" This file is to practice implementing the basic linear data structure dequeue. """

class Dequeue:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def palindrome_checker(string):
    """ Function to check if a word is a palindrome with a dequeue """

    dequeue = Dequeue()

    for letter in string:
        dequeue.add_rear(letter)

    while not dequeue.is_empty():
        if dequeue.size() == 1:
            return True
        else:
            first = dequeue.remove_front()
            last = dequeue.remove_rear()

            if first != last:
                return False

    return True

print(palindrome_checker("a"))
print(palindrome_checker("toot"))
print(palindrome_checker("madam"))
print(palindrome_checker("tote"))
print(palindrome_checker("toet"))
print(palindrome_checker(""))