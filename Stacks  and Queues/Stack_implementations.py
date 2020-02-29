# We can implement stack in different ways
# the most common implementations are using array, using a linked list, and using a deque (double ended linked list)

# The stack has the following methods
# - Add - add element to the (top of) the stack
# - Remove - remove element from the (top of) the stack
# - Peek - return the top element from the stack
# - IsEmpty - return True if the stack has no element otherwise False

# Implementation with an array
class Stack:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self):
        if len(self.items) > 0:
            self.items.pop()
        return

    def peek(self):
        if len(self.items) > 0:
            return self.items[len(self.items) - 1]
        return None

    def is_empty(self):
        if len(self.items) > 0:
            return True
        return False

# testing the array implementation
st1 = Stack()
st1.add("item1")
st1.add("item2")
assert st1.is_empty() is True, "error"
assert st1.peek() == "item2", "error"
st1.remove()
assert st1.peek() == "item1", "error"
assert st1.is_empty() is True, "error"
st1.remove()
assert st1.is_empty() is False, "error"
assert st1.peek() is None, "error"
