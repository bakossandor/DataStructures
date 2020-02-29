from collections import deque


class StackWithDeque:
    def __init__(self):
        self.items = deque()

    def add(self, item):
        self.items.append(item)

    def remove(self):
        try:
            self.items.pop()
        except IndexError:
            return

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def is_empty(self):
        if self.items:
            return True
        return False

# testing the deque implementation
st2 = StackWithDeque()
st2.add("item1")
st2.add("item2")
assert st2.is_empty() is True, "error"
assert st2.peek() == "item2", "error"
st2.remove()
assert st2.peek() == "item1", "error"
assert st2.is_empty() is True, "error"
st2.remove()
assert st2.is_empty() is False, "error"
assert st2.peek() is None, "error"
