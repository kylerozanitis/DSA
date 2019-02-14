""" This file contains the program for checking that a string of parentheses
is balanced using a stack. """

from pythonds.basic.stack import Stack

def balParChecker(symbolString):
    s = Stack()

    for item in symbolString:
        if item == "(":
            s.push(item)
        elif item == ")":
            if s.isEmpty():
                return False
            else:
                s.pop()
        else:
            return "Invalid input. Input must only contain opening and closing parenthses."
        
    return True if s.isEmpty() else False

print(balParChecker('((()))'))
print(balParChecker('((())))'))
print(balParChecker('((())'))
print(balParChecker('(((x)))'))