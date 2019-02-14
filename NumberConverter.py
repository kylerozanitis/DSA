""" This file contains the program to convert a number to any base. It is an
extension of the common 'divide by 2' algorithm. """

from pythonds.basic.stack import Stack

def divide_by_two(number):
    s = Stack()

    while number > 0 :
        remainder = number % 2
        s.push(remainder)
        number = number // 2

    size = s.size()
    result = ""
    for item in range(size):
        result += str(s.pop())
    
    return result


def divide_by_base(number, base):
    """ This function takes any decimal number and any base between 2 and 16
    as parameters. As with divide_by_two, the remainders are still pushed onto
    the stack until the value being converted becomes 0. However, due to our
    base going beyond 10, we can no longer simply use the remainders so we
    need to create a set of digits that can be used to represent those
    remainders beyond 9. """

    digits = "0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F"
    rem_stack = Stack()

    while number > 0:
        remainder = number % base
        rem_stack.push(remainder)
        number = number // base

    result = ""
    while not rem_stack.isEmpty():
        result += str(rem_stack.pop())

    return result

print(divide_by_two(233))
print(divide_by_two(42))
print(divide_by_base(25, 2))
print(divide_by_base(25, 16))
