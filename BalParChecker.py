""" This file contains the program for checking that a string of parentheses
is balanced using a stack. """

from pythonds.basic.stack import Stack

def bal_par_checker(symbol_string):
    s = Stack()

    for item in symbol_string:
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


def bal_symbol_checker(symbol_string):
    s = Stack()

    openers = "({["
    closers = ")}]"

    for item in symbol_string:
        if item in openers:
            s.push(item)
        elif item in closers:
            if s.isEmpty():
                return False
            else:
                top = s.pop()
                if not matcher(top, item):
                    return False
        else:
            return "Invalid input. Input must only contain opening and closing parenthses."
    
    return True if s.isEmpty() else False


def matcher(opener, closer):
    openers = "({["
    closers = ")}]"

    return openers.index(opener) == closers.index(closer)


print(bal_par_checker('((()))'))
print(bal_par_checker('((())))'))
print(bal_par_checker('((())'))
print(bal_par_checker('(((x)))'))

print(bal_symbol_checker('({[]})'))
print(bal_symbol_checker('({[}])'))
print(bal_symbol_checker('({[[]]]})'))
print(bal_symbol_checker('({[]}))'))
print(bal_symbol_checker('({[]x})'))