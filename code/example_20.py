"""
Functions as first-class objects
"""
def zero():
    return 0

def one():
    return 1

zero() + one()

zero() + one() + one()

from functools import reduce

def sum(xs):
    reduce(lambda x, y: x + y, xs)

my_list_of_numbers = [1, 2, 3, 4, 5, one(), one()]

print(sum(my_list_of_numbers))

