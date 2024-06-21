
"""
Example of functions
"""

def hello():
    return "Hello, World!"

print(hello())

def hello_friend(friend_name):
    return f"Hello {friend_name}!"

print(hello_friend("Alice"))

def zero():
    return 0

def one():
    return 1

zero() + one()

zero() + one() + one()

def add_numbers(a, b):
    return a + b

print(add_numbers(2, 3))

print(add_numbers(zero(), one()))

